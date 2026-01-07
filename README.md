# data-model-transformer


## Context

Open Maps For Europe 2 is a project aimed at developing a new production process whose goal is to build a large-scale (1:10,000) pan-European mapping reference.

The development of the production pipeline required the creation of a set of software components that make up the [OME2](https://github.com/openmapsforeurope2/OME2) project. 

## Description

This project provides Python scripts to convert data from their national model to the OME2 model.

## How it works

The first step in the model transformation is to create the [configuration files] (one file per country-theme) if they do not already exist or to modify them if the data model of the new version of a country’s source data has changed since the previous version.
If the mapping between source and target fields requires writing several lines of code, the configuration file can call functions whose bodies are written in files named after the function and stored in the [functions](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions) folder.

Details regarding certain configuration parameters:
- mock: if the value is 'true', the conversion for the given table will be skipped
- where: SQL statement to filter the source data to convert
- mapping: defines the mapping instructions for each target field. Here are some examples:
    - writing code directly in the configuration file: `"national_code": {"eval": "data['nationalcode'] if data['nationalcode'] != '' else 'void_unk'"}`
    - calling a function stored in the functions directory: `"name": {"function": "inspire_xx_name"}`
    - assigning a fixed value: `"national_level_code": {"eval": "'void_unk'"}`
    - mapping directly from target field to source field: `"w_national_identifier": "inspireid"`
- geomapping: allows for simple geometric transformations (projection, type casting, etc.)
- fetched_fields: list of fields to load from the source data that are needed for mapping. This information is stored in the Python object `data`. If the source field is mapped field-to-field, it does not need to be included in this list.

> _Note: You can use template parameters (e.g., `${a_parameter}`) that refer to a parameter (`a_parameter`) present in the same file. The template `${a_parameter}` will be resolved when the configuration is loaded by the application, replacing it with the value of the parameter `a_parameter`._

The transformation process takes place in three phases:
1. Extracting the relevant source data into .json files stored in a temporary directory (output/tmp)
2. Creating .sql dump files saved in the output directory
3. Restoring the dump files into the target database

> _Notes:_
> - _The output parameter must be set in the conf.json configuration file_
> - _The output/tmp folder is deleted at the end of the process_

> _Warning: It is important to ensure that the volume containing the output folder has enough space to store the dump files and temporary files, as all these files can be quite large._

## Configuration

Configuration is especially important here because it contains the conversion logic.

Configuration files are located in the [configuration folder](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/conf). You will find:
- the template file [conf.json.template](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/conf/conf.json.template), which must be completed as **conf.json**
- **country-theme.json** configuration files created by the user.
- the file **mapping_conf.json** which allows associating a country with configuration files. You must edit this file accordingly when you create a new country-theme.json file.

Configuration files can be associated with functions which must be stored in the [functions](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions) directory.

## Usage

The tool is used from the command line.

Script options:
* -h, --help: display help
* -v, --verbose: verbose mode
* -s, --no_reset: do not delete existing data before restore
* -c, --conf=FILE: path to JSON configuration file
* -t, --test: test mode (process only 10 objects)
* -n, --no_history: target database without life-cycle management system

<br>

Example on ome2_hvlsp_v4 (without life-cycle management):
~~~
python3 script/transform.py -c path/to/conf.json --no_history
~~~

Example on ome2_hvlsp_v5 (with life-cycle management):
~~~
python3 script/transform.py -c path/to/conf.json
~~~
