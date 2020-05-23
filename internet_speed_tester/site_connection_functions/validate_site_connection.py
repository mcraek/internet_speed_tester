# === Import required functions / libraries ===

# --- Built-in ---

# Allows calling ping utility
import subprocess


# --- Built for project ---

from output_progress import output_progress


def validate_site_connection(args, site, log_name):

    message = '+++ Testing connection to ' + site + ' +++'
    output_progress(args, message, log_name)

    # Initialize status message containing results of ping command

    ping_results = ''

    # --- Run ping test to site and store raw command call / stdout ---

    try:

        ping_test = subprocess.run(['ping', site], capture_output=True)

        # Capture stdout of the command
        ping_results += str(ping_test.stdout.decode())

    except Exception as e:

        ping_results += str(e)

    # --- Determine if connection to site was successful ---

    if ping_test.returncode == 0:

        status = True

    else:

        status = False

    return status, ping_results
