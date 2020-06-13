# === Import required functions / libraries ===

# Built-in

# Used for creating test log file

import os
import contextlib
import io

# Built for project

from internet_speed_tester.misc_functions import output_progress

# Test writing to an existing log file


def test_write_log(temp_dir):

    # --- Validate write_log creates a log file if it
    # doesn't exist ---

    test_log = 'test_log.txt'

    output_progress({'log': True, 'verbose': False}, 'message', test_log)
    assert os.path.exists('./' + test_log)

    # --- Assert write_log can append to the log file ---

    message = 'append test'
    output_progress({'log': True, 'verbose': False}, message, test_log)
    log = open(test_log, 'r')

    # Read log contents, validate test message
    # appended to it

    log_contents = log.read()
    assert message in log_contents

# Validate output_progres writes message to console with -v arg


def test_verbose_console_output():

    test_msg = 'Hello world!'

    x = io.StringIO()

    with contextlib.redirect_stdout(x):

        output_progress({'log': False, 'verbose': True}, test_msg, 'test_log')

    output = x.getvalue()

    assert test_msg in output
