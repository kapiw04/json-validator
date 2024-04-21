from utils import load_policy_from_file
from validations import validate_policy, validate_structure
import sys


def main():
    file_path = sys.argv[1]

    if not file_path:
        raise ValueError("File path is required.")

    try:
        policy_data = load_policy_from_file(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    is_valid_policy = validate_policy(policy_data)

    if is_valid_policy:
        print("Policy is valid.")
    else:
        print("Policy is invalid.")

    return is_valid_policy


if __name__ == '__main__':
    main()
