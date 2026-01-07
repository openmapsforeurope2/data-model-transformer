# Data Model Transformer – Technical Documentation

## Overview

The **data-model-transformer** aims at converting national data provided by producers for their country to the ECRM (ex-HVLSP) data model, then integrates the converted data into the central ECRM database. The following figure summarizes how the harmonization tool works:

<img width="454" height="221" alt="image" src="https://github.com/user-attachments/assets/3e0d3b91-c02f-4e9a-88be-93b6f3b8a3d0" />

## Key features
### Repository structure
The source code repository contains the following folders:
- config: JSON configuration files used by the tool (see §3.2.2);
- docker: dockerfile and build script for reproducible setup;
- functions: functions implemented to operate some complex transformations (see §3.2.2);
- script: orchestrating script and additional script, which constitute the tool.
Additional files such as README, VERSION, LICENSE, CHANGELOG are also included.

### License
The Harmonization tool is distributed under the MIT license.

### Technical characteristics
The Harmonization tool has been developed with Python 3.11. It uses standard Python libraries to handle PostGIS databases.
The Harmonization tool may be run from Windows or Linux environments.

### Deployment
The Harmonization tool is deployed on a Cloud infrastructure hosted by OVH-Cloud, which is often referred to as the “OME2 production platform”. This infrastructure was set into place and is maintained by IGN-France. Its access is restricted to a list of authorized IP addresses for security reasons.

### Running the tool
The Harmonization tool may be run from the OME2 production platform where a simple Jenkins interface is available to the OME2 producers. The interface enables the producer to specify a number of parameters:
-	The name of the source national database (a PostGIS database stored on the production platform);
-	The source PostGIS schema name in the national database;
-	The target PostGIS schema name in the HVLSP central database;
-	The country code of the country to process;
-	The theme to process (au = Administrative units, tn = Transport network, hy = Hydrography).
<img width="1019" height="642" alt="image" src="https://github.com/user-attachments/assets/2d0a7afe-fe65-4b97-88de-f8a17d977055" />
Once the parameters are filled, the tool can be run by clicking on the “Build” button.

