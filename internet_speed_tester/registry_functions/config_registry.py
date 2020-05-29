# === Import required functions / libraries ===

# --- Built for project ---

from internet_speed_tester.registry_functions.query_registry \
    import connect_registry, check_root_key, check_subkey

from internet_speed_tester.registry_functions.set_registry \
    import create_root_key, create_subkey, set_subkey_value

# Define function for returning class of info back


def build_class(a, b, c):

    class RegistryConnection:

        pass

    reg = RegistryConnection()

    reg.subkey_set = a
    reg.ie_original_zoom = b
    reg.root_key = c

    return reg

# Define main function for querying / setting registry value


def config_registry(args, log_name):

    # === Query Registry For ZoomFactor Value ===

    # Connect to registry

    reg_connection = connect_registry(args, log_name)

    # Find root key

    root_key_exists, root_key = check_root_key(args, log_name, reg_connection)

    # Find subkey if root key exists and return ZoomFactor value

    subkey_exists, ie_original_zoom = \
        check_subkey(args, log_name, reg_connection,
                     root_key_exists, root_key)

    # === Set ZoomFactor Registry Value To 100% For Selenium ===

    # Create root key if required

    create_root_key(args, log_name, root_key_exists, reg_connection)

    # Create ZoomFactor subkey if required

    create_subkey(args, log_name, subkey_exists, root_key)

    # If ZoomFactor subkey exists already, ensure this is set to 100%

    subkey_set = set_subkey_value(args, log_name, 100000,
                                  ie_original_zoom, root_key,
                                  'config')

    # Return class containing info for resetting
    # ZoomFactor key to original value

    reg_info = build_class(subkey_set, ie_original_zoom, root_key)

    return reg_info


if __name__ == '__main__':

    config_registry()
