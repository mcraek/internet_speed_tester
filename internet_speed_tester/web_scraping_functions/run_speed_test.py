# === Import dependencies ===

# Custom

from internet_speed_tester.web_scraping_functions.initialize_ie_session import start_ie_session
from internet_speed_tester.web_scraping_functions.navigate_to_site import go_to_site
from internet_speed_tester.web_scraping_functions.read_site import wait
from internet_speed_tester.web_scraping_functions.read_site import get_download_speed
from internet_speed_tester.web_scraping_functions.read_site import get_upload_speed


def build_class(a, b, c):

    # Returns browser instance, and speed test results

    class SpeedTestResults:

        pass

    results = SpeedTestResults()

    results.session = a
    results.download_speed = b
    results.upload_speed = c

    return results


def run_speed_test(args, log_name, registry):

    # Initializes IE browser, navigates to fast.com, runs speed test and returns results

    # Start IE Browser

    session, window_hidden = start_ie_session(args, log_name, registry)

    # Navigate to fast.com

    site = 'fast.com'
    go_to_site(args, log_name, registry, session, site)

    # Wait for site to finish loading

    wait(args, log_name, session, registry)

    # Start speed test, get download speed

    download_speed = get_download_speed(args, log_name, session, registry)

    # Get upload speed

    upload_speed = get_upload_speed(args, log_name, session, registry)

    # Return class containing speed test results

    results = build_class(session, download_speed, upload_speed)

    return results


if __name__ == '__main__':

    run_speed_test()
