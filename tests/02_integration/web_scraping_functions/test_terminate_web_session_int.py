# === Import dependencies ===

# Built-in

import pytest
from unittest.mock import Mock

# Custom

from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session

# Setup mocked registry connection and browser instance

mocked_reg_connection = Mock()
mocked_browser_instance = Mock()

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"


class registry_options:

    # Set registry option to test graceful / error option functionality
    # without calling registry key value restore

    subkey_set = False


class registry_restore:

    # Set registry parameter to use restore option of end_web_session
    # Set ie_original_zoom to None so as not to adjust value during test

    subkey_set = True
    ie_original_zoom = None
    root_key = Mock()


@pytest.mark.usefixtures("start_browser_graceful")
class TestTerminateWebSessionGraceful:

    def test_terminate_web_session_graceful(self):

        # Validate graceful option closes the browser

        try:

            end_web_session(args, log, 'graceful', registry_options, self.driver)
            session_terminated = True

        except Exception as e:

            session_terminated = False
            print('Error running end_web_session with graceful option. Error message: ' + str(e))

        assert session_terminated


@pytest.mark.usefixtures("start_browser_error")
class TestTerminateWebSessionErrorAndRestore:

    def test_terminate_web_session_error(self):

        # Validate error option completes

        # Error option closes the browser
        # The with (SystemExit) is added to avoid PyTest considering
        # the sys.exit called by the function being an error

        with pytest.raises(SystemExit):

            try:

                end_web_session(args, log, 'error', registry_options, self.driver)
                session_terminated = True

            except Exception as e:

                session_terminated = False
                print('Error running end_web_session with error option. Error message: ' + str(e))

            assert session_terminated

    def test_terminate_web_session_restore_key(self):

        # Validate restore IE ZoomFactor works

        # Test terminate_web_session is able to restore original registry setting for IE ZoomFactor
        # Added this to the same class as the error test as this will cause the other tests
        # above to fail if on its own.

        try:

            end_web_session(args, log, 'graceful', registry_restore, mocked_browser_instance)

        except Exception:

            pytest.fail('end_web_session failed to restore original IE ZoomFactor value')
