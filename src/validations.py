from typing import List, Dict, Any


def validate_policy(policy_data: Dict[str, Any]) -> bool:
    """
    Validate the policy to ensure no statement's Resource field is just '*'.

    Args:
        policy_data (dict): policy data json

    Returns:
        bool: False if any of the statement's Resource field is just '*'. True otherwise.
    """
    if validate_structure(policy_data) is False:
        return False

    statements: List[Dict[str, Any]] = read_statements(
        policy_data.get('PolicyDocument', {}))

    for statement in statements:
        resources: List[str] = read_resources_from_statement(statement)
        print(resources)
        if check_for_asterisks(resources):
            return False

    return True


def validate_structure(policy_data: Dict[str, Any]) -> bool:
    """Check if the policy has the correct structure.

    Args:
        policy_data (dict): policy data json

    Returns:
        bool: True if the policy has the correct structure, False otherwise.
    """
    if check_root_structure(policy_data) is False:
        return False

    statements: List[Dict[str, Any]] = read_statements(
        policy_data["PolicyDocument"])

    versionMissing: bool = 'Version' not in policy_data["PolicyDocument"]

    if not statements or versionMissing:
        return False

    for statement in statements:
        if check_statement_structure(statement) is False:
            return False

    return True


def check_root_structure(policy_data: Dict[str, Any]) -> bool:
    """Check if the policy has the correct root structure.

    Args:
        policy_data (dict): policy data json

    Returns:
        bool: True if the policy has the correct root structure, False otherwise.
    """
    policy_data_required_fields = ['PolicyName', 'PolicyDocument']
    if any(field not in policy_data for field in policy_data_required_fields):
        return False

    return True


def read_statements(policy_document_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Read the statements from the policy data.

    Args:
        policy_data (dict): policy data json

    Returns:
        list: list of statements
    """
    statements = policy_document_data.get('Statement', [])
    if isinstance(statements, dict):
        statements = [statements]
    return statements


def check_statement_structure(statement: Dict[str, Any]) -> bool:
    """Check if the statement has the correct structure.

    Args:
        statement (dict): statement data json

    Returns:
        bool: True if the statement has the correct structure, False otherwise.
    """
    statement_required_fields = ['Effect', 'Action', 'Resource']
    statement_optional_fields = ['Sid', 'Condition', 'Principal']

    if any(field not in statement for field in statement_required_fields):
        return False

    statement_keys = statement.keys()
    if any(key not in statement_required_fields + statement_optional_fields for key in statement_keys):
        return False

    return True


def read_resources_from_statement(statement: Dict[str, Any]) -> List[str]:
    """Read the resource(s) from the statement.

    Args:
        statement (dict): statement data json

    Returns:
        list: list of resources, which may be empty
    """
    resource = statement.get('Resource', [])
    if isinstance(resource, str):
        return [resource]
    elif isinstance(resource, list):
        return resource
    else:
        return []


def check_for_asterisks(resources: List[str]) -> bool:
    """Check if the resource list contains an asterisk as an entire string.

    Args:
        resources (list): list of resources

    Returns:
        bool: True if any resource is exactly '*', False otherwise.
    """
    return '*' in resources
