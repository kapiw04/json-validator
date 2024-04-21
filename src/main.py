from typing import Any, Dict
from src.validations import validate_policy
import sys
import json


def load_policy_from_file(path: str) -> dict:
    """Load a JSON file and return its contents as a dictionary.

    Args:
        path (str): The path to the JSON file.

    Returns:
        dict: The loaded policy document.
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(path, 'r') as file:
        return json.load(file)


def get_policy_data() -> Dict[str, Any]:
    """Get the policy data from the command line arguments.
    Returns:
        dict: The policy data.
    """

    if len(sys.argv) != 2:
        print("Usage: python main.py <policy_file>")
        sys.exit(1)

    policy_file = sys.argv[1]
    try:
        policy_data = load_policy_from_file(policy_file)
    except FileNotFoundError:
        print(f"File {policy_file} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"File {policy_file} is not a valid JSON.")
        sys.exit(1)

    return policy_data


def main() -> bool:
    policy_data: Dict[str, Any] = get_policy_data()
    is_valid_policy = validate_policy(policy_data)

    if is_valid_policy:
        print("Policy is valid.")
    else:
        print("Policy is invalid.")

    return is_valid_policy


if __name__ == '__main__':
    main()
