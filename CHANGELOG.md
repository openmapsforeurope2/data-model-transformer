## [1.1.0] - 2026-09-25
### Added
- Added model transformation configurations for Germany, Denmark, Finland, Spain and Luxembourg.
- Added support for 3D conversion of area features.
- Added generation of parking points from area features.
- Added maritime zone transformation for Finland and Denmark.
- Added support for the `fictitious` attribute in fetched fields.
- Added support for additional hydrographic and transport data transformations.
- Added a developer guide.
- Added support for specifying the target database as a transformation parameter.

### Changed
- Updated model transformation configurations to reflect changes in the OME2 data model.
- Updated the transformation of administrative unit names to include the country.
- Improved name and label generation for several countries, including France, Finland, Spain and Switzerland.
- Improved filtering and handling of unknown values (`-997` and `-998`).
- Updated railway and road transformations to handle changes in source data and OME2 attributes.
- Updated the transformation of hydrographic features, including wetlands, drainage basins and maritime zones.
- Updated Docker configuration and optimized the Docker image.
- Improved command-line error messages.
- Updated the tool for deployment in the IGN-MUT environment.

### Fixed
- Fixed various transformation errors identified during quality controls.
- Fixed geometry type and source table handling for several hydrographic features.
- Fixed handling of null values in boolean fields.
- Fixed incorrect language and script values for INSPIRE names.
- Fixed name ordering and label generation issues for Finnish and Spanish data.
- Fixed railway attributes and track gauge value handling.
- Fixed transformation issues for French, Czech, Swiss and other national datasets.


## [1.0.0] - 2025-03-24
### Added
- Initial release of the project

### Changed
- NTR

### Fixed
- NTR