# === Import required functions / libraries ===

# --- Built-in ---

import unittest
from unittest.mock import patch
from unittest.mock import Mock

# --- Built for project ---

from internet_speed_tester.registry_functions.set_registry \
    import connect_key, create_root_key, create_subkey, \
    set_subkey_value

from internet_speed_tester.registry_functions.query_registry \
    import check_root_key, connect_registry


# Set up mocks to pass to set_registry functions

mocked_root_key = Mock(check_root_key)
mocked_reg_connection = Mock(connect_registry)

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Test working connect_key


def test_connect_key():

    with patch('internet_speed_tester.registry_functions.set_registry.winreg.OpenKey'):

        ie_zoom_key_access = connect_key(args, log, mocked_root_key)

        assert ie_zoom_key_access is not None


# Test connect_key error functionality

# Created class for catching sys.exit() call

class TestConnectKeyError(unittest.TestCase):

    def test_connect_key_error(self):

        with patch('internet_speed_tester.registry_functions.set_registry.winreg.OpenKey',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                connect_key(args, log, mocked_root_key)


# Test working create_root_key returns False if root key already exists


def test_create_root_key_1():

    root_key_exists = True
    root_key_created = create_root_key(args, log,
                                       root_key_exists, mocked_reg_connection)

    assert not root_key_created

# Test working create_root_key creates the root key if it doesn't exist already


def test_create_root_key_2():

    with patch('internet_speed_tester.registry_functions.set_registry.winreg.CreateKey'):

        root_key_exists = False
        root_key_created = create_root_key(args, log,
                                           root_key_exists,
                                           mocked_reg_connection)

        assert root_key_created

# Test create_root_key exits program in event of an error


class TestCreateRootKeyError(unittest.TestCase):

    def test_create_root_key_error(self):

        with patch('internet_speed_tester.registry_functions.set_registry.winreg.CreateKey',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                root_key_exists = False
                create_root_key(args, log,
                                root_key_exists, mocked_reg_connection)


# Test working create_subkey returns False if root key already exists


def test_create_subkey_1():

    subkey_exists = True

    subkey_created = create_subkey(args, log,
                                   subkey_exists, mocked_root_key)

    assert not subkey_created


# Test working create_subkey returns True / creates subkey if it doesn't exist


def test_create_subkey_2():

    with patch('internet_speed_tester.registry_functions.set_registry.winreg'):

        subkey_exists = False
        subkey_created = create_subkey(args, log,
                                       subkey_exists,
                                       mocked_root_key)
        assert subkey_created


# Test create_subkey exists program in event of an error


class TestCreateSubkeyError(unittest.TestCase):

    def test_subkey_error(self):

        with patch('internet_speed_tester.registry_functions.set_registry.winreg.SetValueEx',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                subkey_exists = False
                create_subkey(args, log, subkey_exists, mocked_root_key)


# Check set_subkey_value returns False if
# ZoomFactor already set to 100% w/ config option


def test_set_subkey_value_1():

    ie_original_zoom = 10000
    option = 'config'

    subkey_set = set_subkey_value(args, log, 1,
                                  ie_original_zoom,
                                  mocked_root_key, option)

    assert not subkey_set


# Check set_subkey_value returns True and sets
# ZoomFactor to 100% if it isn't already w/ config option


def test_set_subkey_value_2():

    ie_original_zoom = 5
    value = 10000
    option = 'config'

    with patch('internet_speed_tester.registry_functions.set_registry.winreg'):

        subkey_set = set_subkey_value(args, log, value,
                                      ie_original_zoom,
                                      mocked_root_key, option)

        assert subkey_set

# Check set_subkey_value returns True and restores original
# ZoomFactor value if restore option used


def test_set_subkey_value_3():

    ie_original_zoom = 5
    option = 'restore'

    with patch('internet_speed_tester.registry_functions.set_registry.winreg'):

        subkey_set = set_subkey_value(args, log, 1,
                                      ie_original_zoom,
                                      mocked_root_key, option)

        assert subkey_set


# Check set_subkey_value terminates program on error w/ config optoin


def test_set_subkey_value_error_1():

    def test_set_subkey_value_error_1(self):

        with patch('internet_speed_tester.registry_functions.set_registry.winreg.SetValueEx',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                ie_original_zoom = 5
                value = 10000
                option = 'config'

                set_subkey_value(args, log, value,
                                 ie_original_zoom,
                                 mocked_root_key, option)


# Check set_subkey_value terminates program on error w/ restore option


def test_set_subkey_value_error_2():

    def test_set_subkey_value_error_2(self):

        with patch('internet_speed_tester.registry_functions.set_registry.winreg.SetValueEx',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                ie_original_zoom = 5
                value = 10000
                option = 'restore'

                set_subkey_value(args, log, value,
                                 ie_original_zoom,
                                 mocked_root_key, option)
