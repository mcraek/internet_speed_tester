# === Import required functions / libraries ===

# --- Built-in ---

# Writes output to text file if --log specified

import os

# --- Functions built for project ---

# Print messages to console with auto time.sleep

from print_msg import print_msg

# === Define function for writing log messages to text
# file in same directory as program ===


def write_log(message, log_name):

    # Check if log file exists already, create it if it doesn't

    log_check = os.path.exists('./' + log_name)

    if not log_check:

        log_file = open(log_name, 'w')
        log_file.close()

    # Append message to log file

    log_file = open(log_name, 'a')
    log_file.write('\n' + message)
    log_file.close()


def output_progress(args, message, log_name):

    # === Receive / handle args passed to this function from
    # the commandline ===

    # If --debug specified, write console output to log file

    if args['log']:

        write_log(message)

    # If --verbose specified, write output to console

    if args['verbose']:

        print_msg(message)
