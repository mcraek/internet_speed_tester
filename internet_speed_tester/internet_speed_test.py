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

    # === Handle arguments passed to program / set defaults ===

    print(sys.argv[1:])
    args = vars(check_arguments(sys.argv[1:]))

    # === Set log file name (output_progress requires this to be
    # set regardless if -v or -l used or not) ===

    log_name = set_logname()

    # === Output welcome messages (requires verbose) ===

    message = '---- Internet Speed Test Checker v. 0.5 ----\n'
    output_progress(args, message, log_name)

    message = '\n++++Starting speed test\n++++'
    output_progress(args, message, log_name)


if __name__ == "__main__":

    internet_speed_tester()
