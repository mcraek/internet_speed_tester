# === Import dependencies ===

# Built-in

import unittest
from unittest.mock import patch

# Custom

from internet_speed_tester.registry_functions.query_registry import connect_registry, check_root_key, check_subkey


def test_connect_registry():

    # Validate connect_registry completes with patched registry connection

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        reg_connection = connect_registry( { 'log': False, 'verbose': False }, 'log' )

        assert reg_connection is not None


def test_connect_registry_error():

    # Patch winreg.ConnectRegistry raising an Error / Validate function completes
    # Per documentation, it will raise an OSError: https://docs.python.org/3/library/winreg.html
    # Other winreg errors pulled from here as well; e.g., OpenKey

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.ConnectRegistry',
               unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        assert reg_connection is None


def test_check_root_key():

    # Validate check_root_key completes with patched registry connection

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        # Set up reg_connection, then pass it to check_root_key
        
        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key({'log': False, 'verbose': False}, 'log', reg_connection)

        assert root_key_exists and root_key is not None


def test_check_root_key_error():

    # Patch winreg.OpenKey raising an error, validate function completes

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.OpenKey',
               unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key({'log': False, 'verbose': False}, 'log', reg_connection)

    assert not root_key_exists and root_key is None


def test_check_subkey_1():

    # Validate check_subkey returns subkey_exists = False, and ie_original_zoom = False

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        root_key_exists = False
        root_key = None

        subkey_exists, ie_original_zoom = check_subkey({'log': False, 'verbose': False}, 'log',
                                                        reg_connection, root_key_exists, root_key)

        assert not subkey_exists and ie_original_zoom is None


def test_check_subkey_2():

    # Validate check_subkey returns subkey_exists and an ie_original_zoom value

    with patch('internet_speed_tester.registry_functions.query_registry.winreg'):

        # Set up check_root_key and use its return values for check_subkey

        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key({'log': False, 'verbose': False}, 'log', reg_connection)

        subkey_exists, ie_original_zoom = check_subkey({'log': False, 'verbose': False}, 'log',
                                                        reg_connection, root_key_exists, root_key)

    assert subkey_exists and ie_original_zoom is not None


def test_check_subkey_error():

    # Validate check_subkey completes with Exception

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.QueryValueEx',
               unittest.mock.MagicMock(side_effect=OSError)):

        reg_connection = connect_registry({'log': False, 'verbose': False}, 'log')

        root_key_exists, root_key = check_root_key({'log': False, 'verbose': False}, 'log', reg_connection)

        subkey_exists, ie_original_zoom = check_subkey({'log': False, 'verbose': False}, 'log',
                                                        reg_connection, root_key_exists, root_key)

    assert not subkey_exists and ie_original_zoom is None
