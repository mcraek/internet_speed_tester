# === Import required functions / libraries ===

# --- Built-in ---

# Passes commandline arguments to argument handler
import sys

# --- Built for project ---

# Parse arguments passed from commandline
from internet_speed_tester.misc_functions import check_arguments

# Used with --log option to output verbose output to log file
from internet_speed_tester.misc_functions import set_logname

# Verbose output to console / logfile with -v and -l args
from internet_speed_tester.misc_functions import output_progress

# Tests connection to fast.com
from internet_speed_tester.site_connection_functions import validate_site_connection

# Sets ZoomFactor HKCU reg key for Internet Explorer Zoom
# to 100% (Selenium Requirement)
from internet_speed_tester.registry_functions import config_registry

# Restores IE ZoomFactor if it was changed
from internet_speed_tester.registry_functions import set_subkey_value

# Runs speed test and returns results using selenium
from internet_speed_tester.web_scraping_functions import run_speed_test

# Terminates IE Browser instance started with Selenium
from internet_speed_tester.web_scraping_functions.terminate_web_session import end_web_session


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
    site_up, ping_results = validate_site_connection(args, site, log_name)

    if site_up:

        message = site + ' appears to be online and reachable'
        output_progress(args, message, log_name)

        message = '==========\n\nPing results: \n' + ping_results + '\n\n=========='
        output_progress(args, message, log_name)

    else:

        message = 'Unable to connect to ' + site
        output_progress(args, message, log_name)

        message = '==========\n\nPing results: ' + ping_results + '\n\n=========='
        output_progress(args, message, log_name)

        sys.exit()

    # --- Set IE Zoom Level to 100% (Selenium requirement) ---

    message = '+++ Checking IE Zoom Level is 100% for Selenium +++'
    output_progress(args, message, log_name)

    registry = config_registry(args, log_name)

    # --- Start Selenium session to fast.com, pull return speed values ---

    message = '++++ Starting speed test ++++'
    output_progress(args, message, log_name)

    results = run_speed_test(args, log_name, registry)

    # Output speed test results

    message = '++++ Speed test complete! Here are the results:  ++++\n\n' \
        + 'Download speed (MB / s): ' + str(results.download_speed) + '\n' \
            +'Upload speed (MB / s): ' + str(results.upload_speed)

    output_progress(args, message, log_name)

    # --- Terminate IE browser instance / restore IE origianl ZoomFactor

    message = '++++ Terminating IE Browser Instance ++++'
    output_progress(args, message, log_name)

    end_web_session(args, log_name, 'graceful', registry, results.session)


if __name__ == "__main__":

    internet_speed_tester()
