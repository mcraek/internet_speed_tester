# === Import required functions / libraries ===

# --- Built-in ---

# Allow importing from other directories

import sys

sys.path += ['./misc_functions', './registry_functions',
             './site_connection_functions', './web_scraping_functions']

# --- Built for project ---

# Parse arguments passed from commandline
from check_arguments import check_arguments

# Used with --log option to output verbose output to log file
from set_logname import set_logname

# Verbose output to console / logfile with -v and -l args
from output_progress import output_progress

# Tests connection to fast.com
from validate_site_connection import validate_site_connection

# Sets ZoomFact HKCU reg key for Internet Explorer Zoom
# to 100% (Selenium Requirement)
from config_registry import config_registry


def internet_speed_tester():

    # === Handle arguments passed to program / set defaults ===

    args = vars(check_arguments(sys.argv[1:]))

    # === Set log file name (output_progress requires this to be
    # set regardless if -v or -l used or not) ===

    log_name = set_logname()

    # === Output welcome messages (requires verbose) ===

    message = '---- Internet Speed Test Checker v. 0.5 ----'
    output_progress(args, message, log_name)

    # === Begin function ===

    # --- Test connection to the fast.com, terminate if unsuccessful ---

    site = 'fast.com'
    message = '+++ Testing connection to ' + site + ' +++'
    output_progress(args, message, log_name)

    # Builds class with ping, ping_result, and connection_status attributes
    site_connection = validate_site_connection(args, site, log_name)

    if site_connection.connection_successful:

        message = 'Connection to ' + site + ' successful'
        output_progress(args, message, log_name)

    else:

        message = site + ' appears to be online and reachable\n'
        output_progress(args, message, log_name)
        sys.exit()

    # --- Set IE Zoom Level to 100% (Selenium requirement) ---

    message = '+++ Checking IE Zoom Level is 100% for Selenium +++'
    output_progress(args, message, log_name)

    ie_zoom_changed, ie_original_zoom = config_registry(args, log_name)
    
    # --- Begin speed test ---

    message = '++++ Starting speed test ++++'
    output_progress(args, message, log_name)

    # --- After speed test, restore original IE ZoomFactor value ---

    if ie_zoom_changed:

        message = '+++ Restoring original IE ZoomFactor value'
        output_progress(args, message, log_name)

        






if __name__ == "__main__":

    internet_speed_tester()
