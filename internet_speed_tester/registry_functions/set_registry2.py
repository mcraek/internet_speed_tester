# === Import dependencies ===

# Built-in

import winreg
import sys

# Custom

from internet_speed_tester.misc_functions import output_progress


def connect_registry(args, log_name, hive):

    # Attempt to connect to registry hive, store connection to return if successful

    message = 'Attempting connection to ' + hive + " registry hive"
    output_progress(args, message, log_name)

    try:

        # Using getattr allows accessing attributes via dynamic variable
        # An alternative would be winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        
        reg_hive = getattr(winreg, hive)
        connection = winreg.ConnectRegistry(None, reg_hive)
        
        message = 'Connected to ' + hive + ' registry hive successfully'
        output_progress(args, message, log_name)

    except Exception as e:

        connection = None
        message = 'Failed to connect to the ' + hive + ' registry hive. \nError Message: ' + str(e)
        output_progress(args, message, log_name)

    return connection


def check_root_key(args, log_name, reg_connection, root_key_path):

    # Checks for the root key in the registry. If not found, this will create it
    # and return whether or not the key existed

    message = 'Checking for ' + root_key_path + ' root registry key'
    output_progress(args, message, log_name)

    try:

        root_key = winreg.OpenKey(reg_connection, root_key_path)
        root_key_exists = True

        message = 'Root key found.'
        output_progress(args, message, log_name)

    except Exception as e:

        root_key = None
        root_key_exists = False

        message = 'Root key not found.\nError message: ' + str(e)
        output_progress(args, message, log_name)

    if not root_key_exists:

        message = 'Creating the ' + root_key_path + ' root key...'
        output_progress(args, message, log_name)

        try:

            winreg.CreateKey(reg_connection, root_key_path)
            return True

        except Exception as e:

            message = 'Unable to create root key. Terminating program.'
            output_progress(args, message, log_name)
            sys.exit()

    return root_key_exists, root_key


def check_subkey(args, log_name, hive, root_key_exists, root_key_path, subkey_name):

    # Checks a subkey value and returns its original value if it exists. Otherwise returns false if the
    # key does not exist

    reg_hive = getattr(winreg, hive)

    try:

        message = 'Attempting connection to ' + root_key_path + ' root key'
        output_progress(args, message, log_name)
        subkey_access = winreg.OpenKey(reg_hive, root_key_path, 0, winreg.KEY_ALL_ACCESS)

    except Exception as e:

        message = 'Unable to establish registry connection to root key. Error message: ' + str(e)
        output_progress(args, message, log_name)

    if not root_key_exists:

        subkey_exists = False
        original_key_value = None

    # Check if the subkey exists

    else:

        try:

            message = 'Searching root key for ' + str(subkey_name) + ' subkey'
            output_progress(args, message, log_name)
            original_key_value = (winreg.QueryValueEx(subkey_access, subkey_name))[0]

            subkey_exists = True

        except Exception as e:

            message = 'Subkey not found. Results of check: ' + str(e)
            output_progress(args, message, log_name)
            subkey_exists = False
            original_key_value = None

    # Output and return results

    if subkey_exists:

        message = 'Subkey found. Original value = ' + str(original_key_value)

    else:

        message = 'Subkey not found.'

    output_progress(args, message, log_name)

    return subkey_exists, original_key_value, subkey_access


def set_subkey(args, log_name, subkey_name, subkey_access, subkey_exists, original_key_value, expected_value, reg_type):

    # Creates / sets subkey value to the expected value. Returns whether or not existing value was changed

    key_type = getattr(winreg, reg_type)
    change_reqd = False

    # Set output messages depending on requirements

    if not subkey_exists:

        message = 'Creating and setting ' + subkey_name + ' subkey to ' + str(expected_value)
        change_reqd = True

    if original_key_value != expected_value:

        message = subkey_name + 'value ' + str(original_key_value) + ' does not match expected value ' + str(expected_value)
        message += '. Setting value'
        change_reqd = True

    else:

        message = 'Existing subkey value already meets requirements.'

    output_progress(args, message, log_name)

    # Set subkey value if required

    if change_reqd:

        winreg.SetValueEx(subkey_access, subkey_name, 0, key_type, expected_value)
        subkey_changed = True

    else:

        subkey_changed = False

    return subkey_changed