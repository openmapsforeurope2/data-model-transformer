import sys
import os
from subprocess import call
import utils


def run(
    conf, pathIn, reset, nohistory
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
                resetCommand += "BEGIN;"
                if not nohistory:
                    resetCommand += "SELECT nextval('seqnumrec');"
                resetCommand += 'UPDATE '+targetTableCompleteName+' SET gcms_detruit = true WHERE gcms_detruit = false AND '

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
                    resetCommand += "SELECT ign_gcms_finalize_transaction(" \
                            "currval('seqnumrec')::int," \
                            "-1," \
                            "'"+target_table+"'," \
                            "NULL," \
                            "NULL," \
                            "'FLUSH'," \
                            "'"+conf['country_code']+" data removal'," \
                            "ST_GeomFromText('MultiPolygon(((9 9, 9 9, 9 9, 9 9)))')," \
                            "(SELECT COUNT(*)::integer FROM "+targetTableCompleteName+" WHERE gcms_numrec = currval('seqnumrec'))," \
                            "NULL," \
                            "NULL" \
                        ");"
                    
                resetCommand += "COMMIT;"

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