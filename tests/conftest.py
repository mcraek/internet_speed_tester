# === Import required functions / libraries ===

# Built-in

import os
import pytest
import shutil

# 3rd party

import selenium

# Create fixture which sets a temporary working directory for tests / files
# generatedduring testing. After tests are complete, remove the temp directory
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

    driver_path = '../config/drivers/IEDriverServer.exe'

    from selenium import webdriver

    ie_options = Options()
    ie_options.ignore_protected_mode_settings = True

    webdriver = webdriver.Ie(executable_path=driver_path, options=ie_options)

    session = request.node

    for item in session.items:

        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"browser_instance",web_driver)

    yield
    webdriver.close()