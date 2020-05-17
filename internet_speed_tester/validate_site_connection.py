def validate_site_connection(args, site, log_name):

    # === Import built-in dependencies ===

    # Allows running ping utility on Windows systems
    import subprocess

    # === Begin Function ===

    # --- Run ping test to site and store raw command call / stdout ---

    ping_test = subprocess.run(['ping', site], capture_output=True)
    ping_results = ping_test.stdout.decode()

    # --- Determine if connection to site was successful ---

    # Windows sends four echo requests by default. As long as all four
    # are not lost return True

    if 'Sent = 4, Received = 4,' in ping_results:

        status = True
    
    else:

        status = False

    # --- Build / return class (object) containing connection test results ---

    def build_class(a, b, c):

        class ConnectionTestResults:

            pass

        results = ConnectionTestResults()

        results.ping = a
        results.ping_result = b
        results.connection_successful = c

        return results

    # Pass ping test results including raw command call to class

    connection_result = build_class(ping_test, ping_results, status)

    return connection_result
