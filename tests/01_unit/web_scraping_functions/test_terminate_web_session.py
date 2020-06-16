# === Import dependencies ===

# Built-in

import pytest
import unittest
from unittest.mock import patch, Mock

# Custom

from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session

# Set up mocked browser instance to pass to function

mocked_browser_instance = Mock()

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"


class registry_options:

    # Set registry parameter to test graceful / error option functionality
    # of end_web_session without calling registry key value restore

    subkey_set = False


class registry_restore:

    # Set registry parameter to use restore option of end_web_session 

    subkey_set = True
    ie_original_zoom = None
    root_key = Mock()


def test_terminate_web_session_graceful():

    # Validate graceful option is able to close browser instance w/o raising exception

    try:

        end_web_session(args, log, 'graceful', registry_options, mocked_browser_instance)

    except Exception:

        pytest.fail('end_web_session with graceful option failed to run browser_instance.close()')


def test_terminate_web_session_error():

    # Validate error option closes browser the with (SystemExit) is added to avoid PyTest considering
    # the sys.exit called by the function being an error

    with pytest.raises(SystemExit):

        try:

            end_web_session(args, log, 'error', registry_options, mocked_browser_instance)
            session_terminated = True

        except Exception as e:

            session_terminated = False
            print('Error running end_web_session with error option. Error message: ' + str(e))

        assert session_terminated


class TestTerminateWebSessionRestore(unittest.TestCase):

    def test_terminate_web_session_error_exit(self):

        # Validate error option calls end_web_session

        with self.assertRaises(SystemExit):

            end_web_session(args, log, 'error', registry_options, mocked_browser_instance)

    @patch('internet_speed_tester.web_scraping_functions.terminate_web_session.set_subkey_value')
    def test_terminate_web_session_restore(self, mocked_set_subkey_value):

        # Validate set_subkey_value is called when subkey_set for registry is set to True

        end_web_session(args, log, 'graceful', registry_restore, mocked_browser_instance)
        self.assertTrue(mocked_set_subkey_value.called)
