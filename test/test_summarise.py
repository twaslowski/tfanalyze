import pytest

from tfanalyze.change import Change, ChangeAction
from tfanalyze.cli import _summarize


@pytest.fixture()
def changes():
    return [
        Change(
            address="module.foo.aws_instance.bar",
            type="aws_instance",
            name="bar",
            change_action=ChangeAction.CREATE,
            properties_before={},
            properties_after={"ami": "ami-12345678"},
        )
    ]


def test_should_output_one_change(changes, capsys):
    _summarize(changes, set())
    captured = capsys.readouterr()
    assert "CREATE module.foo.aws_instance.bar" in captured.out


def test_should_output_modification_details_on_modified_resource(changes, capsys):
    changes[0].change_action = ChangeAction.UPDATE
    _summarize(changes, set())
    captured = capsys.readouterr()
    assert "ami: None -> ami-12345678" in captured.out


def test_should_exclude_specified_change_type(changes, capsys):
    _summarize(changes, {ChangeAction.CREATE})
    captured = capsys.readouterr()
    assert "aws_instance" not in captured.out


def test_should_exclude_multiple_change_types(changes, capsys):
    changes[0].change_action = ChangeAction.UPDATE
    _summarize(changes, {ChangeAction.CREATE, ChangeAction.UPDATE})
    captured = capsys.readouterr()
    assert "aws_instance" not in captured.out


def test_should_show_all_change_types_by_default(changes, capsys):
    changes[0].change_action = ChangeAction.NOOP
    _summarize(changes, set())
    captured = capsys.readouterr()
    assert "NOOP module.foo.aws_instance.bar" in captured.out


def test_should_render_structured_value_diff_as_block(changes, capsys):
    changes[0].change_action = ChangeAction.UPDATE
    changes[0].properties_before = {"tags": {"env": "staging"}}
    changes[0].properties_after = {"tags": {"env": "staging", "team": "infra"}}
    _summarize(changes, set())
    captured = capsys.readouterr()
    assert '"env": "staging"' in captured.out
    assert '"team": "infra"' in captured.out
