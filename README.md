# data-model-transformer

Run script transform.py

Script options:
* -h, --help: display help
* -v: Verbose mode
* -r: Delete existing data before restore
* -c, --conf=FILE: Path to JSON configuration file
* -o, --output-dir=DIR: Path to output directory
* -t, --test: Test mode (process only 10 objects)
* -n, --no_history: Target database without life-cycle management system

Example on ome2_hvlsp_v4 (without life-cycle management):
~~~
python3 script/transform.py -c xx-trans.json -o data -r --no_history
~~~

Example on ome2_hvlsp_v5 (with life-cycle management):
~~~
python3 script/transform.py -c xx-trans.json -o data -r
~~~
