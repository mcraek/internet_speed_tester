# === Import dependencies ===

# Built-in

import unittest
from unittest.mock import patch, Mock

# Custom

from internet_speed_tester.web_scraping_functions.read_site import check_html_element, wait, \
    convert_speed, get_download_speed, get_upload_speed

# 3rd party

from selenium.common.exceptions import TimeoutException

# Setup mocked registry connection & browser instance

mocked_reg_connection = Mock()
mocked_browser = Mock()

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"


def test_check_html_element():

    # Validate function completes when HTML element exists and is found

    element_id = 'element'
    element_exists = check_html_element(args, log, element_id, mocked_browser, mocked_reg_connection)
    assert element_exists


def test_wait():

    # Validate wait returns True when site has finished loading

    with patch('internet_speed_tester.web_scraping_functions.read_site.webdriver'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.check_html_element'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.WebDriverWait'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.EC'):

        site_loaded = wait(args, log, mocked_browser, mocked_reg_connection)

        assert site_loaded


class TestWaitError(unittest.TestCase):

    # Validate end_web_session called when Wait results in a timeout meaning HTML element
    # used to confirm site is loaded is not found
    # https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

    @patch('internet_speed_tester.web_scraping_functions.read_site.end_web_session')
    def test_wait_error(self, mocked_end_web_session):

        with patch('internet_speed_tester.web_scraping_functions.read_site.WebDriverWait',
                   unittest.mock.MagicMock(side_effect=TimeoutException)):

            wait(args, log, mocked_browser, mocked_reg_connection)

            self.assertTrue(mocked_end_web_session.called)


def test_convert_speed():

    # Validate convert_speed returns an expected value

    test_speed = 8
    converted_speed = convert_speed(test_speed)

    assert converted_speed == 1


def test_get_download_speed():

    # Validate download speed is returned

    with patch('internet_speed_tester.web_scraping_functions.read_site.check_html_element'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.convert_speed'):

        download_speed = get_download_speed(args, log, mocked_browser, mocked_reg_connection)

        assert download_speed


def test_get_upload_speed():

    # Validate upload speed is returned

    with patch('internet_speed_tester.web_scraping_functions.read_site.element_has_css_class'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.check_html_element'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.WebDriverWait'), \
               patch('internet_speed_tester.web_scraping_functions.read_site.convert_speed'):

        upload_speed = get_upload_speed(args, log, mocked_browser, mocked_reg_connection)

        assert upload_speed


class TestWaitError2(unittest.TestCase):

    # Validate end_web_session called when Wait results in a timeout meaning HTML element
    # used to confirm site is loaded is not found
    # https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

    @patch('internet_speed_tester.web_scraping_functions.read_site.end_web_session')
    def test_wait_error2(self, mocked_end_web_session):

        with patch('internet_speed_tester.web_scraping_functions.read_site.WebDriverWait',
                   unittest.mock.MagicMock(side_effect=TimeoutException)):

            wait(args, log, mocked_browser, mocked_reg_connection)

            self.assertTrue(mocked_end_web_session.called)
