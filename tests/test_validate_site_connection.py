# === Import required functions / libraries ===

# --- Built-in ---

# Used for generating random string for running ping test to
# non-resolvable hostname

import string
import random

# --- Built for project ---

from internet_speed_tester import validate_site_connection


# Validate ping is callable

def test_ping():

    site = 'fast.com'

    # --- Validate ping is callable and returns an exit code of 0 ---

    # Was receiving "module object is not callable" error when
    # attempting to run pytest until the function call was changed
    # to validate_site_connection.validate_site_connection

    ping_test = validate_site_connection.validate_site_connection(
        'args', site, 'log_name')

    assert ping_test.ping.returncode == 0


def test_site_connection_response():

    # --- Validate connection_successful set to
    # False if site is not reachable ---

    # Define function for returning random string

    def generate_string(size=20, chars=string.ascii_uppercase + string.digits):

        return ''.join(random.choice(chars) for x in range(size))

    # Generate random hostname to ping

    test_site = generate_string()

    # Run ping test to random site, validate
    # site_connection attribute set to False

    ping_test = validate_site_connection.validate_site_connection(
        'args', test_site, 'log_name')

    assert not ping_test.connection_successful

    # --- Validate connection to site is successful when the site is up ---

    test_site = 'google.ca'

    # Run ping test to google to validate site_connection
    # attribute returns True

    ping_test = validate_site_connection.validate_site_connection(
        'args', test_site, 'log_name')

    assert ping_test.connection_successful
