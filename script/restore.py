import sys
import os
from subprocess import call
import utils


def run(
    conf, pathIn, reset, nohistory, verbose
):
    print("RESTORE...", flush=True)

    if conf is not None:

        prefix = conf['country_code']

        commandBase = utils.getCommandBase(conf['target_db'])

        for target_table, target_table_conf in conf['target_tables'].items():
            if 'mock' in target_table_conf and target_table_conf['mock'] : continue

            if reset:
                targetTableCompleteName = ( conf['target_db']['schema']+"." if conf['target_db']['schema'] else "") + target_table
                resetCommand = commandBase + ' -q -c "'
                if not(nohistory):
                    resetCommand += 'ALTER TABLE '+targetTableCompleteName+ ' DISABLE TRIGGER ign_gcms_history_trigger; '
                resetCommand += 'DELETE FROM '+targetTableCompleteName+' WHERE '
                whereClause = ""

                #Multiple country codes
                if not 'country_code_list' in conf or conf['country_code_list'] is None:
                    whereClause = conf['target_country_field']+'=\''+conf['country_code']+'\''

                else:
                    whereClause = conf['target_country_field'] + ' IN ('
                    for code in conf['country_code_list']:
                        whereClause += '\'' + code + '\','
                    whereClause = whereClause[0:len(whereClause)-1] + ')'

                resetCommand += whereClause + ';'
                if not(nohistory):
                    resetCommand += ' ALTER TABLE '+targetTableCompleteName+ ' ENABLE TRIGGER ign_gcms_history_trigger;'
                resetCommand += '"'

                print(resetCommand)

                returnValue = call( resetCommand, shell=True )
                if returnValue != 0:
                    raise
                
            dumpFile = '{}/{}_{}.sql'.format(pathIn, prefix, target_table)

            restoreCommand = commandBase + " -q -f "+dumpFile
            print(restoreCommand)

            returnValue = call( restoreCommand, shell=True )
            if returnValue != 0:
                raise