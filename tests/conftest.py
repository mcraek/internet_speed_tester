# === Import dependencies ===

# Built-in

import os
import pytest
import shutil


@pytest.fixture
def temp_dir(tmpdir):

    # Create fixture which sets a temporary working directory for tests / files
    # generated during testing. After tests are complete, remove the temp directory
    # To see the path of the tempdir:
    # add a print('tempdir located at: ' + str(tempdir)) below, and run pytest -s

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


def browser(request, navigate_to_site=False):

    # Define function for use in start_browser fixtures below
    # There are multiple fixtures created for starting the web browser
    # because when a fixture is called under a session scope, it can only
    # be called once per pytest session. A session scope is utilized as that 
    # provides access to .items which allows calling the web browser via 
    # self.driver and the registry via self.reg_info within a test.
    # These were created for three separate browser instances to be used during
    # test_read_site and test_terminate_web_session integration tests

    from selenium import webdriver
    from internet_speed_tester.registry_functions.config_registry import config_registry
    from selenium.webdriver.ie.options import Options

    # Define argugments to pass to config_registry and terminate_web_session

    args = {'log': False, 'verbose': False}
    log = "log"

    # Ensure IE ZoomFactor is set to 100% (Selenium requirement)

    reg_info = config_registry(args, log)

    # Define location, relative to tests directory to IE driver

    driver_location = '../config/drivers/IEDriverServer.exe'

    # Start Selenium Session, navigate to fast.com if testing site functionality

    options = Options()
    options.ignore_protected_mode_settings = True    

    driver = webdriver.Ie(executable_path=driver_location, ie_options=options)

    if navigate_to_site:

        driver.get('http://www.fast.com')

    session = request.node

    for item in session.items:

        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        setattr(cls.obj, "reg_info", reg_info)

    return driver, reg_info


@pytest.fixture(scope="session")
def start_browser(request):

    # Used during test_navigate_to_site integration test
    # Starts IE browser session, navigates to fast.com and uses end_web_session
    # when testing is finished to close the IE browser

    from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session

    # Define argugments to pass to config_registry and terminate_web_session

    args = {'log': False, 'verbose': False}
    log = "log"

    # Create fixture to start Selenium Test Instance
    # Referenced from: https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-with-pytest

    driver, reg_info = browser(request, navigate_to_site=True)

    # Once test is complete, restore IE ZoomFactor, Terminate IE Browser

    yield

    end_web_session(args, log, 'graceful', reg_info, driver)


# Create fixture to start Selenium Test Instance for terminate_web_session, w/ graceful option

@pytest.fixture(scope="session")
def start_browser_graceful(request):

    # Used during test_terminate_web_session integration test for graceful option

    driver, reg_info = browser(request)


# Create fixture to start Selenium Test Instance for terminate_web_session, w/ error option

@pytest.fixture(scope="session")
def start_browser_error(request):

        # Used during test_terminate_web_session integration test for error option

    driver, reg_info = browser(request)
