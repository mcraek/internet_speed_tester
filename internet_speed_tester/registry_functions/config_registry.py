# === Import dependencies ===

# Custom

from internet_speed_tester.registry_functions.set_registry2 import connect_registry, check_root_key, check_subkey,\
    set_subkey


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

    # Queries / sets registry IE ZoomFactor value

    # === Connect to registry / store info on IE ZoomFactor key ===

    # Connect to HKCU registry hive

    hive = 'HKEY_CURRENT_USER'
    reg_connection = connect_registry(args, log_name, hive)

    # Create root key if it doesn't exist

    root_key_path = r'Software\\Microsoft\\Internet Explorer\\Zoom'
    root_key_exists, root_key = check_root_key(args, log_name, reg_connection, root_key_path)

    # Find subkey if root key exists and store existing ZoomFactor value, store access to subkey to restore original value

    subkey_name = 'ZoomFactor'
    subkey_exists, ie_original_zoom, zoom_key_access = check_subkey(args, log_name, hive, root_key_exists, root_key_path, subkey_name)

    # Set ZoomFactor Registry Value To 100% For Selenium If Not Already Set To This

    expected_value = 100000
    reg_type = 'REG_DWORD'
    subkey_changed = set_subkey(args, log_name, subkey_name, zoom_key_access, subkey_exists, ie_original_zoom, expected_value, reg_type)
    
    # Return class with reg connection / and info

    reg_info = build_class(subkey_changed, ie_original_zoom, root_key)

    return reg_info


if __name__ == '__main__':

    config_registry()
