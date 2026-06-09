![Build](https://github.com/twaslowski/tfanalyze/actions/workflows/test.yml/badge.svg)
![Coverage](./test/coverage.svg)

# tfanalyze

Do you ever look at a Terraform plan with 15 deletions and 43 updates and wonder how you're
supposed to safely perform an apply? Fear not! `tfanalyze` has your back.

tfanalyze is a lightweight command-line utility to summarize the contents of a Terraform plan.
It allows you to quickly see what resources are being created, updated, or destroyed, and what changes are being made to
them.

## Installation

pip:

```bash
pip install tfanalyze
```

pipx:

```shell
pipx install tfanalyze
```

## Usage

Supply `tfanalyze` with a single Terraform plan:

```
terraform plan -out=plan.tfplan
tfanalyze plan.tfplan
```

This will output a summary of the plan, showing the resources that are being created, updated, or destroyed.
You can list only the resources that would be destroyed by adding the `--destroy-only` flag.

## Development

Lifecycle tasks can be performed using the provided [Taskfile](https://taskfile.dev).
`black`, `isort` and `autoflake` are used to ensure consistent formatting.

Tests exist and can be invoked with pytest. In order to generate a test coverage report, simply
run `task test`.

Additionally, check the `e2e/` directory to validate `tfanalyze` against real Terraform plans.
You can generate plans for different scenarios by using the provided bash script:

```shell
# You'll want to create an initial baseline setup
cd e2e
terraform init

./generate-plans.sh destroy
./generate-plans.sh update
```

A minimal baseline state exists at `e2e/state/e2e.tfstate` which is re-used by all scenarios.