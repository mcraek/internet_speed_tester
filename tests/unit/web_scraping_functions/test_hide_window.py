# === Import required functions / libraries ===

# --- Built-in ---

import unittest
from unittest.mock import patch

# --- Built for project ---

from internet_speed_tester.web_scraping_functions.hide_window \
    import hide_ie_window

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"

# Validate hide_ie_window returns True when working


def test_hide_ie_window():

    with patch('internet_speed_tester.web_scraping_functions.hide_window.win32gui'):

        check = hide_ie_window(args, log)
        assert check

# Validate hide_ie_window returns False in event of error (program continues)


def test_hide_ie_window_error():

    with patch('internet_speed_tester.web_scraping_functions.hide_window.win32gui.EnumWindows',
               unittest.mock.MagicMock(side_effect=OSError)):

        check = hide_ie_window(args, log)
        assert not check
