import pytest
from unittest.mock import patch
from src.main import main, get_policy_data

# Test for get_policy_data function


@patch('builtins.print')
@patch('sys.argv', ['main.py'])
def test_get_policy_data_no_args(mock_print):
    with pytest.raises(SystemExit) as e:
        get_policy_data()
    assert e.type == SystemExit
    assert e.value.code == 1
    mock_print.assert_called_once_with("Usage: main.py <filename>")


@patch('builtins.print')
@patch('sys.argv', ['main.py', 'nonexistent.json'])
def test_get_policy_data_file_not_found(mock_print):
    with pytest.raises(SystemExit) as e:
        get_policy_data()
    assert e.type == SystemExit
    assert e.value.code == 1
    mock_print.assert_called_once_with("File nonexistent.json not found.")


@patch('src.main.load_policy_from_file', return_value={'key': 'value'})
@patch('sys.argv', ['main.py', 'valid.json'])
def test_get_policy_data_valid(mock_load):
    assert get_policy_data() == {'key': 'value'}
    mock_load.assert_called_once_with('valid.json')

# Test for main function


@patch('builtins.print')
@patch('src.main.validate_policy', return_value=True)
@patch('src.main.get_policy_data', return_value={'key': 'value'})
def test_main_valid_policy(mock_print):
    assert main() is True
    mock_print.assert_called_once_with("Policy is valid.")


@patch('builtins.print')
@patch('src.main.validate_policy', return_value=False)
@patch('src.main.get_policy_data', return_value={'key': 'value'})
def test_main_invalid_policy(mock_print):
    assert main() is False
    mock_print.assert_called_once_with("Policy is invalid.")
