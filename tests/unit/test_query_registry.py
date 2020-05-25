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


# Mock winreg_ConnectRegistry raising an Error
# Per documentation, it will raise on
# OSError: https://docs.python.org/3/library/winreg.html


def test_connect_registry_error():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.ConnectRegistry', unittest.mock.MagicMock(side_effect=OSError)):

        assert connect_registry({'log': False, 'verbose': False}, 'log') is None
