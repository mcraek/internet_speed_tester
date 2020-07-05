# === Import dependencies ===

# Custom

from internet_speed_tester.registry_functions.set_registry2 import connect_registry, check_root_key, check_subkey,\
    set_subkey

from internet_speed_tester.misc_functions import output_progress


class RegSetting():

    def __init__self():

        self.subkey_set = ''
        self.original_value = ''
        self.root_key = ''
        self.subkey_exists = ''

# Initialize classes for returning information on and connections to registry keys that will be checked / configured

zoom_info = RegSetting()
protected_zone_info = RegSetting()
initialization_wizard_info = RegSetting()


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

    zoom_root_key_path = r'Software\\Microsoft\\Internet Explorer\\Zoom'
    zoom_root_key_exists, zoom_root_key = check_root_key(args, log_name, reg_connection, zoom_root_key_path)

    # Find subkey if root key exists and store existing ZoomFactor value, store access to subkey to restore original value

    zoom_subkey_name = 'ZoomFactor'
    zoom_subkey_exists, ie_original_zoom, zoom_subkey_access = check_subkey(args, log_name, hive, zoom_root_key_exists, zoom_root_key_path, zoom_subkey_name)

    # Set ZoomFactor Registry Value To 100% For Selenium If Not Already Set To This

    expected_value = 100000
    reg_type = 'REG_DWORD'
    zoom_subkey_changed = set_subkey(args, log_name, zoom_subkey_name, zoom_subkey_access, zoom_subkey_exists, ie_original_zoom, expected_value, reg_type)

    # Add information on zoom factor registry settings to class created earlier

    setattr(zoom_info, 'subkey_set', zoom_subkey_changed)
    setattr(zoom_info, 'original_value', ie_original_zoom)
    setattr(zoom_info, 'root_key', zoom_root_key)
    setattr(zoom_info, 'subkey_exists', zoom_subkey_exists)
    
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

        # Store information on registry changes to Zones class created earlier

        attribute_1 = 'zone_' + str(zone) + '_subkey_set'
        attribute_2 = 'zone_' + str(zone) + '_original_value'
        attribute_3 = 'zone_' + str(zone) + '_root_key'
        attribute_4 = 'zone_' + str(zone) + '_subkey_exists'

        setattr(protected_zone_info, attribute_1, subkey_changed)
        setattr(protected_zone_info, attribute_2, original_zone_setting)
        setattr(protected_zone_info, attribute_3, subkey_access)
        setattr(protected_zone_info, attribute_4, subkey_exists)

        # Creates class for storing information on each IE Protected Zone registry setting
    
    # Skip IE first time setup wizard using existing HKCU connection

    message = '--- Disabling IE first run setup wizard ---'
    output_progress(args, message, log_name)

    wizard_root_key_path = r'Software\\Microsoft\\Internet Explorer\\Main'
    wizard_root_key_exists, wizard_root_key = check_root_key(args, log_name, reg_connection, wizard_root_key_path)

    wizard_subkey_name = 'DisableFirstRunCustomize'
    wizard_subkey_exists, original_ie_setup, wizard_subkey_access = check_subkey(args, log_name, hive, wizard_root_key_exists, wizard_root_key_path, wizard_subkey_name)

    # Set DisableFirstRunCustomize registry value to 1 to disable the wizard

    expected_value = 1
    reg_type = 'REG_DWORD'
    wizard_subkey_changed = set_subkey(args, log_name, wizard_subkey_name, wizard_subkey_access, wizard_subkey_exists, original_ie_setup, expected_value, reg_type)

    # Add information on the IE initialization wizard registry settings to class created earlier

    setattr(initialization_wizard_info, 'subkey_set', wizard_subkey_changed)
    setattr(initialization_wizard_info, 'original_value', original_ie_setup)
    setattr(initialization_wizard_info, 'root_key', wizard_root_key)
    setattr(initialization_wizard_info, 'subkey_exists', wizard_subkey_exists)

    # Return classes with reg connections / info

    return zoom_info, protected_zone_info, initialization_wizard_info


if __name__ == '__main__':

    config_registry()
