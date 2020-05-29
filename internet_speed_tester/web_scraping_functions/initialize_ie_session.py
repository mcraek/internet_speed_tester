# === Import required functions / libraries ===

# --- Built-in ---

# Allows terminating program in event of error
import sys

# --- Built for project ---

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.misc_functions import get_path
from internet_speed_tester.web_scraping_functions.hide_window import hide_window

# 3rd party functions installed to project Python executable

# Allows controlling web browser, same with next two below this
from 		selenium						import	    webdriver   

# Allows ignoring IE Protected Zone settings
from        selenium.webdriver.ie.options   import      Options                     


# Open IE window & hide it, return browser instance 
# back to pass to other functions


def initialize_ie_session():

    message = 'Establishing Internet Explorer session...'
    print(message)

    try:

        ie_driver = get_path('../../config/drivers/IEDriverServer.exe')        # Define driver location for Python to use

        # Define option specifying Selenium should not require IE to have Protected Mode
        # enabled on all zones within Internet Options/Security, otherwise program errors
        # out if run as an exe

        ie_options = Options()
        ie_options.ignore_protected_mode_settings = True
        
        ie = webdriver.Ie(executable_path=ie_driver, options=ie_options)                # Initializes browser

        # Hide IE Window

        hide_window() 
        
        message = 'IE session started\n'
        print(message)

        return ie       # Returns browser object to main program so it can be passed again to this function

    except:
        
        message = 'Error starting Selenium Internet Explorer option. Cannot locate IEDriverServer.exe within ' + ie_driver
        print(message)

        sys.exit()

if __name__ == '__main__':

    initialize_ie_session()