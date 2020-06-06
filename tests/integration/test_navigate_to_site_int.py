import pytest
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session
from internet_speed_tester.web_scraping_functions.navigate_to_site import go_to_site
from internet_speed_tester.registry_functions.config_registry import config_registry
from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session

# Setup arguments to pass to function

args = {'log': False, 'verbose': False}
log = "log"

# Set ZoomFactor to 100% (Selenium Requirement)

reg_info = config_registry(args, log)

# Get browser instance

def test_navigate_to_site():

     # Validate IE session can be started and the browser can navigate to fast.com
     
    browser_instance, window_hidden = start_ie_session(args, log, reg_info.ie_original_zoom)
    site = 'fast.com'
    site_reached = go_to_site(args, log, reg_info.ie_original_zoom, browser_instance, site)
    end_web_session(args, log, 'graceful', reg_info, browser_instance)

    assert site_reached