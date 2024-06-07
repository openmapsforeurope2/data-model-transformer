# data-model-transformer

Run script transform.py

Script options:
* -h, --help: display help
* -v: Verbose mode
* -r: Delete existing data before restore
* -c, --conf=FILE: Path to JSON configuration file
* -o, --output-dir=DIR: Path to output directory
* -t, --test: Test mode (process only 10 objects)
* -n, --nohistory: Target database without life-cycle management system


Example:
~~~
python3 script/transform.py -c xx-trans.json -o data -r
~~~
