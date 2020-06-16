# === Import dependencies ===

# Built-in

import unittest
from unittest.mock import patch
from unittest.mock import Mock

# Custom

from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"


def test_start_ie_session():

    # Validate IE session is returned by start_ie_session

    with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.webdriver'):

        reg_info = Mock()

        session = start_ie_session(args, log, reg_info)
        assert session is not None


class TestStartIESessionError(unittest.TestCase):

    # Validate start_ie_session terminates program in event of error

    def test_start_ie_session_error(self):

        with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.get_path',
                   unittest.mock.MagicMock(side_effect=OSError)):

            with self.assertRaises(SystemExit):

                reg_info = Mock()
                start_ie_session(args, log, reg_info)
