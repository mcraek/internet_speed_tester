# === Import required functions / libraries ===

# --- Built-in ---

import contextlib
import io

# --- Built for project ---

from internet_speed_tester.misc_functions import print_msg


# Provide test message to print function, validate
# it prints the custom message when called


def test_print_msg():

    test_msg = 'Hello world!'

    # Call print_msg / redirect stdout to a variable

    x = io.StringIO()

    with contextlib.redirect_stdout(x):

        print_msg(test_msg)

    print_msg_output = x.getvalue()

    assert test_msg in print_msg_output
