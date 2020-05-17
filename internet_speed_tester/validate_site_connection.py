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
    # are not lost, and an Average RTT is calculated return True to
    # indicate a successful connection to the site.
    # Any other issues, local or otherwise will return false as well
    # as dropped pings

    received_responses = ['Sent = 4', 'Received = 4' 'Average = ']
    status = all(item in received_responses for item in ping_results)

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
