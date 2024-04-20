from policy_loader import PolicyLoader
from policy_validator import PolicyValidator


def main():
    file_path = 'policy.json'  # Adjust the file path as needed
    try:
        loader = PolicyLoader(file_path)
        policy_data = loader.load_policy()

        # Extract just the PolicyDocument for validation
        policy_document = policy_data.get('PolicyDocument')
        if policy_document is None:
            raise ValueError("Missing 'PolicyDocument' in loaded JSON.")

        validator = PolicyValidator(policy_document)
        is_valid = validator.validate_policy()

        print("Policy validation passed." if is_valid else "Policy validation failed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
