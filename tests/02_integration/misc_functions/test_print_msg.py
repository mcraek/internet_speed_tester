# === Import dependencies ===

# Built-in

import contextlib
import io

# Custom

from internet_speed_tester.misc_functions import print_msg


def test_print_msg():

    # Validate output_progress displays text to console

    test_msg = 'Hello world!'

    # Call print_msg / redirect stdout to a variable

    x = io.StringIO()

    with contextlib.redirect_stdout(x):

        print_msg(test_msg)

    print_msg_output = x.getvalue()

    assert test_msg in print_msg_output
