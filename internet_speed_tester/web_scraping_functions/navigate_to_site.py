# === Import dependencies ===

# Built-in

import sys

# Custom

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session


def go_to_site(args, log_name, registry, browser_instance, site):

    # Navigate browser instance to site

    message = '++++ Navigating to ' + site + '... ++++'
    output_progress(args, message, log_name)

    try:

        browser_instance.get('http://www.' + site) # Navigate to the website
        return True
    
    except Exception as e:

        message = 'Unable to navigate to ' + site + 'Error: ' + str(e)
        end_web_session(args, log_name, 'error', registry, browser_instance)
