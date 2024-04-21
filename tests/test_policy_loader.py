from src.utils import load_policy_from_file
import pytest  # type: ignore
import json


def test_can_load_json_file():
    path = "tests/cases/valid_policy_single_statement.json"
    policy = load_policy_from_file(path)
    valid_policy = {
        "PolicyName": "ValidSingleStatement",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": {
                "Sid": "Stmt1",
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::example_bucket"
            }
        }
    }

    assert policy == valid_policy


def test_fail_on_invalid_path():
    path = "invalid_path.json"
    with pytest.raises(FileNotFoundError):
        load_policy_from_file(path)


def test_fail_on_invalid_json():
    path = "tests/cases/invalid_json.json"
    with pytest.raises(json.JSONDecodeError):
        load_policy_from_file(path)
