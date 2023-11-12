# datalad-schema

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
