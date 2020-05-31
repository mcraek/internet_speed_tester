# === Import required functions / libraries ===

# --- Built-in ---

# Allows terminating program in event of error
import sys

# --- Built for project ---

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.misc_functions.get_filepath import get_path
from internet_speed_tester.web_scraping_functions.hide_window import hide_ie_window
from internet_speed_tester.web_scraping_functions.terminate_web_session import terminate_web_session

# 3rd party functions installed to project Python executable

# Allows controlling web browser, same with next two below this
from selenium import webdriver

# Allows ignoring IE Protected Zone settings
from selenium.webdriver.ie.options import Options


# Open IE window & hide it, return browser instance
# back to pass to other functions


def start_ie_session(args, log_name, ie_original_zoom):

    message = 'Establishing Internet Explorer session...'
    output_progress(args, message, log_name)

    try:

        # Define driver location for Python to use
        # (relative to direcotry of main.py)

        driver_location = '../config/drivers/IEDriverServer.exe'
        ie_driver = get_path(driver_location)
        
        # Define option specifying Selenium should not require IE
        # to have Protected Mode enabled on all zones within
        # Internet Options/Security, otherwise program errors
        # out if run as an exe
        ie_options = Options()
        ie_options.ignore_protected_mode_settings = True

        # Initializes browser
        ie = webdriver.Ie(executable_path=ie_driver, options=ie_options)

        # Hide IE Window
        window_hidden = hide_ie_window(args, log_name)

        message = 'IE session started'
        output_progress(args, message, log_name)

        return ie, window_hidden

    except Exception as e:

        message = 'Error starting Selenium Internet Explorer option. ' + \
            'Cannot locate IEDriverServer.exe within ' + driver_location + \
            'Error message: ' + str(e)
        output_progress(args, message, log_name)

        browser_instance = None

        terminate_web_session(args, log_name, 'error', ie_original_zoom, browser_instance)
        


if __name__ == '__main__':

    initialize_ie_session()
