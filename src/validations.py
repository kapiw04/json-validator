def validate_policy(policy_data: dict) -> bool:
    """
    Validate the policy to ensure no statement's Resource field is just '*'. 

    Args:
        policy_data (dict): policy data json

    Returns:
        bool: False if any of the statement's Resource field is just '*'. True otherwise.
    """
    if validate_structure(policy_data) is False:
        return False

    statements = policy_data.get('PolicyDocument', []).get('Statement', [])
    if isinstance(statements, dict):  # Handle single statement policies
        statements = [statements]

    for statement in statements:
        resource = statement.get('Resource')
        if resource == '*':
            return False
        if isinstance(resource, list) and '*' in resource:
            return False
    return True


def validate_structure(policy_data: dict) -> bool:
    """Check if the policy has the correct structure.

    Args:
        policy_data (dict): policy data json

    Returns:
        bool: True if the policy has the correct structure, False otherwise.
    """
    policy_data_required_fields = ['PolicyName', 'PolicyDocument']
    if any(field not in policy_data for field in policy_data_required_fields):
        return False

    policy_document_data = policy_data.get('PolicyDocument', {})
    policy_document_required_fields = ['Version', 'Statement']
    # Assuming Resource is required in each statement.
    # Documentation says it's required in some cases and given the context of the task it seems to be a required field.
    statement_required_fields = ['Effect', 'Action', 'Resource']
    statement_optional_fields = ['Sid', 'Condition', 'Principal']

    if any(field not in policy_document_data for field in policy_document_required_fields):
        return False

    statements = policy_document_data.get('Statement', [])
    if isinstance(statements, dict):
        statements = [statements]

    for statement in statements:
        if any(field not in statement for field in statement_required_fields):
            return False
        statement_keys = statement.keys()
        if any(key not in statement_required_fields + statement_optional_fields for key in statement_keys):
            return False

    return True
