#!/usr/bin/env python3

import sys
import os
from subprocess import call
import utils


def restore(
    confFile, pathIn, verbose
):
    print("RESTORE...", flush=True)

    conf = utils.getConf(confFile)
    if conf is not None:

        prefix = conf['country_code']

        commandBase = 'PGPASSWORD="'+conf['target_db']['pwd']+'" psql -U "'+conf['target_db']['user']+'" -h "'+conf['target_db']['host']+'" -p "'+str(conf['target_db']['port'])+'" -d "'+conf['target_db']['name']+'"'

        for target_table, target_table_conf in conf['target_tables'].items():
            if 'mock' in target_table_conf and target_table_conf['mock'] : continue
                
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
        verbose = True if sys.argv[4] == 'true' else False
    except:
        print (comment)
        sys.exit()

    restore(confFile, pathIn, verbose)
