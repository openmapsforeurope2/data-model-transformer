import json
import traceback
import utils


def run(
    functions, conf, pathIn, pathOut, nohistory
):
    print("DUMP...", flush=True)

    if conf is not None:
        prefix = conf['country_code']

        for target_table, target_table_conf in conf['target_tables'].items():
            if 'mock' in target_table_conf and target_table_conf['mock'] : continue

            exportPath = '{}/{}_{}.sql'.format(pathOut, prefix, target_table)

            with open(exportPath, 'w') as outFile:
                count = 0

                # pour historisation
                if not nohistory:
                    outFile.write("BEGIN;\n")
                    outFile.write("SELECT nextval('seqnumrec');\n")

                for table_name, table_conf in target_table_conf['source_tables'].items():
                    if 'mock' in table_conf and table_conf['mock'] : continue

                    importPath = pathIn+'/'+utils.getTempFileNameConf(prefix, target_table, table_name)+'.json'
                    table_conf['target_table'] = ( conf['target_db']['schema']+"." if conf['target_db']['schema'] else "") + target_table

                    
                    with open(importPath, 'r') as inFile:
                        for ligne in inFile:
                            count += 1

                            ligne = ligne.replace("\\\\","\\")
                            data = json.loads(ligne)

                            insertStatement = getInsertStatement( data, table_conf, count, importPath, functions )
                            outFile.write(insertStatement.encode('utf8').decode()+"\n")

                # pour historisation
                if not nohistory:
                    # on enregistre l'objet reconciliation
                        #numéro de réconciliation
                        #numéro de client
                        #classes impactées
                        #nom de la zone de reconciliation (ex: be#fr ?)
                        #changement zr
                        #nature de l'operation
                        #commentaire
                        #géométried de la zone de réconciliation
                        #nombre d'objets
                        #operateur zr (user)
                        #groupe/profil
                        #source --> DEFAULT NULL
                    recStatement = "SELECT ign_gcms_finalize_transaction(" \
                            "currval('seqnumrec')::int," \
                            "-1," \
                            "'"+target_table+"'," \
                            "NULL," \
                            "NULL," \
                            "'INIT'," \
                            "'"+conf['country_code']+" data initialization'," \
                            "ST_GeomFromText('MultiPolygon(((9 9, 9 9, 9 9, 9 9)))')," \
                            +str(count)+"," \
                            "NULL," \
                            "NULL" \
                        ");"
                    outFile.write(recStatement+"\n")
                    outFile.write("COMMIT;\n")

                print('{} {}'.format(count, target_table), flush=True)


def getInsertStatement(data, tableConf, line, file, functions ):
    fields = []
    values = []

    # pour historisation
    fields.append("gcms_numrec")
    values.append("currval('seqnumrec')")
    fields.append("gcms_date_creation")
    values.append("NOW()")

    if 'mapping' in tableConf and tableConf['mapping']:
        for field, mappedField in tableConf['mapping'].items():
            fields.append(field)
            value = None

            if isinstance(mappedField, dict):
                try:
                    if 'eval' in mappedField:
                        value = eval(mappedField['eval'], {'data': data, 'json': json})
                    elif 'function' in mappedField:
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

            if value is None: # or (isinstance(value, list) and len(value) == 0):
                value = 'NULL'
            elif isinstance(value, list) :
                if len(value) == 0:
                    value = '\'{}\'::json'
                # Cas des champs jsonb
                elif isinstance(value[0], dict):
                    value = toJsonArray(value)
                else:
                    value = toSqlArray(value)
            elif isinstance(value, dict) :
                # Cas des champs jsonb
                if len(value) == 0:
                    value = '\'{}\'::json'
                else:
                    value = '\'' + str(value).replace("\'",'"') + '\''
            elif isinstance(value, (int, float)):
                value = str(value)
            else:
                value = value.replace("\'","\'\'")
                value = "\'"+value+"\'"

            values.append(value)
    
    if 'geomapping' in tableConf and tableConf['geomapping']:
        for field, mappedField in tableConf['geomapping'].items():
            if data[field] is None:
                data[field] = 'NULL'
            else:
                data[field] = "\'"+data[field].replace("\\x","")+"\'"

            fields.append(field)
            values.append(data[field])

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


def toJsonArray( ls ) :
    newList = []
    for l in ls:
        if l is None or not l :
            continue
        else:
            l = convertEncodedCharacters(json.dumps(l))
            newList.append(l)

    if len(newList) == 0 : 
        return None

    newList = str(newList)
    newList = newList.replace("\'{", "{")
    newList = newList.replace("}\'", "}")
    newList = newList.replace("\\'", "\'\'")
    newList = "\'" + newList + "\'"

    return newList


def convertEncodedCharacters(substring):
    # Equivalences entre les caractères spéciaux de l'API et les chaines Python
    charConversion = {
        "\\u00e0": 'à',
        "\\u00e1": 'á',
        "\\u00e2": 'â',
        "\\u00e4": 'ä',
        "\\u00e7": 'ç',
        "\\u010d": 'č',
        "\\u010c": 'Č',
        "\\u010f": 'ď',
        "\\u00e8": 'è',
        "\\u00e9": 'é',
        "\\u00ea": 'ê',
        "\\u00eb": 'ë',
        "\\u011b": 'ě',
        "\\u00ee": 'î',
        "\\u00ef": 'ï',
        "\\u00ed": 'í',
        "\\u0148": 'ň',
        "\\u00f4": 'ô',
        "\\u00f6": 'ö',
        "\\u0158": 'Ř',
        "\\u0159": 'ř',
        "\\u0160": 'Š',
        "\\u0161": 'š',
        "\\u0165": 'ť',
        "\\u00f9": 'ù',
        "\\u00fb": 'û',
        "\\u00fc": 'ü',
        "\\u00da": 'Ú',
        "\\u00fa": 'ú',
        "\\u016f": 'ů',
        "\\u00fd": 'ý',
        "\\u017d": 'Ž',
        "\\u017e": 'ž'
        
    }

    newString = substring
    for c, v in charConversion.items():
        newString = newString.replace(c, v)
    return newString

