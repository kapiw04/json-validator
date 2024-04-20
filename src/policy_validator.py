class PolicyValidator:
    def __init__(self, policy_data: dict):
        """Initialize with the IAM policy data as a dictionary."""
        self.policy_data = policy_data
        if not self.validate_structure():
            raise ValueError("Policy structure validation failed.")

    def validate_policy(self):
        """Validate the policy to ensure no statement's Resource field is just '*'. """
        statements = self.policy_data.get('Statement', [])
        if isinstance(statements, dict):  # Handle single statement policies
            statements = [statements]

        for statement in statements:
            resource = statement.get('Resource')
            if resource == '*':
                return False
            if isinstance(resource, list) and '*' in resource:
                return False
        return True

    def validate_structure(self):
        """Check if the policy has the correct structure."""
        required_fields = ['Version', 'Statement']
        # Assuming Resource is required
        statement_required_fields = ['Effect', 'Action', 'Resource']

        if any(field not in self.policy_data for field in required_fields):
            return False

        statements = self.policy_data.get('Statement', [])
        if isinstance(statements, dict):
            statements = [statements]

        for statement in statements:
            if any(field not in statement for field in statement_required_fields):
                return False
        return True
