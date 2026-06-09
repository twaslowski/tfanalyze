![Build](https://github.com/twaslowski/tfanalyze/actions/workflows/test.yml/badge.svg)
![Coverage](./test/coverage.svg)

# tfanalyze

tfanalyze is a lightweight command-line utility to summarize the contents of a Terraform plan.
It allows you to quickly see what resources are being created, updated, or destroyed, and what changes are being made to them.

## Installation

You can install this tool using pip:

```bash
pip install tfanalyze
```

You can also install it from source:

```bash
git clone git@github.com:twaslowski/tfanalyze.git
pip install ./tfanalyze/   # global installation
poetry install  # installs in your given poetry virtual environment
```

## Usage

To use the tool, simply run it with the path to the Terraform plan file as an argument:

```
terraform plan -out=plan.tfplan
tfanalyze plan.tfplan
```

This will output a summary of the plan, showing the resources that are being created, updated, or destroyed.
You can list only the resources that would be destroyed by adding the `--destroy-only` flag.

## Development

This is a very minimal tool for now. I will develop it to be useful for me, and I hope that others may find it useful
too. If you would like to develop it further, feel free to fork the repository and submit a pull request.

You can set up the local development environment using [Poetry](https://python-poetry.org/): Simply run `poetry install`.
