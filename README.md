![Build](https://github.com/twaslowski/tfanalyze/actions/workflows/test.yml/badge.svg)
![Coverage](./test/coverage.svg)
![GitHub Release](https://img.shields.io/github/v/release/twaslowski/tfanalyze)

# tfanalyze

Do you ever look at a Terraform plan with 15 deletions and 43 updates and wonder how you're
supposed to safely perform an apply? Fear not! `tfanalyze` has your back.

tfanalyze is a lightweight command-line utility to summarize the contents of a Terraform plan.
It allows you to quickly see what resources are being created, updated, or destroyed, and what changes are being made to
them.

```shell
$ terraform plan -out plan.tfplan
$ tfanalyze plan.tfplan
  DESTROY grafana_data_source.grafana_amazon_prometheus_datasource
  DESTROY grafana_data_source.loki["team-a"]
  DESTROY grafana_data_source.loki["team-b"]
  DESTROY grafana_data_source.loki_admin
  DESTROY grafana_data_source_permission.loki_admin_logs_read
  DESTROY grafana_data_source_permission.loki_team_logs_read["team-a"]
  DESTROY grafana_data_source_permission.loki_team_logs_read["team-b"]
  UPDATE grafana_folder.infrastructure
    title: infrastructure -> infra
```

## Installation

uv (recommended):

```shell
uv tool install tfanalyze
```

pipx:

```bash
pipx install tfanalyze
```

pip (not recommended for a global install):

```shell
pip install tfanalyze
```

## Usage

Supply `tfanalyze` with a single Terraform plan:

```
terraform plan -out=plan.tfplan
tfanalyze plan.tfplan
```

This will output a summary of the plan, showing all resources that are being created, updated, destroyed, read,
or left unchanged (no-op). To narrow down the output, exclude one or more change types with `--exclude`/`-e`
(repeatable):

```shell
# Hide unchanged resources and anything being destroyed
tfanalyze plan.tfplan --exclude noop --exclude destroy
```

Valid values are `create`, `update`, `destroy`, and `noop` (data source reads are reported as `noop`).

If your plan was generated with [OpenTofu](https://opentofu.org/) rather than Terraform, pass the `--tofu` flag
so `tfanalyze` uses the `tofu` binary to read the plan instead of `terraform`.

## Development

Clone the repository and install dependencies with [uv](https://docs.astral.sh/uv/):

```shell
git clone https://github.com/twaslowski/tfanalyze.git
cd tfanalyze
uv sync
```

This installs `tfanalyze` in editable mode alongside its dev dependencies, so you can run it locally
against your changes. Note that `uv run` only works from within the repo (or a subdirectory of it),
since it needs to find the project's `pyproject.toml` to locate its virtual environment:

```shell
cd tfanalyze
uv run tfanalyze plan.tfplan
```

If you want to use your editable build as your regular `tfanalyze` binary from any directory while
developing, install it as a uv tool instead:

```shell
uv tool install --editable .
```

or, with pip:

```shell
pip install -e .
```

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