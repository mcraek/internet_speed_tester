# === Import required functions / libraries ===

# --- Built-in ---

import unittest
from unittest.mock import patch

# --- Built for project ---

from internet_speed_tester.registry_functions.query_registry \
    import connect_registry, check_root_key, check_subkey

# Mock working connection to registry


def test_connect_registry():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        assert reg_connection is not None


# Mock winreg.ConnectRegistry raising an Error
# Per documentation, it will raise on
# OSError: https://docs.python.org/3/library/winreg.html
# Other winreg errors pulled from here as well; e.g., OpenKey


def test_connect_registry_error():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.ConnectRegistry', unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        assert reg_connection is None


# Functioning check_root_key

def test_check_root_key():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        # First need to mock reg_connection, then pass it to check_root_key
        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key(
            {'log': False, 'verbose': False}, 'log', reg_connection)

        assert root_key_exists and root_key is not None


# Mock winreg.OpenKey raising an error

def test_check_root_key_error():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.OpenKey', unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key(
            {'log': False, 'verbose': False}, 'log', reg_connection)

    assert not root_key_exists and root_key is None


# Functioning check_subkey, validate it returns
# subkey_exists = False, and ie_original_zoom = False


def test_check_subkey_1():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        root_key_exists = False
        root_key = None

        subkey_exists, ie_original_zoom = check_subkey(
            {'log': False, 'verbose': False}, 'log',
            reg_connection, root_key_exists, root_key)

        assert not subkey_exists and ie_original_zoom is None


# Functioning check_subkey, validate it returns subkey_exists
# and an ie_original_zoom value


def test_check_subkey_2():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        # Mock working check_root_key and use its return
        # values for check_subkey

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key(
            {'log': False, 'verbose': False}, 'log', reg_connection)

        subkey_exists, ie_original_zoom = check_subkey(
            {'log': False, 'verbose': False}, 'log',
            reg_connection, root_key_exists, root_key)

    assert subkey_exists and ie_original_zoom is not None


# Mock winreg.QueryValueEx raising an error

def test_check_subkey_error():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.QueryValueEx', unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry(
            {'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key(
            {'log': False, 'verbose': False}, 'log', reg_connection)

        subkey_exists, ie_original_zoom = check_subkey(
            {'log': False, 'verbose': False}, 'log',
            reg_connection, root_key_exists, root_key)

    assert not subkey_exists and ie_original_zoom is None
