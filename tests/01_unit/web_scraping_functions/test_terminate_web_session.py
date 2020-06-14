# === Import required functions / libraries ===

# --- Built-in ---

import pytest
import unittest
from unittest.mock import patch
from unittest.mock import Mock

# --- Built for project ---

from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session


# Set up mocked browser instance to pass to function

mocked_browser_instance = Mock()

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Set registry option to test graceful / error option functionality
# without calling registry key value restore


class registry_options:

    subkey_set = False


class registry_restore:

    subkey_set = True
    ie_original_zoom = None
    root_key = Mock()


def test_terminate_web_session_graceful():

    # Test graceful option is able to close browser instance w/o raising exception

    try:

        end_web_session(args, log, 'graceful', registry_options, mocked_browser_instance)

    except Exception:

        pytest.fail('end_web_session with graceful option failed to run browser_instance.close()')


def test_terminate_web_session_error():

    # Test error option is able to close browser instance w/o raising exception

    try:

        end_web_session(args, log, 'error', registry_options, mocked_browser_instance)

    except Exception as e:

        pytest.fail('Error running end_web_session with error option. Error message: ' + str(e))


def test_terminate_web_session_error2():

    # Validate error option closes browser
    # The with (SystemExit) is added to avoid PyTest considering
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

        # Test error option exits program

        with self.assertRaises(SystemExit):

            end_web_session(args, log, 'error', registry_options, mocked_browser_instance)

    @patch('internet_speed_tester.web_scraping_functions.terminate_web_session.set_subkey_value')
    def test_terminate_web_session_restore(self, mocked_set_subkey_value):

        # Validate set_subkey_value called when subkey_set for registry is set to True

        end_web_session(args, log, 'graceful', registry_restore, mocked_browser_instance)
        self.assertTrue(mocked_set_subkey_value.called)
