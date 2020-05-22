# === Import required functions / libraries ===

# --- Built-in ---

# Allows modifying HKCU reg key for setting IE zoom level
import winreg

# Used for terminating speed test when Exception raised
import sys

# Define Registry key location & name

ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
zoom_key_name = 'ZoomFactor'
zoom_value = 10000

# Define function for connecting to root key for RW access to values

def connect_key(root_key):

    ie_zoom_key_access = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, ie_key_location,
        0, winreg.KEY_ALL_ACCESS)

    return ie_zoom_key_access


# --- Create root key if it doesn't exist ---

def create_root_key(root_key_exists):

    if not root_key_exists:

        message = 'Creating Zoom HKCU root key...'
        print(message)

        try:

            winreg.CreateKey(reg_info.reg_connection, ie_key_location)
            return True

        except Exception:

            message = 'Unable to create root key. Terminating speed test'
            print(message)
            sys.exit()

    else:

        message = 'Zoom HKCU root key already exists'
        print(message)

# --- Create ZoomFactor subkey if it doesn't exist ---
