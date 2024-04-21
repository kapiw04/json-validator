# Test Cases

## Test Case 1: invalid policy multiple asterisks in resource

```json
{
  "PolicyName": "ValidMultipleStatements",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": [
          "*",
          "arn:aws:iam::123456789012:role/*",
          "arn:aws:iam::123456789012:user/*",
          "arn:aws:iam::123456789012:role/role1"
        ]
      }
    ]
  }
}
```

## Test Case 2: invalid policy multiple statements with asterisks

```json
{
  "PolicyName": "ValidMultipleStatements",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": [
          "arn:aws:iam::123456789012:role/*",
          "arn:aws:iam::123456789012:user/*",
          "arn:aws:iam::123456789012:role/role1"
        ]
      },
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": [
          "*",
          "arn:aws:iam::123456789012:role/*",
          "arn:aws:iam::123456789012:user/*",
          "arn:aws:iam::123456789012:role/role1"
        ]
      }
    ]
  }
}
```

## Test Case 3: invalid policy single asterisk in resource

```json
{
  "PolicyName": "ValidMultipleStatements",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": "*"
      }
    ]
  }
}
```

## Test Case 4: invalid policy structure missing action

```json
{
  "PolicyName": "InvalidMissingAction",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Sid": "Stmt1",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::example_bucket"
    }
  }
}
```

## Test Case 5: invalid policy structure missing effect

```json
{
  "PolicyName": "InvalidMissingEffect",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Sid": "Stmt1",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example_bucket"
    }
  }
}
```

## Test Case 6: invalid policy structure missing policy document

```json
{
  "PolicyName": "InvalidMissingPolicyDocument"
}
```

## Test Case 7: invalid policy structure missing policy name

```json
{
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
```

## Test Case 8: invalid policy structure missing resource

```json
{
  "PolicyName": "InvalidMissingResource",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Sid": "Stmt1",
      "Effect": "Allow",
      "Action": "s3:ListBucket"
    }
  }
}
```

## Test Case 9: invalid policy structure missing statement

```json
{
  "PolicyName": "InvalidMissingStatement",
  "PolicyDocument": {
    "Version": "2012-10-17"
  }
}
```

## Test Case 10: invalid policy structure missing version

```json
{
  "PolicyName": "InvalidMissingVersion",
  "PolicyDocument": {
    "Statement": {
      "Sid": "Stmt1",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example_bucket"
    }
  }
}
```

## Test Case 11: invalid policy structure unexpected key

```json
{
  "PolicyName": "InvalidUnexpectedKey",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Sid": "Stmt1",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example_bucket",
      "UnexpectedKey": "UnexpectedValue"
    }
  }
}
```

## Test Case 12: valid policy multiple statements

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
        "Resource": "arn:aws:s3:::example_bucket/all"
      }
    ]
  }
}
```

## Test Case 13: valid policy single statement

```json
{
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
```

## Test Case 14: valid policy with asterisks

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
        "Resource": "arn:aws:s3:::example_bucket/*"
      },
      {
        "Sid": "Stmt2",
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::example_bucket/all/*"
      }
    ]
  }
}
```

## Test Case 15: valid policy with multiple resources and no asterisks

```json
{
  "PolicyName": "ValidMultipleStatements",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": [
          "arn:aws:iam::123456789012:role/*",
          "arn:aws:iam::123456789012:user/*",
          "arn:aws:iam::123456789012:role/role1"
        ]
      }
    ]
  }
}
```

## Test Case 16: invalid json

```json
// {
""
// }
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
```

## Test Case 17: empty

```json

```
