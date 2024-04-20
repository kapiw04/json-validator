import json


class PolicyLoader:
    """Handles loading and parsing of IAM policy JSON files."""

    def __init__(self, file_path):
        """Initialize with the path to the IAM policy JSON file."""
        self.file_path = file_path

    def load_policy(self):
        """Load a JSON file and return its contents as a dictionary.

        Returns:
            dict: The loaded policy document.
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)
