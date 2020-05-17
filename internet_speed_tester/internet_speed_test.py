def internet_speed_tester():

    # === Import required functions / libraries ===

    # --- Built-in ---

    import sys

    # --- Functions built for project ---

    # Parse arguments passed from commandline
    from check_arguments import check_arguments

    # Used with --log option to output verbose output to log file
    from set_logname import set_logname

    # Used for verbose output to console / logfile with -v and -l args
    from output_progress import output_progress

    # Used for testing connection to fast.com
    from validate_site_connection import validate_site_connection

    # === Handle arguments passed to program / set defaults ===

    args = vars(check_arguments(sys.argv[1:]))

    # === Set log file name (output_progress requires this to be
    # set regardless if -v or -l used or not) ===

    log_name = set_logname()

    # === Output welcome messages (requires verbose) ===

    message = '---- Internet Speed Test Checker v. 0.5 ----'
    output_progress(args, message, log_name)

    # === Begin function ===

    # --- Test connection to the fast.com, terminate if unsuccessful ---

    site = 'fast.com'
    message = '+++ Testing connection to ' + site + ' +++'
    output_progress(args, message, log_name)

    # Builds class with ping, ping_result, and connection_status attributes
    site_connection = validate_site_connection(args, site, log_name)

    if site_connection.connection_successful:

        message = 'Connection to ' + site + ' successful'
        output_progress(args, message, log_name)

    else:

        message = site + ' appears to be online and reachable\n'
        output_progress(args, message, log_name)
        sys.exit()

    # --- Begin speed test ---

    message = '++++ Starting speed test ++++'
    output_progress(args, message, log_name)


if __name__ == "__main__":

    internet_speed_tester()
