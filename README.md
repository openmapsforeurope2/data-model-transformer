# data-model-transformer

Lancer le script transform.py

Les options de ce script sont:
  -h, --help                Afficher l'aide
  -v                        Mode verbeux
  -r                        Suppression des données existentes dans les tables avant restauration
  -c, --conf=FILE           Chemin vers le fichier JSON de configuration
  -o, --output-dir=DIR      Spécifier le dossier de sortie


Exemples:
~~~
python3 script/transform.py -c xx-trans.json -o data -r
~~~
