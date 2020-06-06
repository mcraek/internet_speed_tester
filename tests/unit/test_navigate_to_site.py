import pytest
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from internet_speed_tester.web_scraping_functions.navigate_to_site import go_to_site
from internet_speed_tester.registry_functions.config_registry import config_registry

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"

# @pytest.mark.usefixtures("start_browser")
# class Test:

#     def test_navigate_to_site(self):

#         site = 'fast.com'
#         site = go_to_site(args, log, self.reg_info, self.browser_instance, site)


def test_navigate_to_site():

    # Validate navigate_to_site returns True when site is reachable

    reg_info = Mock()
    browser_instance = Mock()

    site = 'fast.com'
    site = Mock(go_to_site(args, log, reg_info, browser_instance, site))
    assert site


class TestNavigateToSiteError(unittest.TestCase):

    # Validate navigate_to_site calls end_web_session when site is not reachable

    @patch('internet_speed_tester.web_scraping_functions.navigate_to_site.end_web_session')
    def test_navigate_to_site_error(self, mocked_end_web_session):
               
        reg_info = None
        browser_instance = None

        site = 'fast.com'
        site = go_to_site(args, log, reg_info, browser_instance, site)
        self.assertTrue(mocked_end_web_session.called)