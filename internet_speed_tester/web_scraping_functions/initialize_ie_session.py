# === Import dependencies ===

# Built-in

import sys

# Custom

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.misc_functions.get_filepath import get_path
from internet_speed_tester.web_scraping_functions.hide_window import hide_ie_window
from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session

# 3rd party

from selenium import webdriver
from selenium.webdriver.ie.options import Options


def start_ie_session(args, log_name, registry):

    # Open IE window & hide it, return browser instance back to pass to other functions

    message = 'Establishing Internet Explorer session...'
    output_progress(args, message, log_name)

    try:

        # Define driver location for Python to use (relative to directory of main.py)

        driver_location = '../config/drivers/IEDriverServer.exe'
        ie_driver = get_path(driver_location)
        
        # Define option specifying Selenium should not require IE to have Protected Mode enabled on all zones within
        # Internet Options/Security, otherwise will crash if run as an exe and this is not set
        
        ie_options = Options()
        ie_options.ignore_protected_mode_settings = True

        # Initializes browser
        
        ie = webdriver.Ie(executable_path=ie_driver, options=ie_options)

        # Hide IE Window, return browser instance
        
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

        end_web_session(args, log_name, 'error', registry, browser_instance)
        

if __name__ == '__main__':

    initialize_ie_session()
