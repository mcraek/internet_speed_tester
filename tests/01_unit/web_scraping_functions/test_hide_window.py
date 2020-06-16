# === Import dependencies ===

# Built--in

import unittest
from unittest.mock import patch

# Custom

from internet_speed_tester.web_scraping_functions.hide_window import hide_ie_window

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"


def test_hide_ie_window():

    # Validate hide_ie_window returns True

    with patch('internet_speed_tester.web_scraping_functions.hide_window.win32gui'):

        check = hide_ie_window(args, log)
        assert check


def test_hide_ie_window_error():

    # Validate hide_ie_window returns False in event of error (program continues)

    with patch('internet_speed_tester.web_scraping_functions.hide_window.win32gui.EnumWindows',
               unittest.mock.MagicMock(side_effect=OSError)):

        check = hide_ie_window(args, log)
        assert not check
