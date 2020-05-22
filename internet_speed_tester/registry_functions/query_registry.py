 # Creates / returns class containing info on ZoomFactor registry key

# === Import required functions / libraries ===

# --- Built-in ---

# Allows modifying HKCU reg key for setting IE zoom level
import winreg

# --- Built for project ---

#from output_progress import output_progress

# === Begin function ===

# Define reg key location & name

ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
zoom_key_name = 'ZoomFactor'

# Initialize error message variable

error = ''

# Determine if HKCU can be connected to, store connection to return

def connect_registry():

    message = 'Attempting connection to HKCU hive'
    print(message)

    try:

        reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        message = 'Connected to HKCU successfully'
        print(message)

    except Exception:

        reg_connection = None
        message = 'Failed to connect to HKCU'
        print(message)

    return reg_connection

# Check if root key exists in registry

def check_root_key(reg_connection):

    message = 'Checking for HKCU:' + ie_key_location + ' registry key'
    print(message)

    # Check if root key exists

    try:

        root_key = winreg.OpenKey(reg_connection, ie_key_location)
        root_key_exists = True

        message = 'Root key found.'
        print(message)

    except Exception:

        root_key = None
        root_key_exists = False

        message = 'Root key not found.'
        print(message)

    return root_key_exists, root_key

# Find subkey if root key exists and return ZoomFactor value

def check_subkey(reg_connection, root_key_exists, root_key):

    if not root_key_exists:

        subkey_exists = False
        ie_original_zoom = None

    else:

        try:

            ie_zoom_key_access = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)
            ie_original_zoom = (winreg.QueryValueEx(ie_zoom_key_access, zoom_key_name))[0]
            subkey_exists = True
            message = 'Subkey found.'
            print(message)

        except Exception:

            message = 'Subkey not found.'
            print(message)
            subkey_exists = False
            ie_original_zoom = None

    return subkey_exists, ie_original_zoom





# If root key isn't found, the subkey will not exist either
subkey_exists = False
ie_original_zoom = None