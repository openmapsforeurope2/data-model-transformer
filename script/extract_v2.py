

import sys
from subprocess import call
import utils


def getCommandBase(conf):
    if on_windows:
        return 'psql -U "'+conf['source_db']['user']+'" -h "'+conf['source_db']['host']+'" -p "'+conf['source_db']['port']+'" -d "'+conf['source_db']['name']
    else:
        return 'PGPASSWORD="'+conf['source_db']['pwd']+'" psql -U "'+conf['source_db']['user']+'" -h "'+conf['source_db']['host']+'" -p "'+conf['source_db']['port']+'" -d "'+conf['source_db']['name']


def getTableName(table_name, conf, table_conf):
    source_schema = conf['source_db']['schema'] if conf['source_db']['schema'] else ""

    #si un schema particulier est specifie pour la table
    schema_prefix=source_schema
    if 'schema' in table_conf and table_conf['schema']:
        schema_prefix = table_conf['schema']

    schema_prefix =  schema_prefix+"." if schema_prefix else ""

    return schema_prefix + table_name


def appendFieldToSelect(selectString, field):
    fieldName = ""
    if isinstance(field, dict) :
        fieldName = next(iter(field))
        mappedField = field[fieldName]

        if isinstance(mappedField, dict) :
            return selectString
    else:
        mappedField = field

    selectPart = mappedField

    if fieldName : selectPart += " AS " + fieldName

    return selectString + ("," if selectString else "") + selectPart


def appendGeometryFieldToSelect(selectString, geometryfield, sourceSRID):
    fieldName = ""
    transform = None
    if isinstance(geometryfield, dict) :
        fieldName = next(iter(geometryfield))
        mappedField = geometryfield[fieldName]

        if isinstance(mappedField, dict):
            sourceName = next(iter(mappedField))
            if 'transform' in mappedField[sourceName] and mappedField[sourceName]['transform']:
                transform = mappedField[sourceName]['transform']
            mappedField = sourceName
            
    else:
        mappedField = geometryfield

    geometryField = mappedField
    geometryField = transformGeometryToWGS84(sourceSRID, geometryField)

    if transform is not None:
        geometryField = transform.replace('${}', geometryField)

    selectPart = geometryField

    #patch au cas ou la geometrie n'est pas renvoyée en WKB
    selectPart = "ST_AsEWKB("+selectPart+")"

    if fieldName : selectPart += " AS " + fieldName
        
    return selectString + ("," if selectString else "") + selectPart


def transformGeometryToWGS84(
    source_srid, geometry_field
):
    if source_srid != "4326":
        return "ST_Transform(ST_SetSRID("+geometry_field+", "+source_srid+"), 4326)"
    return geometry_field


def getWhereStatement( tableConf ):
    where_statement = ""
    if 'where' in tableConf and tableConf['where']:
        where_statement = " WHERE " + tableConf['where']
    return where_statement


def extract(
    conf, pathOut
):
    print("EXTRACTING...", flush=True)

    command_base = getCommandBase(conf)

    for target_table, target_table_conf in conf['target_tables'].items():
        if 'mock' in target_table_conf and target_table_conf['mock'] : continue

        for table_name, table_conf in target_table_conf['source_tables'].items():
            if 'mock' in table_conf and table_conf['mock'] : continue

            table_conf['source_srid'] = conf['source_srid']

            full_table_name = getTableName(table_name, conf, table_conf)
            select = ""

            if 'mapping' in table_conf and table_conf['mapping']:
                for field, mappedField in table_conf['mapping'].items():
                    select = appendFieldToSelect( select, {field: mappedField} )

            if 'geomapping' in table_conf and table_conf['geomapping']:
                for field, mappedField in table_conf['geomapping'].items():
                    select = appendGeometryFieldToSelect( select, {field: mappedField}, table_conf["source_srid"] )
            
            if 'fetched_fields' in table_conf and table_conf['fetched_fields']:
                for computational_field in table_conf['fetched_fields']:
                    select = appendFieldToSelect( select, computational_field )
            
            where_statement = getWhereStatement(table_conf)

            select = "SELECT " + select + " FROM " + full_table_name + where_statement
            query = "SELECT row_to_json(t) FROM ("+ select +") AS t"
            query = "\COPY ("+ query +") TO '"+ pathOut + "/" + utils.getTempFileNameConf(conf['country_code'], target_table, table_name) + ".json'"

            command = command_base +'" -c "'+ query +'"'

            print(u'command: {}'.format(command), flush=True)
            print('table: {}'.format(full_table_name), flush=True)

            call( command, shell=True )


if __name__ == "__main__":
    comment = '''
    Usage : extract <conf.json> <output path> <verbose>
    '''
    try:
        workspace = sys.argv[1]
        confFile = workspace+"/conf/"+sys.argv[2]
        pathOut = sys.argv[3]
        verbose = True if sys.argv[4] == 'true' else False
        on_windows = True if sys.platform.startswith("win") else False
    except:
        print (comment)
        sys.exit()

    conf = utils.getConf(confFile)

    if conf is not None:
        extract(conf, pathOut)