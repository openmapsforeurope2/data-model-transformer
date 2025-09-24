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
    arg_noreset = False
    arg_verbose = False
    arg_test = False
    arg_nohistory = False # life-cycle management is enabled as default
    
    try:
        opts, args = getopt.getopt(argv[1:], "hc:vstn", ["help", "conf=", 
        "verbose", "no_reset", "test", "no_history"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)
		

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(1)
        elif opt in ("-c", "--conf"):
            arg_conf = arg
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

    source_db={}
    source_db["host"]=os.environ["PGHOST"]
    source_db["port"]=os.environ["PGPORT"]
    source_db["name"]=os.environ["PGDATABASE-NAT"]
    source_db["user"]=os.environ["PGUSER"]
    source_db["pwd"]=os.environ["PGPASSWORD"]
    source_db["schema"]=os.environ["PGSCHEMA-NAT"]
	
    target_db={}
    target_db["host"]=os.environ["PGHOST"]
    target_db["port"]=os.environ["PGPORT"]	
    target_db["name"]=os.environ["PGDATABASE"]
    target_db["user"]=os.environ["PGUSER"]
    target_db["pwd"]=os.environ["PGPASSWORD"]
    target_db["schema"]=os.environ["PGSCHEMA"]
	
    conf["source_db"]=source_db
    conf["target_db"]=target_db


    #mapping conf
    if not os.path.isfile(conf["mapping_conf_file"]):
        print("The mapping configuration file "+ conf["mapping_conf_file"] + " does not exist.")
        sys.exit(1)

    mapping_conf = utils.getConf(conf["mapping_conf_file"])

    #process conf
    process_conf_file = os.path.join(os.path.dirname(conf["mapping_conf_file"]), mapping_conf[os.environ["COUNTRY"]]["conf_file"][os.environ["THEME"]])
    process_conf = utils.getConf(process_conf_file)

    #merge conf
    conf.update(process_conf)

    if not os.path.exists(conf["output_dir"]):
        os.makedirs(conf["output_dir"])

    print('conf:', arg_conf)
    print('output:', conf["output_dir"])
    print('no_reset:', arg_noreset)
    print('verbose:', arg_verbose)
    print('test:', arg_test)
    print('no_history:', arg_nohistory)


    tempDir = conf["output_dir"] + "/tmp"

    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)
    os.makedirs(tempDir)

    print("[START TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    functions = utils.getFunctions(conf["functions_dir"])

    #--
    try:
        extract.run(conf, tempDir, arg_test)
    except:
        print("EXTRACT ERROR")
        sys.exit(1)

    #--
    try:
        dump.run(functions, conf, tempDir, conf["output_dir"])
    except:
        print("DUMP ERROR")
        sys.exit(1)

    #--
    try:
        restore.run(conf, conf["output_dir"], not arg_noreset, arg_nohistory, arg_verbose)
    except:
        print("RESTORE ERROR")
        sys.exit(1)

    #--
    shutil.rmtree(tempDir)

    print("[END TRANSFORM] "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    run(sys.argv)