from click.testing import CliRunner

from tfanalyze.cli import tfanalyze


def test_load_command_with_nonexistent_file():
    runner = CliRunner()
    result = runner.invoke(tfanalyze, ["nonexistent.tfplan"])
    assert result.exit_code == 1
    assert "File nonexistent.tfplan could not be found." in result.output


def test_load_command_with_invalid_file():
    runner = CliRunner()
    result = runner.invoke(tfanalyze, ["test/resources/invalid_plan.tfplan"])
    assert result.exit_code == 1
    assert "Failed to load Terraform plan" in result.output
