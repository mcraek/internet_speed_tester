def internet_speed_tester():

    # === Import required functions / libraries ===

    # --- Built-in ---

    # Used for terminating program in event of an error
    import sys

    # --- Functions built for project ---

    # Parse arguments passed from commandline
    from check_arguments import check_arguments

    # Used with --log option to output verbose output to log file
    from set_logname import set_logname

    # Verbose output to console / logfile with -v and -l args
    from output_progress import output_progress

    # Tests connection to fast.com
    from validate_site_connection import validate_site_connection

    # Queries registry for Internet Explorer ZoomFactor key required by Selenium
    from query_registry import query_registry

    # Sets ZoomFactor subkey value to 100%
    from set_registry import set_registry

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

    # --- Set IE Zoom Level to 100% (Selenium requirement) ---

    message = '+++ Checking IE Zoom Level is 100% for Selenium +++'
    output_progress(args, message, log_name)

    # Attempt connection to registry / check for existence of ZoomFactor key
    # Store connection to registry key if possible

    message = 'Querying registry...'
    output_progress(args, message, log_name)

    reg_info = query_registry(args, log_name)

    # If connected to registry, create / set ZoomFactor key value and store original
    # value to return to

    if (reg_info.registry_connected):

        message = 'Connection to registry successful. Ensuring ZoomFactor key is set to 100%...'
        output_progress(args, message, log_name)
        reg_changed = set_registry(args, reg_info, 'initial-set', log_name, zoom_factor_changed = False)

    else:

        message = 'Unable to connect to registry for checking ZoomFactor value. Terminating speed test...'
        sys.exit()

    # --- Begin speed test ---

    message = '++++ Starting speed test ++++'
    output_progress(args, message, log_name)

    # --- After speed test, restore original IE ZoomFactor value ---

    message = '+++ Checking if IE ZoomFactor registry value needs to be restored +++'
    output_progress(args, message, log_name)

    if reg_changed:

        message = 'Restoring original IE ZoomFactor value (' + str(reg_info.ie_original_zoom) + ')'
        output_progress(args, message, log_name)

        set_registry(args, reg_info, 'restore-setting', log_name, zoom_factor_changed = False)

    else:

        message = 'IE ZoomFactor key value unchanged during speed test'
        output_progress(args, message, log_name)


if __name__ == "__main__":

    internet_speed_tester()
