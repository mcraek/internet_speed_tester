# === Import dependencies ===

# Custom

from internet_speed_tester.registry_functions.set_registry2 import connect_registry, check_root_key, check_subkey,\
    set_subkey

from internet_speed_tester.misc_functions import output_progress


def build_class(a, b, c):

    # Returns class containing registry connection / info back

    class RegistryConnection:

        pass

    reg = RegistryConnection()

    reg.subkey_set = a
    reg.ie_original_zoom = b
    reg.root_key = c

    return reg


def config_registry(args, log_name):

    # Queries / sets registry IE ZoomFactor value, enables IE protected zones, disables first IE run setup,
    # returns original settings

    # === Connect to registry / store info on IE ZoomFactor key ===

    message = '--- Setting IE Zoom Factor to 100% ---'
    output_progress(args, message, log_name)

    # Connect to HKCU registry hive

    hive = 'HKEY_CURRENT_USER'
    reg_connection = connect_registry(args, log_name, hive)

    # Create root key if it doesn't exist

    root_key_path = r'Software\\Microsoft\\Internet Explorer\\Zoom'
    root_key_exists, root_key = check_root_key(args, log_name, reg_connection, root_key_path)

    # Find subkey if root key exists and store existing ZoomFactor value, store access to subkey to restore original value

    subkey_name = 'ZoomFactor'
    subkey_exists, ie_original_zoom, subkey_access = check_subkey(args, log_name, hive, root_key_exists, root_key_path, subkey_name)

    # Set ZoomFactor Registry Value To 100% For Selenium If Not Already Set To This

    expected_value = 100000
    reg_type = 'REG_DWORD'
    subkey_changed = set_subkey(args, log_name, subkey_name, subkey_access, subkey_exists, ie_original_zoom, expected_value, reg_type)
    
    # Ensure all IE Protected Zones Are Enabled using existing HKCU connection

    '''
    Selenium requires Protected Zones in IE either to all be enabled or disabled. This can
    be controlled with registry settings.

    There is an option with the Selenium web driver to ignore this setting and launch
    anyway, after testing with that option, that was found to not work well in this
    case.

    Here are the security zones as they're located in the registry:
    0 = Local Machine zone
    1 = Intranet zone
    2 = Trusted Sites zone
    3 = Internet zone
    4 = Restricted Sites zone

    Example: Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\2 = Trusted Sites

    Changing the "2500" subkey value in the registry to DWORD 0 enables the Protected Zone

    Source: https://stackoverflow.com/questions/17677127/python-protection-settings-ie

    '''

    message = '--- Enabling IE Protected Zones ---'
    output_progress(args, message, log_name)

    zones = ['0','1','2','3','4']

    for zone in zones:

        # Check for / create root key

        root_key = r'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\'
        root_key_path = str(root_key) + str(zone)
        root_key_exists, root_key = check_root_key(args, log_name, reg_connection, root_key_path)

        # Enable IE Protected Zone

        subkey_name = '2500'
        subkey_path = str(root_key) + str(zone) + str(subkey_name)

        expected_value = 0
        reg_type = 'REG_DWORD'

        subkey_exists, original_zone_setting, subkey_access = check_subkey(args, log_name, hive, root_key_exists, root_key_path, subkey_name)
        subkey_changed = set_subkey(args, log_name, subkey_name, subkey_access, subkey_exists, original_zone_setting, expected_value, reg_type)
    
    # Skip IE first time setup wizard using existing HKCU connection

    message = '--- Disabling IE first run setup wizard ---'
    output_progress(args, message, log_name)

    root_key_path = r'Software\\Microsoft\\Internet Explorer\\Main'
    root_key_exists, root_key = check_root_key(args, log_name, reg_connection, root_key_path)

    subkey_name = 'DisableFirstRunCustomize'
    subkey_exists, original_ie_setup, subkey_access = check_subkey(args, log_name, hive, root_key_exists, root_key_path, subkey_name)

    # Set DisableFirstRunCustomize registry value to 1 to disable the wizard

    expected_value = 1
    reg_type = 'REG_DWORD'
    subkey_changed = set_subkey(args, log_name, subkey_name, subkey_access, subkey_exists, original_ie_setup, expected_value, reg_type)

    # Return class with reg connection / and info

    reg_info = build_class(subkey_changed, ie_original_zoom, root_key)

    return reg_info


if __name__ == '__main__':

    config_registry()
