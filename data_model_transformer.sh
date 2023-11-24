#!/bin/sh
python3 script/transform.py -c be-au.json -o data -r
python3 script/transform.py -c fr-au.json -o data -r
python3 script/transform.py -c nl-au.json -o data -r

python3 script/transform.py -c be-trans.json -o data -r
python3 script/transform.py -c fr-trans.json -o data -r
python3 script/transform.py -c nl-trans.json -o data -r