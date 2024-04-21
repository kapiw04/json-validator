# Python script to write the markdown file with test cases as specified

import json
import os


def create_test_cases_md(test_cases_dir, output_file):
    """
    Creates a markdown file with test cases from JSON files in the given directory.

    Args:
    test_cases_dir (str): The directory containing test case JSON files.
    output_file (str): The output markdown file to write the test cases to.
    """
    # Get all the JSON files from the test cases directory
    test_case_files = sorted(
        [f for f in os.listdir(test_cases_dir) if f.endswith('.json')])
    test_case_files.remove('empty.json')
    test_case_files.remove('invalid_json.json')

    # Start the markdown content with a header
    markdown_content = "# Test Cases\n\n"

    # Iterate over the test case files and format the markdown content
    for i, filename in enumerate(test_case_files, start=1):
        # Replace underscores with spaces for the title
        title = filename.replace('_', ' ').replace('.json', '')

        # Read the JSON content from the file
        with open(os.path.join(test_cases_dir, filename), 'r', encoding='utf-8') as file:
            json_content = json.load(file)
            json_formatted = json.dumps(json_content, indent=4)

            # Append the test case to the markdown content
            markdown_content += f"## Test Case {i}: {title}\n```json\n{json_formatted}\n```\n\n"

    # Write the formatted markdown content to the output file
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)


# Specify the test cases directory and output file
cases_dir = 'tests/cases/'
output_md_file = 'TEST_CASES.md'

if __name__ == '__main__':
    # Run the function to create the markdown file
    create_test_cases_md(cases_dir, output_md_file)
