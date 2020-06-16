# === Import dependencies ===

# Built-in

import winreg
import sys

# Custom

from internet_speed_tester.misc_functions import output_progress

# Define Registry key location & name

ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
zoom_key_name = 'ZoomFactor'
zoom_value = 100000


def connect_key(args, log_name, root_key):

    # Connects to root key for RW access to values

    try:

        ie_zoom_key_access = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)

        return ie_zoom_key_access

    except Exception as e:

        message = 'Unable to connect to root key. Terminating speed test.\nError message: ' + str(e)
        output_progress(args, message, log_name)

        ie_zoom_key_access = None

        sys.exit()


def create_root_key(args, log_name, root_key_exists, reg_connection):

    # Creates root key if it doesn't already exist

    if not root_key_exists:

        message = 'Creating Zoom HKCU root key...'
        output_progress(args, message, log_name)

        try:

            winreg.CreateKey(reg_connection, ie_key_location)
            return True

        except Exception as e:

            message = 'Unable to create root key. Terminating speed test.\nError message: ' + str(e)
            output_progress(args, message, log_name)
            sys.exit()

    else:

        message = 'Zoom HKCU root key already exists'
        output_progress(args, message, log_name)
        return False


def create_subkey(args, log_name, subkey_exists, root_key):

    # Creates ZoomFactor subkey if it doesn't exist

    if not subkey_exists:

        try:

            ie_zoom_key_access = connect_key(args, log_name, root_key)
            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, zoom_value)
            return True

        except Exception as e:

            message = 'Unable to create subkey. Terminating speed test.\nError message: ' + str(e)
            output_progress(args, message, log_name)
            sys.exit()

    else:

        message = 'ZoomFactor subkey already exists'
        output_progress(args, message, log_name)
        return False


def set_subkey_value(args, log_name, value, ie_original_zoom, root_key, option):

    # Sets ZoomFactor subkey value

    # Config option sets IE ZoomFactor to 100%

    if option == 'config' and ie_original_zoom != 100000:

        message = 'Current IE ZoomFactor is ' + str(ie_original_zoom)
        output_progress(args, message, log_name)

        message = 'Setting value to 10000 (100%)...'
        output_progress(args, message, log_name)

        try:

            ie_zoom_key_access = connect_key(args, log_name, root_key)
            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, zoom_value)
            return True

        except Exception as e:

            message = 'Unable to create root key. Terminating speed test.\nError message: ' + str(e)
            output_progress(args, message, log_name)
            sys.exit()

    # Restore option restores the original IE ZoomFactor value pulled from system

    elif option == 'restore':

        message = 'Restoring IE ZoomFactor to original value'

        try:

            ie_zoom_key_access = connect_key(args, log_name, root_key)
            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, ie_original_zoom)
            return True

        except Exception as e:

            message = 'Unable to restore original zoom value. Error message: ' + str(e)
            output_progress(args, message, log_name)
            sys.exit()

    else:

        message = 'IE ZoomFactor is already at 100%'
        output_progress(args, message, log_name)
        return False
