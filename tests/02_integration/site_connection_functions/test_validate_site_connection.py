# === Import dependencies ===

# Built-in

import string
import random

# Custom

from internet_speed_tester.site_connection_functions import validate_site_connection

# Define site for performing connection test
# Program functionality depends on fast.com so this is used for testing

site = 'fast.com'


def generate_string(size=20, chars=string.ascii_uppercase + string.digits):

    # Define fake hostname for running ping test to, for checking program
    # response when site is down. This should result in non-pingable host

    return ''.join(random.choice(chars) for x in range(size))

# Generate random hostname to ping

test_site = generate_string()


def test_validate_site_connection():

    # Validate ping is callable and returns True for a site reached

    status, ping_results = validate_site_connection({'log': False, 'verbose': False}, site, 'log_name')

    assert status

    # Validate ping stdout captured

    assert 'Reply' in ping_results


def test_site_down_response():

    # Validate connection_successful set to False if site is not reachable

    # Run ping test to random hostname, validate status of site set to False

    status, ping_results = validate_site_connection({'log': False, 'verbose': False}, test_site, 'log_name')

    assert not status
