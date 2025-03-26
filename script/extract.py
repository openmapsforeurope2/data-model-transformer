import sys
from subprocess import call
import utils


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


def appendGeometryFieldToSelect(selectString, geometryfield, sourceSRID, targetSRID):
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
    geometryField = transformGeometryToWGS84(sourceSRID, targetSRID, geometryField)

    if transform is not None:
        geometryField = transform.replace('${}', geometryField)

    selectPart = geometryField

    #patch au cas ou la geometrie n'est pas renvoyée en WKB
    selectPart = "ST_AsEWKB("+selectPart+")"

    if fieldName : selectPart += " AS " + fieldName
        
    return selectString + ("," if selectString else "") + selectPart


def transformGeometryToWGS84(
    source_srid, target_srid, geometry_field
):
    if source_srid != target_srid:
        return "ST_Transform(ST_SetSRID("+geometry_field+", "+source_srid+"), " + target_srid +")"
    return geometry_field


def getWhereStatement( tableConf ):
    where_statement = ""
    if 'where' in tableConf and tableConf['where']:
        where_statement = " WHERE " + tableConf['where']
    return where_statement


def run(
    conf, pathOut, testOnly
):
    print("EXTRACTING...", flush=True)

    commandBase = utils.getCommandBase(conf['source_db'])

    for target_table, target_table_conf in conf['target_tables'].items():
        if 'mock' in target_table_conf and target_table_conf['mock'] : continue

        for table_name, table_conf in target_table_conf['source_tables'].items():
            if 'mock' in table_conf and table_conf['mock'] : continue

            table_conf['source_srid'] = conf['source_srid']
            table_conf['target_srid'] = conf['target_srid']

            full_table_name = getTableName(table_name, conf, table_conf)
            select = ""

            if 'mapping' in table_conf and table_conf['mapping']:
                for field, mappedField in table_conf['mapping'].items():
                    select = appendFieldToSelect( select, {field: mappedField} )

            if 'geomapping' in table_conf and table_conf['geomapping']:
                for field, mappedField in table_conf['geomapping'].items():
                    select = appendGeometryFieldToSelect( select, {field: mappedField}, table_conf["source_srid"], table_conf['target_srid'] )
            
            if 'fetched_fields' in table_conf and table_conf['fetched_fields']:
                for computational_field in table_conf['fetched_fields']:
                    select = appendFieldToSelect( select, computational_field )
            
            where_statement = getWhereStatement(table_conf)
            if testOnly:
                where_statement += " LIMIT 10"

            select = "SELECT " + select + " FROM " + full_table_name + where_statement
            query = "SELECT row_to_json(t) FROM ("+ select +") AS t"
            query = "\COPY ("+ query +") TO '"+ pathOut + "/" + utils.getTempFileNameConf(conf['country_code'], target_table, table_name) + ".json'"

            command = commandBase +' -c "'+ query +'"'

            print(u'command: {}'.format(command), flush=True)
            print('table: {}'.format(full_table_name), flush=True)

            returnValue = call( command, shell=True )
            if returnValue != 0:
                raise