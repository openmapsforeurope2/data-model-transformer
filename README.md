# data-model-transformer

Purpose: transform data from a national or INSPIRE model to the OME2 data model

Run script transform.py

Script options:
* -h, --help: display help
* -v, --verbose: Verbose mode
* -s, --no_reset: Not delete existing data before restore
* -c, --conf=FILE: Path to JSON configuration file
* -t, --test: Test mode (process only 10 objects)
* -n, --no_history: Target database without life-cycle management system

Example on ome2_hvlsp_v4 (without life-cycle management):
~~~
python3 script/transform.py -c conf/conf.json --no_history
~~~

Example on ome2_hvlsp_v5 (with life-cycle management):
~~~
python3 script/transform.py -c conf/conf.json
~~~
 
