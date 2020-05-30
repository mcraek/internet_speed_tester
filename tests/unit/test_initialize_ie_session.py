# === Import required functions / libraries ===

# --- Built-in ---

import unittest
from unittest.mock import patch

# --- Built for project ---

from internet_speed_tester.web_scraping_functions.initialize_ie_session \
    import start_ie_session

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"


# Validate IE session is returned by start_ie_session

def test_start_ie_session():

    with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.webdriver'):

        session = start_ie_session(args, log)
        assert session is not None


# Validate start_ie_session terminates program in event of error

class TestStartIESessionError(unittest.TestCase):

    def test_start_ie_session_error(self):

        with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.get_path',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                start_ie_session(args, log)
