# AWS IAM Role Policy Validator

This Python script is designed to validate AWS IAM (Identity and Access Management) Role Policy JSON files. It ensures that the policy does not grant overly broad access by checking for the presence of a single asterisk (`*`) in any "Resource" field, which indicates permissions are granted on all resources.

[AWS IAM Role JSON definition and example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)
[Overview of JSON polcies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json)

## Setup

### Prerequisites

- Git (Download and install from [git-scm.com](https://git-scm.com/downloads))
- Python 3.6 or higher (Download from [python.org](https://www.python.org/downloads/))

  It is recommended to use a virtual environment to manage dependencies.

### Cloning the Repository

To get started, first clone the repository to your local machine:

```bash
git clone https://github.com/kapiw04/json-validator.git
cd json-validator
```

## Setup

### Creating a Virtual Environment

To create a virtual environment in your project directory, follow these steps:

```bash
# Create a virtual environment named 'venv'
python -m venv .venv
```

### Activating the Virtual Environment

Activate the virtual environment by running:

- On Windows:

```bash
.\.venv\Scripts\activate
```

- On macOS and Linux:

```bash
source .venv/bin/activate
```

### Installing Dependecies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

## Usage

This script is designed to validate AWS IAM Role Policy files to ensure they do not grant overly broad permissions indicated by a single asterisk (`*`) in the "Resource" field.

### Command Line Syntax

Run the script by passing the path to the JSON policy file you want to validate:

```bash
python main.py <path_to_policy_file>
```

### Parameters

- <path_to_policy_file>: Path to the JSON policy document you wish to validate.

### Examples

To validate a policy file:

```bash
python main.py /path/to/policy.json
```

## Expected Outputs

The script will output one of the following based on the contents of the policy:

- "Policy is valid." - Indicates no single asterisk (\*) in any "Resource" field, suggesting appropriate access levels.
- "Policy is invalid." - Indicates presence of a single asterisk (\*) in any "Resource" field, suggesting overly broad access.
