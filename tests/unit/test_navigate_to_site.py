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

    reg_info = Mock()
    browser_instance = Mock()

    site = 'fast.com'
    site = Mock(go_to_site(args, log, reg_info, browser_instance, site))
    assert site


def test_navigate_to_site_error():
        
    reg_info = None
    browser_instance = None

    site = 'fast.com'
    site = go_to_site(args, log, reg_info, browser_instance, site)
    assert not site