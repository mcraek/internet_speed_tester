# === Import required functions / libraries ===

# --- Built-in ---

import pytest
import unittest
from unittest.mock import patch
from unittest.mock import Mock

# --- Built for project ---

from internet_speed_tester.registry_functions.set_registry \
    import connect_key, create_root_key, create_subkey, \
        set_subkey_value

from internet_speed_tester.registry_functions.query_registry \
    import check_root_key


# Set up mocks to pass to set_registry functions

mocked_root_key = Mock(check_root_key)

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Test working connect_key

def test_connect_key():

    with patch('internet_speed_tester.registry_functions.query_registry.winreg.OpenKey'):

        ie_zoom_key_access = connect_key(args, log, mocked_root_key)

        assert ie_zoom_key_access is not None


# Test connect_key error functionality

# Created class for catching sys.exit() call

class TestConnectKeyError(unittest.TestCase):

    def test_connect_key_error(self):

        with patch('internet_speed_tester.registry_functions.query_registry.winreg.OpenKey', unittest.mock.MagicMock(side_effect=OSError)):
            
            with self.assertRaises(SystemExit):

                connect_key(args, log, mocked_root_key)
