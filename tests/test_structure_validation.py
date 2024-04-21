from src.validations import validate_structure
from src.main import load_policy_from_file


def test_validate_valid_structure_multiple_statements():
    assert validate_structure(load_policy_from_file(
        "tests/cases/valid_policy_multiple_statements.json"))


def test_validate_valid_structure_single_statement():
    assert validate_structure(load_policy_from_file(
        "tests/cases/valid_policy_single_statement.json"))


def test_validate_valid_structure_with_asterisks():
    assert validate_structure(load_policy_from_file(
        "tests/cases/valid_policy_with_asterisks.json"))


def test_validate_invalid_structure_missing_version():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_version.json"))


def test_validate_invalid_structure_missing_statement():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_statement.json"))


def test_validate_invalid_structure_missing_effect():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_effect.json"))


def test_validate_invalid_structure_missing_action():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_action.json"))


def test_validate_invalid_structure_missing_resource():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_resource.json"))


def test_validate_invalid_structure_unexpected_key():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_unexpected_key.json"))


def test_validate_invalid_structure_missing_policy_name():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_policy_name.json"))


def test_validate_invalid_structure_missing_policy_document():
    assert not validate_structure(load_policy_from_file(
        "tests/cases/invalid_policy_structure_missing_policy_document.json"))
