# IAM Policy Validator Test Cases

This document provides a series of test cases to be used for validating an IAM policy validator tool. Each test case includes a JSON object representing an AWS IAM policy, designed to verify that the tool correctly identifies both valid and invalid `Resource` specifications within policy statements.

## Test Case 1: Valid Policy with Multiple Statements

```json
{
  "PolicyName": "ValidMultipleStatements",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "Stmt1",
        "Effect": "Allow",
        "Action": ["s3:ListBucket"],
        "Resource": "arn:aws:s3:::example_bucket"
      },
      {
        "Sid": "Stmt2",
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::example_bucket/*"
      }
    ]
  }
}
```

Test Case 2: Invalid Policy with Single Asterisk Resource

```json
{
  "PolicyName": "InvalidResourceWildcard",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "Stmt1",
        "Effect": "Allow",
        "Action": ["s3:ListAllMyBuckets"],
        "Resource": "*"
      }
    ]
  }
}
```

Test Case 3: Valid Policy with Conditional Statement

```json
{
  "PolicyName": "ValidConditional",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "ConditionalAccess",
        "Effect": "Allow",
        "Action": ["ec2:StartInstances", "ec2:StopInstances"],
        "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*",
        "Condition": {
          "StringEquals": { "ec2:ResourceTag/Department": "Sales" }
        }
      }
    ]
  }
}
```

Test Case 4: Policy with Missing Version Field

```json
{
  "PolicyName": "MissingVersion",
  "PolicyDocument": {
    "Statement": [
      {
        "Sid": "NoVersion",
        "Effect": "Allow",
        "Action": ["s3:ListBucket"],
        "Resource": "arn:aws:s3:::some-bucket"
      }
    ]
  }
}
```

Test Case 5: Policy with Missing Statement Field

```json
{
  "PolicyName": "MissingStatement",
  "PolicyDocument": {
    "Version": "2012-10-17"
    // Note: Statement field is missing
  }
}
```
