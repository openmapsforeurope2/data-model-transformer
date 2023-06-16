import sys
import os
from subprocess import call
import utils


def run(
    conf, pathIn, reset, verbose
):
    print("RESTORE...", flush=True)

    if conf is not None:

        prefix = conf['country_code']

        commandBase = utils.getCommandBase(conf['target_db'])

        for target_table, target_table_conf in conf['target_tables'].items():
            if 'mock' in target_table_conf and target_table_conf['mock'] : continue

            if reset:
                targetTableCompleteName = ( conf['target_db']['schema']+"." if conf['target_db']['schema'] else "") + target_table
                resetCommand = commandBase + ' -q -c "DELETE FROM '+targetTableCompleteName+' WHERE '
                whereClause = ""

                #Multiple country codes
                if not 'country_code_list' in conf or conf['country_code_list'] is None:
                    whereClause = conf['target_country_field']+'=\''+conf['country_code']+'\''

                else:
                    whereClause = conf['target_country_field'] + ' IN ('
                    for code in conf['country_code_list']:
                        whereClause += '\'' + code + '\','
                    whereClause = whereClause[0:len(whereClause)-1] + ')'

                resetCommand += whereClause + '"'

                print(resetCommand)
                call( resetCommand, shell=True )
                
            dumpFile = '{}/{}_{}.sql'.format(pathIn, prefix, target_table)

            restoreCommand = commandBase + " -q -f "+dumpFile
            print(restoreCommand)
            call( restoreCommand, shell=True )


if __name__ == "__main__":
    comment = '''
    Usage : restore <conf.json> <input path> <verbose>
    '''

    try:
        workspace = sys.argv[1]
        confFile = workspace+"/conf/"+sys.argv[2]
        pathIn = sys.argv[3]
        reset = True if sys.argv[4] == 'true' else False
        verbose = True if sys.argv[5] == 'true' else False
    except:
        print (comment)
        sys.exit()

    conf = utils.getConf(confFile)
    run(conf, pathIn, reset, verbose)
