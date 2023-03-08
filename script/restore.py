import sys
import os
from subprocess import call
import utils


def restore(
    confFile, pathIn, reset, verbose
):
    print("RESTORE...", flush=True)

    conf = utils.getConf(confFile)
    if conf is not None:

        prefix = conf['country_code']

        commandBase = utils.getCommandBase(conf['target_db'])

        for target_table, target_table_conf in conf['target_tables'].items():
            if 'mock' in target_table_conf and target_table_conf['mock'] : continue

            if reset:
                targetTableCompleteName = ( conf['target_db']['schema']+"." if conf['target_db']['schema'] else "") + target_table
                resetCommand = commandBase + ' -q -c "DELETE FROM '+targetTableCompleteName+'"'
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

    restore(confFile, pathIn, reset, verbose)
