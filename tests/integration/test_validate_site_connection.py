# === Import required functions / libraries ===

# --- Built-in ---

# Used for generating random string for running ping test to
# non-resolvable hostname

import string
import random

# --- Built for project ---

from internet_speed_tester.site_connection_functions \
    import validate_site_connection

# output_progress({'log': True, 'verbose': False}, 'message', test_log)
#     assert os.path.exists('./' + test_log)

# Define site for performing connection test
# Program functionality depends on fast.com so this is used for testing

site = 'fast.com'

# Define fake hostname for running ping test to, for checking program
# response when site is down


def generate_string(size=20, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for x in range(size))


# Generate random hostname to ping

test_site = generate_string()

# Validate ping is callable


def test_validate_site_connection():

    # --- Validate ping is callable and returns True for a site reached ---

    # Was receiving "module object is not callable" error when
    # attempting to run pytest until the function call was changed
    # to validate_site_connection.validate_site_connection

    status, ping_results = validate_site_connection(
        {'log': False, 'verbose': False}, site, 'log_name')

    assert status

    # Validate ping stdout captured

    assert 'Reply' in ping_results


def test_site_down_response():

    # --- Validate connection_successful set to
    # False if site is not reachable ---

    # Run ping test to random site, validate
    # status of site set to False

    status, ping_results = validate_site_connection(
        {'log': False, 'verbose': False}, test_site, 'log_name')

    assert not status
