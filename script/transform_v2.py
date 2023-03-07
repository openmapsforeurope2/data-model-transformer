#!/usr/bin/env python3

import os
import sys
import getopt
from datetime import datetime
import shutil

def transform(argv):

    currentDir = os.path.dirname(os.path.abspath(__file__))

    arg_conf = ""

    if on_windows:
        arg_output = os.path.dirname(currentDir)+"/data"
    else:
        arg_output = currentDir+"/../data"

    arg_reset = "false"
    arg_verbose = "false"
    arg_help = "{0} -c <conf> -o <output> -v".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hc:o:vr", ["help", "conf=", 
        "output=", "verbose", "reset"])
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
            arg_reset = "true"
        elif opt in ("-v", "--verbose"):
            arg_verbose = "true"

    print('conf:', arg_conf)
    print('output:', arg_output)
    print('reset:', arg_reset)
    print('verbose:', arg_verbose)

    if on_windows:
        workspace = os.path.dirname(currentDir)+"/"
        tempDir = arg_output + "/tmp"
    else:
        workspace=currentDir+"/../"
        tempDir=arg_output+"/tmp"

    if not os.path.isfile(workspace+"conf/"+arg_conf):
        print("le fichier de configuration "+ arg_conf + " n'existe pas.")
        sys.exit(2)

    if not os.path.exists(arg_output):
        os.makedirs(arg_output)

    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)
    os.makedirs(tempDir)

    print("[START TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    os.system(workspace+"script/extract_v2.py {0} {1} {2} {3}".format(workspace, arg_conf, tempDir, arg_verbose))
    os.system(workspace+"script/dump_v2.py {0} {1} {2} {3} {4}".format(workspace, arg_conf, tempDir, arg_output, arg_verbose))
    os.system(workspace+"script/restore_v2.py {0} {1} {2} {3} {4}".format(workspace, arg_conf, arg_output, arg_reset, arg_verbose))
    shutil.rmtree(tempDir)

    print("[END TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    on_windows = True if sys.platform.startswith("win") else False
    transform(sys.argv)