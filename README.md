# data-model-transformer


## Context

Open Maps For Europe 2 est un projet qui a pour objectif de développer un nouveau processus de production dont la finalité est la construction d'un référentiel cartographique pan-européen à grande échelle (1:10 000).

L'élaboration de la chaîne de production a nécessité le développement d'un ensemble de composants logiciels qui constituent le projet [OME2](https://github.com/openmapsforeurope2/OME2).


## Description

Ce projet fournir les scripts python permettant de convertir les données de leur modèle nationale vers le modèle OME2.


## Fonctionnement

La première étape du changement de modèle consiste à créer les [fichiers de configuration] (un fichier par pays-thème) s'il n'existe pas déjà ou à les modifier si le modèle de données de la nouvelle version des données sources d'un pays a évolué depuis la version antérieure.
Si le mapping entre les champs sources et cibles nécessite l'écriture de plusieurs lignes de code le fichier de configuration pourra appeler des fonctions dont le corps sera écrit dans un fichier portant le nom de la fonction stocké dans le dossier [functions](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions).

Précisions concernant certains paramètres de configuration:
- mock : si la valeur est 'true', permet de ne pas jouer la convertion pour la table en question
- where : instruction SQL pour filtrer les données sources à convertir
- mapping : défini les instructions de mapping pour chaque champ cible. Voici quelques exemples:
    - écriture du code directement dans le fichier de  configuration : `"national_code": {"eval": "data['nationalcode'] if data['nationalcode'] != '' else 'void_unk'"}`
    - appel d'une fonction stocké dans le répertoire functions : `"name": {"function": "inspire_xx_name"}`
    - affectation d'une valeur fixe : `"national_level_code": {"eval": "'void_unk'"}`
    - mapping directement de champ cible à champ source : `"w_national_identifier": "inspireid"`
- geomapping : permet de réaliser des transformations géométriques simples (projection, transtypage...)
- fetched_fields : liste des champs à charger depuis les données sources nécessaire au mapping. C'est informations sont stockées dans l'objet python `data`. Si le champ source fait l'objet d'un mapping champ à champ il n'est pas nécessaire de l'intégrer dans cette liste.

> _Note : il est possible d'utiliser des paramètres template (ex: `${un_parametre}`) faisant référence à un paramètre (`un_parametre`) présent dans le même fichier. Le template `${un_parametre}` sera réalisé lors du chargement de la configuration par l'application en le remplaçant par la valeur du paramètre `un_parametre`._

Le processus de transformation se déroule en trois phases :
1. extraction des données sources utiles dans des fichiers .json stockés dans un répertoire temporaire (output/tmp)
2. création des fichiers de dump .sql enregistré dans le répertoire output
3. restauration des fichiers dump dans la base cible

> _Notes :_
> - _le paramètre output est à renseigner dans le fichier de configuration conf.json_
> - _le dossier output/tmp est supprimé à l'issu du traitement_

> _Attention : il est important de s'assurer que le volume contenant le dossier output dispose bien de l'espace suffisant pour stocker les fichiers de dump et les fichiers temporaires qui sont tous volumineux._

## Configuration

La configuration est ici particulièrement importante car c'est elle qui recèle la logique de conversion.

Les fichiers de configuration se trouvent dans le [dossier de configuration](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/conf). On y trouve :
- le fichier template [conf.json.template](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/conf/conf.json.template) qui doit être réalisé en **conf.json**
- les fichiers de configuration **pays-theme.json** créés par l'utilisateur.
- le fichier **mapping_conf.json** permettant d'associer un pays à des fichier de configuration. L'utilisateur doit modifier ce fichier en conséquence lorsqu'il crée un nouveau fichier pays-theme.json.

Les fichiers de configuration peuvent être associés à des fonctions qui doivent être stockées dans le répertoire [functions](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions).


## Utilisation

L'outil s'utilise en ligne de commande.

Script options:
* -h, --help: display help
* -v, --verbose: verbose mode
* -s, --no_reset: not delete existing data before restore
* -c, --conf=FILE: path to JSON configuration file
* -t, --test: test mode (process only 10 objects)
* -n, --no_history: target database without life-cycle management system

<br>

Example on ome2_hvlsp_v4 (without life-cycle management):
~~~
python3 script/transform.py -c conf/conf.json --no_history
~~~

Example on ome2_hvlsp_v5 (with life-cycle management):
~~~
python3 script/transform.py -c conf/conf.json
~~~
 