### Demonstration
A video which demonstrates how to use the tool and its results is available via the following [link](https://github.com/openmapsforeurope2/tools_demo/tree/main/D5.1_Harmonization_tool). 

---

## Architecture

### Core Steps

1. **Extract**  
   Relevant source data is extracted into `.json` files stored in a temporary directory (`output/tmp`).

2. **Transform & Dump**  
   SQL dump files are created from the JSON data and saved in the output directory.

3. **Load**  
   The dump files are restored into the target database.

---

## Configuration

- **Configuration Files**:  
  Each country-theme has its own configuration file, which defines:
  - Source/target table mapping.
  - Field-level mapping (direct, expression, or function).
  - Options for mocking, additional filtering, geometric transforms, and field fetching.
- **Function Directory**:  
  For complex field mappings, configuration files can reference reusable Python functions placed in the `functions/` directory.

#### Example mapping types:
- Direct in config:  
  `"national_code": {"eval": "data['nationalcode'] if data['nationalcode'] != '' else 'void_unk'"}`
- Via function:  
  `"name": {"function": "inspire_xx_name"}`
- Fixed value:  
  `"national_level_code": {"eval": "'void_unk'"}`
- Field-to-field:  
  `"w_national_identifier": "inspireid"`

**Template parameters** such as `${a_parameter}` in configs are resolved at load time.

---

## Main Components

### Python Scripts (in `script/`)

- **transform.py**:  
  Orchestrates the process: loads configuration, merges with theme-specific settings, manages output directories, and calls extraction and transformation logic.

- **dump.py**:  
  Converts transformed JSON data to SQL dumps.  
  - Handles mock tables, writes SQL statements, and manages schema.

- **utils.py**:  
  Utility functions for:
  - Loading and templating configuration files.
  - Path management and OS compatibility.
  - Dynamic function loading.

### Function Modules (in `functions/`)

Reusable field-mapping functions, each encapsulated in a separate file (e.g., `es_tn_road_label.py`).  
These accept a `context` dict and return the appropriate transformed value.

**Example:**  
```python
def function_name(context):
    ome2_vial = context['data']['ome2_vial']
    # ... transformation logic ...
    return value
```

---

## Docker Support

A `Dockerfile` is provided for reproducible setup, including:
- Python 3, PostgreSQL client.
- All dependencies installed via `requirements.txt`.
- App runs as non-root user.

---

## Usage

1. Ensure configuration files exist for each country-theme.
2. Set the output directory in `conf.json`.
3. Run the transformation pipeline (typically via `transform.py`).
4. Review and load the generated SQL dump files in your target database.

**Note:**  
- The temporary directory (`output/tmp`) is deleted at the end of the process.
- Ensure sufficient disk space for output and temp files.
- Use the `mock` parameter to skip tables; `where` for filtering; `mapping` for field logic.

---

## Extending

- Add new transformation logic by placing new Python functions in the `functions/` directory.
- Update configuration files to reference new logic as needed.

---

## References

- [README.md](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/README.md)
- [Example functions/](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions)
- [Dockerfile](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/docker/Dockerfile)


---

## Architecture

### Core Steps

1. **Extract**  
   Relevant source data is extracted into `.json` files stored in a temporary directory (`output/tmp`).

2. **Transform & Dump**  
   SQL dump files are created from the JSON data and saved in the output directory.

3. **Load**  
   The dump files are restored into the target database.

---

## Configuration

- **Configuration Files**:  
  Each country-theme has its own configuration file, which defines:
  - Source/target table mapping.
  - Field-level mapping (direct, expression, or function).
  - Options for mocking, additional filtering, geometric transforms, and field fetching.
- **Function Directory**:  
  For complex field mappings, configuration files can reference reusable Python functions placed in the `functions/` directory.

#### Example mapping types:
- Direct in config:  
  `"national_code": {"eval": "data['nationalcode'] if data['nationalcode'] != '' else 'void_unk'"}`
- Via function:  
  `"name": {"function": "inspire_xx_name"}`
- Fixed value:  
  `"national_level_code": {"eval": "'void_unk'"}`
- Field-to-field:  
  `"w_national_identifier": "inspireid"`

**Template parameters** such as `${a_parameter}` in configs are resolved at load time.

---

## Main Components

### Python Scripts (in `script/`)

- **transform.py**:  
  Orchestrates the process: loads configuration, merges with theme-specific settings, manages output directories, and calls extraction and transformation logic.

- **dump.py**:  
  Converts transformed JSON data to SQL dumps.  
  - Handles mock tables, writes SQL statements, and manages schema.

- **utils.py**:  
  Utility functions for:
  - Loading and templating configuration files.
  - Path management and OS compatibility.
  - Dynamic function loading.

### Function Modules (in `functions/`)

Reusable field-mapping functions, each encapsulated in a separate file (e.g., `es_tn_road_label.py`).  
These accept a `context` dict and return the appropriate transformed value.

**Example:**  
```python
def function_name(context):
    ome2_vial = context['data']['ome2_vial']
    # ... transformation logic ...
    return value
```

---

## Docker Support

A `Dockerfile` is provided for reproducible setup, including:
- Python 3, PostgreSQL client.
- All dependencies installed via `requirements.txt`.
- App runs as non-root user.

---

## Usage

1. Ensure configuration files exist for each country-theme.
2. Set the output directory in `conf.json`.
3. Run the transformation pipeline (typically via `transform.py`).
4. Review and load the generated SQL dump files in your target database.

**Note:**  
- The temporary directory (`output/tmp`) is deleted at the end of the process.
- Ensure sufficient disk space for output and temp files.
- Use the `mock` parameter to skip tables; `where` for filtering; `mapping` for field logic.

---

## Extending

- Add new transformation logic by placing new Python functions in the `functions/` directory.
- Update configuration files to reference new logic as needed.

---

## References

- [README.md](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/README.md)
- [Example functions/](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions)
- [Dockerfile](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/docker/Dockerfile)


---

## Architecture

### Core Steps

1. **Extract**  
   Relevant source data is extracted into `.json` files stored in a temporary directory (`output/tmp`).

2. **Transform & Dump**  
   SQL dump files are created from the JSON data and saved in the output directory.

3. **Load**  
   The dump files are restored into the target database.

---

## Configuration

- **Configuration Files**:  
  Each country-theme has its own configuration file, which defines:
  - Source/target table mapping.
  - Field-level mapping (direct, expression, or function).
  - Options for mocking, additional filtering, geometric transforms, and field fetching.
- **Function Directory**:  
  For complex field mappings, configuration files can reference reusable Python functions placed in the `functions/` directory.

#### Example mapping types:
- Direct in config:  
  `"national_code": {"eval": "data['nationalcode'] if data['nationalcode'] != '' else 'void_unk'"}`
- Via function:  
  `"name": {"function": "inspire_xx_name"}`
- Fixed value:  
  `"national_level_code": {"eval": "'void_unk'"}`
- Field-to-field:  
  `"w_national_identifier": "inspireid"`

**Template parameters** such as `${a_parameter}` in configs are resolved at load time.

---

## Main Components

### Python Scripts (in `script/`)

- **transform.py**:  
  Orchestrates the process: loads configuration, merges with theme-specific settings, manages output directories, and calls extraction and transformation logic.

- **dump.py**:  
  Converts transformed JSON data to SQL dumps.  
  - Handles mock tables, writes SQL statements, and manages schema.

- **utils.py**:  
  Utility functions for:
  - Loading and templating configuration files.
  - Path management and OS compatibility.
  - Dynamic function loading.

### Function Modules (in `functions/`)

Reusable field-mapping functions, each encapsulated in a separate file (e.g., `es_tn_road_label.py`).  
These accept a `context` dict and return the appropriate transformed value.

**Example:**  
```python
def function_name(context):
    ome2_vial = context['data']['ome2_vial']
    # ... transformation logic ...
    return value
```

---

## Docker Support

A `Dockerfile` is provided for reproducible setup, including:
- Python 3, PostgreSQL client.
- All dependencies installed via `requirements.txt`.
- App runs as non-root user.

---

## Usage

1. Ensure configuration files exist for each country-theme.
2. Set the output directory in `conf.json`.
3. Run the transformation pipeline (typically via `transform.py`).
4. Review and load the generated SQL dump files in your target database.

**Note:**  
- The temporary directory (`output/tmp`) is deleted at the end of the process.
- Ensure sufficient disk space for output and temp files.
- Use the `mock` parameter to skip tables; `where` for filtering; `mapping` for field logic.

---

## Extending

- Add new transformation logic by placing new Python functions in the `functions/` directory.
- Update configuration files to reference new logic as needed.

---

## References

- [README.md](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/README.md)
- [Example functions/](https://github.com/openmapsforeurope2/data-model-transformer/tree/main/functions)
- [Dockerfile](https://github.com/openmapsforeurope2/data-model-transformer/blob/main/docker/Dockerfile)
