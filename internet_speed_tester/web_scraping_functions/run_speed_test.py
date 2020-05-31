# Import dependencies

from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session
from internet_speed_tester.web_scraping_functions.navigate_to_site import go_to_site
from internet_speed_tester.web_scraping_functions.read_site import wait

# Define function for returning class of info back


def build_class(a):

    class SpeedTestResults:

        pass

    results = SpeedTestResults()

    results.session = a
    # results.error_message = b
    # # reg.ie_original_zoom = b
    # # reg.root_key = c

    return results


def run_speed_test(args, log_name, registry):

    # Start IE Browser

    session, window_hidden = start_ie_session(args, log_name, registry.ie_original_zoom)

    # Navigate to fast.com

    site = 'fast.com'
    go_to_site(args, log_name, registry, session, site)

    # Wait for site to finish loading

    wait(args, log_name, session, registry.ie_original_zoom)

    # Start speed test, get download speed

    

    # Return class containing speed test results

    results = build_class(session)

    return results



if __name__ == '__main__':

    run_speed_test()
