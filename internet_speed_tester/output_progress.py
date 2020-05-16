def output_progress(args, message, log_name):

    # === Import required functions / libraries ===

    # Built-in

    import      os      # Writes output to text file if --log specified

    # Functions built for project

    from        print_msg       import      print_msg       # Print messages to console with auto time.sleep


    # === Define function for writing log messages to text file in same directory as program

    def write_log(log_msg):

        # Check if log file exists already, create it if it doesn't

        log_check = os.path.exists('./' + log_name)

        if log_check == False:

            log_file = open(log_name,'w')
            log_file.close()

        # Append message to log file

        log_file = open(log_name,'a')
        log_file.write('\n' + message)
        log_file.close()

    
    # === Receive / handle args passed to this function from the commandline ===

    # If --debug specified, write console output to log file

    if args['log']:

        write_log(message)

    # If --verbose specified, write output to console

    if args['verbose']:

        print_msg(message)
