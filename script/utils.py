import json
import re
import sys
import os
from os import listdir
from os.path import isfile, join
from types import FunctionType


def getConf(confFile):
    """
    Fonction utilitaire pour la conversion du fichier de configuration json en objet python.

    Paramètres:
    confFile (path) : fichier de configuration

    Retourne:
    objet : configuration
    """

    with open(confFile) as f:
        confString = f.read()
        conf = json.loads(confString)

        match = re.search('\$\{[a-zA-Z_][a-zA-Z_.0-9]*\}', confString)
        while match:
            matchValue = match.group()[2:-1]
            matchValueParts = matchValue.split(".")

            value=conf
            for part in matchValueParts:
                value = value[part]
            
            confString = confString.replace(match.group(), value)

            match = re.search('\$\{[a-zA-Z_][a-zA-Z_.0-9]*\}', confString)

        return json.loads(confString)
    return None

def getTempFileNameConf(prefix, targetTableName, sourceTableName):
    return prefix + "_" + targetTableName + "_" + sourceTableName

def onWindows():
    return sys.platform.startswith("win")

def getCommandBase(conf):
    if onWindows():
        return 'psql -U "'+conf['user']+'" -h "'+conf['host']+'" -p "'+conf['port']+'" -d "'+conf['name']+'"'
    else:
        return 'PGPASSWORD="'+conf['pwd']+'" psql -U "'+conf['user']+'" -h "'+conf['host']+'" -p "'+conf['port']+'" -d "'+conf['name']+'"'

def getPythonBinName():
    if onWindows():
        return 'python.exe'
    else:
        return 'python3'

def getFunctions(functionsDir):
    functions = {}
    files = [f for f in listdir(functionsDir) if isfile(join(functionsDir, f))]
    for f in files:
        key = os.path.splitext(os.path.basename(f))[0]

        fopen = open(join(functionsDir, f), "r")
        f_code = compile("def "+key+"(context):\n"+fopen.read(), "<string>", "exec")
        functions[key] = FunctionType(f_code.co_consts[0], globals(), key)

    return functions