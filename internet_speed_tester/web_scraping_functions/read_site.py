# ============================== Import Dependencies ============================== #

# Built-in functions

import sys
from decimal import Decimal
import time

# 3rd party functions installed to project Python executable

from pynput.keyboard import Key, Controller

from selenium import webdriver
from selenium.webdriver.common.by import By      
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.options import Options

# Built for project

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session


def check_html_element(args, log_name, element_id, browser_instance, registry):

    # Confirms HTML element by ID exists on page, terminates program if not found

    try:

        message = 'Checking if HTML element ID ' + element_id + ' still exists...'
        output_progress(args, message, log_name)

        browser_instance.find_element_by_id(element_id)

        return True

    except:

        message = 'Unable to find HTML element. Perhaps site HTML coding has changed...'
        output_progress(args, message, log_name)

        end_web_session(args, log_name, 'error', registry, browser_instance)


def wait(args, log_name, browser_instance, registry):

    # Waits for 'show-more-details-link' HTML element to confirm page is loaded
    # Times out at 120 seconds

    site_loaded_element_id = 'show-more-details-link'

    # Wait for page to finish loading

    message = 'Waiting for site to fully load...'
    output_progress(args, message, log_name)

    check_html_element(args, log_name, site_loaded_element_id, browser_instance, registry)

    try:

        element = WebDriverWait(browser_instance, 120).until(

            EC.element_to_be_clickable( (By.ID, site_loaded_element_id) )

        )

        message = 'The page has fully loaded\n'
        output_progress(args, message, log_name)

        return True

    except Exception as e:

        message = 'Failed to verify site has loaded. Check the ' + site_loaded_element_id \
            + ' HTML element id still becomes clickable when site is fully loaded.' + " Error message: " + str(e)

        output_progress(args, message, log_name)

        end_web_session(args, log_name, 'error', registry, browser_instance)


def convert_speed(input_value):

    # Converts mbps to MB/s

    speed_converted = Decimal(input_value) / 8
    speed_converted = round(speed_converted, 2)

    return speed_converted


def get_download_speed(args, log_name, browser_instance, registry):

    # When navigating to site, download speed is automatically calculated
    # Check HTML element used for obtaining speed still exists, then pull value

    message = '++++ Obtaining Download Speed ++++'
    output_progress(args, message, log_name)

    down_html_id = 'speed-value'
    check_html_element(args, log_name, down_html_id, browser_instance, registry)

    down_speed_value = browser_instance.find_element_by_id(down_html_id).text

    message = 'Download speed found!'
    output_progress(args, message, log_name)

    # Convert value to MB / s

    down_speed_converted = convert_speed(down_speed_value)

    return float(down_speed_converted)


class element_has_css_class(object):

    # Define a class used for confirming upload speed test is complete
    # This allows for waiting until an HTML element is decorated with a CSS
    # class after clicking the link to start the speed test
            
    # __init__ must be called to create the object from the passed element and define attributes for it

    def __init__(self, locator, css_class):

        self.locator = locator
        self.css_class = css_class

    # Now that the object is defined, the following finds the HTML element we passed to the class
    # and checks if it has a particular CSS class, otherwise returns false

    def __call__(self, browser_instance):

        element = browser_instance.find_element(*self.locator)   # Finding the referenced element

        if self.css_class in element.get_attribute("class"):

            return element
        
        else:

            return False


def get_upload_speed(args, log_name, browser_instance, registry):

    # Start upload speed test and pull value

    message = '++++ Obtaining Upload Speed ++++'
    output_progress(args, message, log_name)

    # Check HTML link element used for starting upload speed test still exists

    up_link_id = 'show-more-details-link'
    check_html_element(args, log_name, up_link_id, browser_instance, registry)

    # Store text from link. This is used to click the link

    up_link_text = (browser_instance.find_element_by_id(up_link_id)).text

    # Calculate upload speed by clicking link

    try:
        
        message = 'Clicking the ' + up_link_id + 'link to begin upload speed test...'
        output_progress(args, message, log_name)
        
        up_link = browser_instance.find_element_by_link_text(up_link_text)
        up_link.click()
        
    except Exception as e:

        message = 'Failed to start upload test by clicking link with HTML ID: ' + upload_link_id + ' with text contents of: ' \
            + upload_link_text + '. Perhaps something has changed HTML-wise for this' + '\nError message: ' + str(e)
        output_progress(arguments_received, message, log_name)

        end_web_session(args, log_name, 'error', registry, browser_instance)

    # Confirm upload speed has finished calculating before pulling value

    message = 'Waiting for upload speed test to complete...'
    output_progress(args, message, log_name)

    # Upload speed test is complete when the upload-value HTML element has the 
    # extra-measurement-value-container succeeded CSS class applied to it, confirmed
    # by inspecting element in web browser dev mode

    try:

        upload_html_id = 'upload-value'
        check_html_element(args, log_name, upload_html_id, browser_instance, registry)

        # Define parameters which control maximum wait time for CSS class to be applied to element 
        # & which CSS class we are expecting

        css = 'extra-measurement-value-container succeeded'
        wait = WebDriverWait(browser_instance, 120)

        element = wait.until(element_has_css_class((By.ID, upload_html_id), css))

    except Exception as e:

        message = 'Failed to verify upload speed test is complete. Verify the ' \
            + upload_html_id + 'HTML element still has the ' + css + ' CSS class applied once the upload test completes'

        output_progress(args, message, log_name)

        message = '\nError message: ' + str(e)

        end_web_session(args, log_name, 'error', registry, browser_instance)

    # Pull / return upload speed value converted to MB / s

    message = 'Upload speed test complete. Pulling value...'
    output_progress(args, message, log_name)

    up_speed_value = browser_instance.find_element_by_id(upload_html_id).text

    up_speed_converted = convert_speed(up_speed_value)

    return float(up_speed_converted)

