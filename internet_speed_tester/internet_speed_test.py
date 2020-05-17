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
    from test_site_connection import test_site_connection

    # === Handle arguments passed to program / set defaults ===

    args = vars(check_arguments(sys.argv[1:]))

    # === Set log file name (output_progress requires this to be
    # set regardless if -v or -l used or not) ===

    log_name = set_logname()

    # === Output welcome messages (requires verbose) ===

    message = '---- Internet Speed Test Checker v. 0.5 ----'
    output_progress(args, message, log_name)

    # === Begin function ===

    # --- Test connection to the fast.com ---

    site = 'fast.com'
    message = '+++ Testing connection to ' + site + ' +++'
    output_progress(args, message, log_name)

    test_site_connection(args, site, log_name)

    message = '++++ Starting speed test ++++'
    output_progress(args, message, log_name)


if __name__ == "__main__":

    internet_speed_tester()
