def test_site_connection(args, site, log_name):

    # === Import built-in dependencies ===

    import subprocess # Allows running ping utility on Windows systems

    # === Import funcitons built for project ===

    from internet_speed_tester import output_progress

    # === Begin Function ===

    # Run ping test to site received as argument

    ping_test = subprocess.run([ 'ping', site ], capture_output=True)

    # Capture the stdout of the ping command run by cmd.exe on Windows
    ping_results = ping_test.stdout.decode() 

    # Windows sends four echo requests by default. As long as all four
    # are not lost, return True to indicate a successful connection

    if '%' in ping_results and 'Lost = 4' not in ping_results:  

        connection_successful = True

    else:

        connection_successful = False

    # Terminate program if connection to site not established
    # otherwise continue the program

    if connection_successful == False:

        message = 'Connection to ' + site + ' failed. Check your connection. Website may also be down...'
        output_progress(args, message, log_name)
        sys.exit()

    else:

        message = site + ' appears to be online and reachable\n'
        output_progress(args, message, log_name)