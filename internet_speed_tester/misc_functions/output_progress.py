# === Import dependencies ===

# Built-in

import os

# Custom

from internet_speed_tester.misc_functions import print_msg


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

    # Receive / handle args passed to this function from the commandline

    # If --debug specified, write console output to log file

    if args['log']:

        write_log(message, log_name)

    # If --verbose specified, write output to console

    if args['verbose']:

        print_msg(message)
