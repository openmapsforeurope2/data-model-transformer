#!/bin/sh

# set -x

currentDir=$(dirname "$0")
confFile=""
workspace=$currentDir"/../"
output=$currentDir"/../data"
tempDir=$output"/tmp"
verbose=false
reset=false

while test $# -gt 0; do
  case "$1" in
    -h|--help)
      echo "Transformation de modèle."
      echo " "
      echo "options:"
      echo "-h, --help                Afficher l'aide"
      echo "-v                        Mode verbeux"
      echo "-r                        Suppression des données existentes dans les tables avant restauration"
      echo "-c, --conf=FILE           Chemin vers le fichier JSON de configuration"
      echo "-o, --output-dir=DIR      Spécifier le dossier de sortie"
      exit 0
      ;;
    -v)
      shift
      verbose=true
      ;;
    -r)
      shift
      reset=true
      ;;
    -c)
      shift
      if test $# -gt 0; then
        confFile=$1
        if [ ! -f "$workspace/conf/$confFile" ]; then
            echo "Le fichier de configuration $confFile n'existe pas"
            exit 1
        fi
      else
        echo "pas de fichier après l'option -c"
        exit 1
      fi
      shift
      ;;
    --conf*)
      if test $# -gt 0; then
        confFile=`echo $1 | sed -e 's/^[^=]*=//g'`
        if [ ! -f "$workspace/conf/$confFile" ]; then
            echo "Le fichier de configuration $confFile n'existe pas"
            exit 1
        fi
      else
        echo "pas de fichier après l'option --conf"
        exit 1
      fi
      shift
      ;;
    -o)
      shift
      if test $# -gt 0; then
        output=$1
      else
        echo "pas de dossier après l'option -o"
        exit 1
      fi
      shift
      ;;
    --output-dir*)
      if test $# -gt 0; then
        output=`echo $1 | sed -e 's/^[^=]*=//g'`
      else
        echo "pas de dossier après l'option -o"
        exit 1
      fi
      shift
      ;;
    *)
      break
      ;;
  esac
done


python --version >/dev/null 2>&1
if [ $? != 0 ]; then
  echo "python n'est pas disponible"
  exit 1
fi

workspace=$(realpath $workspace)
tempDir=$(realpath $tempDir)

output=$(realpath $output)
if [ ! -d $output ]; then
  mkdir -p $output;
fi

if [ -d $tempDir ]; then
  rm -r $tempDir;
fi
mkdir -p $tempDir;

echo "[START TRANSFORM]" $(date +"%m-%d-%Y %H:%M:%S")

python3 $currentDir"/extract.py" $workspace $confFile $tempDir $verbose
python3 $currentDir"/dump.py" $workspace $confFile $tempDir $output $verbose
python3 $currentDir"/restore.py" $workspace $confFile $output $reset $verbose
rm -r $tempDir

echo "[END TRANSFORM]" $(date +"%m-%d-%Y %H:%M:%S")