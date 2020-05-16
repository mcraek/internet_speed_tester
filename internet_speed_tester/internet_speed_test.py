def internet_speed_tester():

    # === Import required functions / libraries === #

    # Built-in

    from    datetime    import      datetime        # Used for logging current date / time of check
    import                          subprocess      # Used for hiding console for --silent option
    import sys

    # Functions built for project

    from            check_arguments         import      check_arguments             # Parses arguments passed to program from commandline
    from            set_logname             import      set_logname                 # Used with --log option to output verbose output to log file


    # === Handle arguments passed to program / set defaults ===
    
    args = vars(check_arguments())


    # === Set log file name ===

    if args['log']:

        logname = set_logname()

    # # --------------- Output starting messages to user / set initial variables for program --------------- #

    # output_progress(arguments_received, '------------------- Internet Speed Test Checker v. 0.5 -------------------\n', log_name)
    # output_progress(arguments_received, 'Starting speed test timestamped: ' + str(date + '\n'), log_name)

if __name__ == "__main__":

    internet_speed_tester()