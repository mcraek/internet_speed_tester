# === Dependencies ===

# Built-in

import winreg

# Custom

from internet_speed_tester.misc_functions import output_progress

# Define reg key location & name

ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
zoom_key_name = 'ZoomFactor'


def connect_registry(args, log_name):

    # Attempt to connect to HKCU, store connection to return if successful

    message = 'Attempting connection to HKCU hive'
    output_progress(args, message, log_name)

    try:

        reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        message = 'Connected to HKCU successfully'
        output_progress(args, message, log_name)

    except Exception as e:

        reg_connection = None
        message = 'Failed to connect to HKCU.\nError Message: ' + str(e)
        output_progress(args, message, log_name)

    return reg_connection


def check_root_key(args, log_name, reg_connection):

    # Check if root key exists in registry, if so connect to it and return connection

    message = 'Checking for HKCU:' + ie_key_location + ' registry key'
    output_progress(args, message, log_name)

    try:

        root_key = winreg.OpenKey(reg_connection, ie_key_location)
        root_key_exists = True

        message = 'Root key found.'
        output_progress(args, message, log_name)

    except Exception as e:

        root_key = None
        root_key_exists = False

        message = 'Root key not found.\nError message: ' + str(e)
        output_progress(args, message, log_name)

    return root_key_exists, root_key


def check_subkey(args, log_name, reg_connection, root_key_exists, root_key):

    # Find subkey if root key exists and return ZoomFactor value

    if not root_key_exists:

        subkey_exists = False
        ie_original_zoom = None

    else:

        try:

            ie_zoom_key_access = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)

            ie_original_zoom = (winreg.QueryValueEx(ie_zoom_key_access, zoom_key_name))[0]
            
            subkey_exists = True
            message = 'Subkey found.'
            output_progress(args, message, log_name)

        except Exception as e:

            message = 'Subkey not found.\nError message: ' + str(e)
            output_progress(args, message, log_name)
            subkey_exists = False
            ie_original_zoom = None

    return subkey_exists, ie_original_zoom
