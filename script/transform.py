import os
import sys
import getopt
from datetime import datetime
import shutil
import utils
import extract
import dump
import restore
import re


def run(argv):
    
    arg_conf = ""
    arg_output = ""
    arg_noreset = False
    arg_verbose = False
    arg_help = "{0} -c <conf> -o <output> -v".format(argv[0])
    arg_test = False
    arg_nohistory = False # life-cycle management is enabled as default
    
    try:
        opts, args = getopt.getopt(argv[1:], "hc:o:vstn", ["help", "conf=", 
        "output=", "verbose", "no_reset", "test", "no_history"])
    except:
        print(arg_help)
        sys.exit(1)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(1)
        elif opt in ("-c", "--conf"):
            arg_conf = arg
        elif opt in ("-o", "--output"):
            arg_output = arg
        elif opt in ("-s", "--no_reset"):
            arg_noreset = True
        elif opt in ("-v", "--verbose"):
            arg_verbose = True
        elif opt in ("-t", "--test"):
            arg_test = True
        elif opt in ("-n", "--no_history"):
            arg_nohistory = True

    #configuration
    if not os.path.isfile(arg_conf):
        print("The configuration file "+ arg_conf + " does not exist.")
        sys.exit(1)
    
    conf = utils.getConf(arg_conf)

    #mapping conf
    if not os.path.isfile(conf["mapping_conf"]):
        print("The mapping configuration file "+ conf["mapping_conf_file"] + " does not exist.")
        sys.exit(1)

    mapping_conf = utils.getConf(conf["mapping_conf_file"])

    #process conf
    process_conf = os.path.join(os.path.dirname(conf["mapping_conf_file"]), mapping_conf[conf["country"]]["conf_file"][conf["theme"]])

    #merge conf
    conf.update(process_conf)


    if arg_output == "" :
        arg_output = conf["output"]
    if arg_output == "" :
        arg_output = workspace+"data"

    if not os.path.exists(arg_output):
        os.makedirs(arg_output)

    print('conf:', arg_conf)
    print('output:', arg_output)
    print('no_reset:', arg_noreset)
    print('verbose:', arg_verbose)
    print('test:', arg_test)
    print('no_history:', arg_nohistory)

    tempDir = arg_output + "/tmp"

    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)
    os.makedirs(tempDir)

    print("[START TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    functions = utils.getFunctions(workspace+"/functions")

    #--
    try:
        extract.run(conf, tempDir, arg_test)
    except:
        print("EXTRACT ERROR")
        sys.exit(1)

    #--
    try:
        dump.run(functions, conf, tempDir, arg_output)
    except:
        print("DUMP ERROR")
        sys.exit(1)

    #--
    try:
        restore.run(conf, arg_output, not arg_noreset, arg_nohistory, arg_verbose)
    except:
        print("RESTORE ERROR")
        sys.exit(1)

    #--
    shutil.rmtree(tempDir)

    print("[END TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    run(sys.argv)