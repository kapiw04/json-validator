from src.validations import validate_policy
from src.main import load_policy_from_file


def test_valid_policy_multiple_statements():
    assert validate_policy(load_policy_from_file(
        "tests/cases/valid_policy_multiple_statements.json"))


def test_valid_policy_single_statement():
    assert validate_policy(load_policy_from_file(
        "tests/cases/valid_policy_single_statement.json"))


def test_valid_policy_with_asterisks():
    assert validate_policy(load_policy_from_file(
        "tests/cases/valid_policy_with_asterisks.json"))


def test_valid_policy_with_multiple_resources_and_no_asterisks():
    assert validate_policy(load_policy_from_file(
        "tests/cases/valid_policy_with_multiple_resources_and_no_asterisks.json"))


def test_invalid_policy_single_asterisk_in_resource():
    assert not validate_policy(load_policy_from_file(
        "tests/cases/invalid_policy_single_asterisk_in_resource.json"))


def test_invalid_policy_multiple_asterisks_in_resource():
    assert not validate_policy(load_policy_from_file(
        "tests/cases/invalid_policy_multiple_asterisks_in_resource.json"))


def test_invalid_policy_multiple_statements_with_asterisks():
    assert not validate_policy(load_policy_from_file(
        "tests/cases/invalid_policy_multiple_statements_with_asterisks.json"))
