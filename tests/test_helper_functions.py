from src.validations import (
    check_root_structure,
    read_statements,
    check_statement_structure,
    read_resources_from_statement,
    check_for_asterisks,
)

# Test check_root_structure function


def test_check_root_structure_valid():
    policy_data = {"PolicyName": "TestPolicy", "PolicyDocument": {}}
    assert check_root_structure(policy_data) is True


def test_check_root_structure_invalid():
    policy_data1 = {"PolicyDocument": {}}
    policy_data2 = {"PolicyName": "TestPolicy"}
    assert check_root_structure(policy_data1) is False
    assert check_root_structure(policy_data2) is False

# Test read_statements function


def test_read_statements_with_single_statement():
    policy_document_data = {"Statement": {"Effect": "Allow"}}
    assert read_statements(policy_document_data) == [{"Effect": "Allow"}]


def test_read_statements_with_multiple_statements():
    policy_document_data = {"Statement": [
        {"Effect": "Allow"}, {"Effect": "Deny"}]}
    assert read_statements(policy_document_data) == [
        {"Effect": "Allow"}, {"Effect": "Deny"}]


def test_read_statements_missing():
    policy_document_data = {}
    assert read_statements(policy_document_data) == []

# Test check_statement_structure function


def test_check_statement_structure_valid():
    statement = {"Effect": "Allow", "Action": "s3:ListBucket",
                 "Resource": "arn:aws:s3:::example_bucket"}
    assert check_statement_structure(statement) is True


def test_check_statement_structure_missing_required_field():
    statement = {"Effect": "Allow", "Resource": "arn:aws:s3:::example_bucket"}
    assert check_statement_structure(statement) is False


def test_check_statement_structure_unexpected_field():
    statement = {"Effect": "Allow", "Action": "s3:ListBucket",
                 "Resource": "arn:aws:s3:::example_bucket", "Unexpected": "Field"}
    assert check_statement_structure(statement) is False

# Test read_resources_from_statement function


def test_read_resources_from_statement_single():
    statement = {"Resource": "arn:aws:s3:::example_bucket"}
    assert read_resources_from_statement(
        statement) == ["arn:aws:s3:::example_bucket"]


def test_read_resources_from_statement_list():
    statement = {"Resource": [
        "arn:aws:s3:::example_bucket", "arn:aws:s3:::another_bucket"]}
    assert read_resources_from_statement(
        statement) == ["arn:aws:s3:::example_bucket", "arn:aws:s3:::another_bucket"]

# Test check_for_asterisks function


def test_check_for_asterisks_with_single_asterisk():
    resources = ["*", "arn:aws:s3:::example_bucket"]
    assert check_for_asterisks(resources) is True


def test_check_for_asterisks_with_multiple_singular_asterisks():
    resources = ["*", "arn:aws:s3:::example_bucket", "*"]
    assert check_for_asterisks(resources) is True


def test_check_for_asterisks_with_one_singular_asterisk():
    resources = "*"
    assert check_for_asterisks(resources) is True


def test_check_for_asterisks_with_multiple_asterisk_as_one_resource():
    resources = ["arn:aws:s3:::example_bucket*",
                 "arn:aws:s3:::another_bucket/*", "**", "****"]
    assert check_for_asterisks(resources) is False


def test_check_for_asterisks_without_asterisk():
    resources = ["arn:aws:s3:::example_bucket", "arn:aws:s3:::another_bucket"]
    assert check_for_asterisks(resources) is False
