import pytest
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from internet_speed_tester.web_scraping_functions.read_site import \
    check_html_element, wait, convert_speed, get_download_speed, get_upload_speed
from selenium.common.exceptions import NoSuchElementException

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


class TestCheckHtmlElementError(unittest.TestCase):

    # Validate end_web_session called when HTML element is not found with check_html_element
    
    @patch('internet_speed_tester.web_scraping_functions.read_site.end_web_session')
    def test_check_html_element_error(self, mocked_end_web_session):

        with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.webdriver', unittest.mock.MagicMock(side_effect=NoSuchElementException)):

            from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session

            browser_instance = start_ie_session(args, log, mocked_reg_connection)
            element_id = 'element'

            element_exists = check_html_element(args, log, element_id, browser_instance, mocked_reg_connection)

            self.assertTrue(mocked_end_web_session.called)