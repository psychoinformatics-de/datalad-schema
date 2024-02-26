
### *[THIS PROJECT HAS BEEN ABANDONED AND IS REPLACED BY https://github.com/psychoinformatics-de/datalad-concepts/]*
---


# datalad-schema

[![deploy-docs](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/deploy-docs.yaml)
[![main](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/main.yaml/badge.svg)](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/main.yaml)
[![pypi-publish](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/pypi-publish.yaml/badge.svg)](https://github.com/psychoinformatics-de/datalad-schema/actions/workflows/pypi-publish.yaml)

DataLad dataset schema

## Website

[https://psychoinformatics-de.github.io/datalad-schema](https://psychoinformatics-de.github.io/datalad-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [datalad_schema](src/datalad_schema)
    * [schema](src/datalad_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/datalad_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
