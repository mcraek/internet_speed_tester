# === Import required functions / libraries ===

# Built-in

import os
import pytest
import shutil
from unittest.mock import patch
from unittest.mock import Mock

# 3rd party

import selenium

# Create fixture which sets a temporary working directory for tests / files
# generated during testing. After tests are complete, remove the temp directory
# To see the path of the tempdir:
# add a print('tempdir located at: ' + str(tempdir)) below, and run pytest -s


@pytest.fixture
def temp_dir(tmpdir):

    # Create the temporary directory
    tempdir = tmpdir.mkdir("internet_speed_tester_workingdir")

    # Store current directory to return to after test
    original_wd = os.getcwd()

    # Change to temporary directory
    os.chdir(tempdir)

    # After tests are complete, return to original working_dir
    # and remove the temp directory

    yield temp_dir
    os.chdir(original_wd)
    shutil.rmtree(str(tempdir))


# Create fixture to start Selenium Test Instance

@pytest.fixture(scope="session")
def start_browser(request):

    from selenium import webdriver
    from selenium.webdriver.ie.options import Options
    from internet_speed_tester.registry_functions.config_registry import config_registry
    from internet_speed_tester.web_scraping_functions.terminate_web_session import terminate_web_session
    from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session

    # Define argugments to pass to config_registry and terminate_web_session

    args = {'log': False, 'verbose': False}
    log = "log"

    # Ensure IE ZoomFactor is set to 100% (Selenium requirement)

    reg_info = config_registry(args, log)

    # Start Selenium Session

    with patch('internet_speed_tester.web_scraping_functions.initialize_ie_session.start_ie_session', 'ie_driver', '../../config/drivers/IEDriverServer.exe'):

        browser_instance, window_hidden = start_ie_session(args, log, reg_info.ie_original_zoom)

    return browser_instance

    # Once test is complete, restore IE ZoomFactor, Terminate IE Browser

    yield

    terminate_web_session(args, log, 'graceful', reg_info, browser_instance)