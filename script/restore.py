import json
import sys
import os
from subprocess import call


def run(
    confFile, pathIn, verbose
):
    with open(confFile, 'r') as f:
        conf = json.load(f)

        prefix = conf['country_code']

        commandBase = 'PGPASSWORD="'+conf['target_db']['pwd']+'" psql -U "'+conf['target_db']['user']+'" -h "'+conf['target_db']['host']+'" -p "'+str(conf['target_db']['port'])+'" -d "'+conf['target_db']['name']+'"'

        for table_name, table_conf in conf['source_tables'].items():
            if 'mock' in table_conf and table_conf['mock'] : continue
            
            dumpFile = '{}/{}_{}.sql'.format(pathIn, prefix, table_name)

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

    run(confFile, pathIn, verbose)
