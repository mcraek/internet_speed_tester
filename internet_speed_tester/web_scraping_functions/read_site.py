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
from internet_speed_tester.web_scraping_functions import terminate_web_session


def check_html_element(args, log_name, element_id, browser_instance, ie_original_zoom):

    # Confirms HTML element by ID exists on page, terminates program if not found

    try:

        message = 'Checking if HTML element ID ' + element_id + ' still exists...'
        output_progress(args, message, log_name)

        browser_instance.find_element_by_id(element_id)

    except:

        message = 'Unable to find HTML element. Perhaps site HTML coding has changed...'
        output_progress(args, message, log_name)

        terminate_web_session(args, log_name, 'error', ie_original_zoom, browser_instance)


def wait(args, log_name, browser_instance, ie_original_zoom):

    # Waits for 'show-more-details-link' HTML element to confirm page is loaded
    # Times out at 120 seconds

    site_loaded_element_id = 'show-more-details-link'

    # Wait for page to finish loading

    message = 'Waiting for site to fully load...'
    output_progress(args, message, log_name)

    check_html_element(args, log_name, site_loaded_element_id, browser_instance, ie_original_zoom)

    try:

            element = WebDriverWait(browser_instance, 120).until(

                EC.element_to_be_clickable( (By.ID, site_loaded_element_id) )

            )

            message = 'The page has fully loaded\n'
            output_progress(args, message, log_name)

    except Exception as e:

        message = 'Failed to verify site has loaded. Check the ' + site_loaded_element_id \
            + ' HTML element id still becomes clickable when site is fully loaded.' + " Error message: " + str(e)

        output_progress(args, message, log_name)

        terminate_web_session(args, log_name, 'error', ie_original_zoom, browser_instance)