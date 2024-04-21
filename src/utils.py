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
