def internet_speed_tester():

    # === Import required functions / libraries ===

    # Built-in

    from    datetime    import      datetime        # Used for logging current date / time of check
    import                          subprocess      # Used for hiding console for --silent option
    import sys

    # Functions built for project

    from            check_arguments         import      check_arguments             # Parses arguments passed to program from commandline
    from            set_logname             import      set_logname                 # Used with --log option to output verbose output to log file
    from            output_progress         import      output_progress             # Used for verbose output to console / logfile


    # === Handle arguments passed to program / set defaults ===
    
    args = vars(check_arguments(sys.argv[1:]))


    # === Set log file name (verbose option requires this as well) ===

    if (args['log']) or (args['verbose']):

        log_name = set_logname()


    # === Output welcome messages (requires verbose) ===

    output_progress(args, '------------------- Internet Speed Test Checker v. 0.5 -------------------\n', log_name)



    # output_progress(arguments_received, '------------------- Internet Speed Test Checker v. 0.5 -------------------\n', log_name)
    # output_progress(arguments_received, 'Starting speed test timestamped: ' + str(date + '\n'), log_name)

if __name__ == "__main__":

    internet_speed_tester()