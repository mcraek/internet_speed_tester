# === Import required functions / libraries ===

# --- Built-in ---

# Allows terminating program in event of error
import sys

# --- Built for project ---

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.web_scraping_functions import terminate_web_session

def go_to_site(args, log_name, registry, browser_instance, site):

    message = '++++ Navigating to ' + site + '... ++++'
    output_progress(args, message, log_name)

    try:

        browser_instance.get('http://www.' + site) # Navigate to the website
        return True
    
    except Exception as e:

        message = 'Unable to navigate to ' + site + 'Error: ' + str(e)
        return False
        terminate_web_session(args, log_name, 'error', registry, browser_instance)
