import os
import sys
import getopt
from datetime import datetime
import shutil
import utils
import extract
import dump
import restore

def transform(argv):

    currentDir = os.path.dirname(os.path.abspath(__file__))

    arg_conf = ""
    arg_output = os.path.dirname(currentDir)+"/data"
    arg_reset = False
    arg_verbose = False
    arg_help = "{0} -c <conf> -o <output> -v".format(argv[0])
    arg_test = False
    
    try:
        opts, args = getopt.getopt(argv[1:], "hc:o:vr", ["help", "conf=", 
        "output=", "verbose", "reset", "test"])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-c", "--conf"):
            arg_conf = arg
        elif opt in ("-o", "--output"):
            arg_output = arg
        elif opt in ("-r", "--reset"):
            arg_reset = True
        elif opt in ("-v", "--verbose"):
            arg_verbose = True
        elif opt in ("-t", "--test"):
            arg_test = True


    print('conf:', arg_conf)
    print('output:', arg_output)
    print('reset:', arg_reset)
    print('verbose:', arg_verbose)
    print('test:', arg_test)

    workspace = os.path.dirname(currentDir)+"/"
    tempDir = arg_output + "/tmp"

    if not os.path.isfile(workspace+"conf/"+arg_conf):
        print("le fichier de configuration "+ arg_conf + " n'existe pas.")
        sys.exit(2)
    arg_conf = workspace+"conf/"+arg_conf

    if not os.path.exists(arg_output):
        os.makedirs(arg_output)

    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)
    os.makedirs(tempDir)

    print("[START TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    conf = utils.getConf(arg_conf)
    functions = utils.getFunctions(workspace+"/functions")

    extract.run(conf, tempDir, arg_test)
    dump.run(functions, conf, tempDir, arg_output)
    restore.run(conf, arg_output, arg_reset, arg_verbose)

    shutil.rmtree(tempDir)

    print("[END TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    transform(sys.argv)