# === Import dependencies ===

# Built-in

import unittest
from unittest.mock import patch

# Custom

from internet_speed_tester.misc_functions.get_filepath import get_path


def test_get_path():

    # Validate get_path returns filepath to IEDriverServer when run as exe

    driver_location = '../config/drivers/IEDriverServer.exe'
    ie_driver = get_path(driver_location)
    assert 'drivers/IEDriverServer.exe' in ie_driver


def test_get_path_error():

    # Validate get_path returns filepath to IEDriverServer when not run as exe

    with patch('internet_speed_tester.misc_functions.get_filepath.sys',
               unittest.mock.MagicMock(side_effect=OSError)):

        driver_location = '../config/drivers/IEDriverServer.exe'
        ie_driver = get_path(driver_location)
        assert 'drivers/IEDriverServer.exe' in ie_driver
