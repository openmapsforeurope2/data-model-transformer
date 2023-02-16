import json
import sys
import traceback
from subprocess import call
import os
from os import listdir
from os.path import isfile, join
from types import FunctionType


def dump(
    workspace, confFile, pathIn, pathOut
):
    print("DUMP...", flush=True)

    functions = getFunctions(workspace)

    with open(confFile) as f:
        conf = json.load(f)
        prefix = conf['country_code']
        target_table = ( conf['target_db']['schema']+"." if conf['target_db']['schema'] else "") + conf['target_table']

        for table_name, table_conf in conf['source_tables'].items():
            importPath = '{}/{}_{}.json'.format(pathIn, prefix, table_name)
            exportPath = '{}/{}_{}.sql'.format(pathOut, prefix, table_name)
            table_conf['target_geometry'] = conf['target_geometry']
            table_conf['target_table'] = target_table

            # classe simulée
            if 'mock' in table_conf and table_conf['mock'] : continue

            with open(exportPath, 'w') as outFile:
                count = 0
                with open(importPath, 'r') as inFile:
                    for ligne in inFile:
                        count += 1

                        ligne = ligne.replace("\\\\","\\")
                        data = json.loads(ligne)

                        insertStatement = getInsertStatement( data, table_conf, count, importPath, functions )
                        outFile.write(insertStatement.encode('utf8').decode()+"\n")
                        
                    print('{} {}'.format(count, table_name), flush=True)


def getInsertStatement(data, tableConf, line, file, functions ):
    fields = []
    values = []
    if 'mapping' in tableConf and tableConf['mapping']:
        for field, mappedField in tableConf['mapping'].items():
            fields.append(field)
            value = None
            
            if isinstance(mappedField, dict):
                if 'eval' in mappedField:
                    try:
                        value = eval(mappedField['eval'], {'data': data, 'json': json})
                    except Exception as e:
                        print("file: "+file)
                        print("line: "+str(line))
                        print("field: "+field)
                        print("data:")
                        print(json.dumps(data))
                        print("error:")
                        print(traceback.format_exc())
                        raise
                elif 'function' in mappedField:
                    try:
                        value = functions[mappedField['function']]({'data': data, 'json': json})
                    except Exception as e:
                        print("file: "+file)
                        print("line: "+str(line))
                        print("field: "+field)
                        print("data:")
                        print(json.dumps(data))
                        print("error:")
                        print(traceback.format_exc())
                        raise
            else:
                value = data[field]
            
            if value is None:
                value = 'NULL'
            elif isinstance(value, list) :
                value = toSqlArray(value)
            elif isinstance(value, (int, float)):
                value = str(value)
            else:
                value = value.replace("\'","\'\'")
                value = "\'"+value+"\'"

            values.append(value)
    
    if data[tableConf['target_geometry']] is None:
        data[tableConf['target_geometry']] = '\\N'
    else:
        data[tableConf['target_geometry']] = "\'"+data[tableConf['target_geometry']].replace("\\x","")+"\'"

    fields.append(tableConf['target_geometry'])
    values.append(data[tableConf['target_geometry']])

    try:
        insertStatement = "INSERT INTO " + tableConf["target_table"] + " (" + u",".join(fields) + ") VALUES (" + u",".join(values) + ");"
    except Exception as e:
        print("insertStatement:")
        print("\nfields:")
        print(json.dumps(fields))
        print("\nvalues:")
        print(json.dumps(values))
        print("\nerror:")
        print(traceback.format_exc())
        raise
    
    return insertStatement


def listToString( ls, delimitor ) :
    newList = []
    for l in ls:
        if l is None or not l :
            continue
        else:
            if not isinstance(l,(str)) : l = str(l)
            newList.append("\""+l+"\"")
    if len(newList) == 0 : return None
    return delimitor.join(newList)


def toSqlArray( ls, separator = ",") :
    newList = listToString( ls, separator )
    if newList is None :
        newList = ""
    newList = "{" + newList + "}"
    return newList


def getFunctions(workspace):
    functions = {}
    functionsDir=workspace+"/functions"
    files = [f for f in listdir(functionsDir) if isfile(join(functionsDir, f))]
    for f in files:
        key = os.path.splitext(os.path.basename(f))[0]

        fopen = open(join(functionsDir, f), "r")
        f_code = compile("def "+key+"(context):\n"+fopen.read(), "<string>", "exec")
        functions[key] = FunctionType(f_code.co_consts[0], globals(), key)

    return functions
        


if __name__ == "__main__":
    comment = '''
    Usage : dump <conf.json> <input path> <output path> <verbose>
    '''

    try:
        workspace = sys.argv[1]
        confFile = workspace+"/conf/"+sys.argv[2]
        pathIn = sys.argv[3]
        pathOut = sys.argv[4]
        verbose = True if sys.argv[5] == 'true' else False
    except:
        print (comment)
        sys.exit()

    dump(workspace, confFile, pathIn, pathOut)
