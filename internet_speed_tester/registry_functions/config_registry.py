from query_registry import connect_registry, check_root_key, check_subkey
from set_registry import create_root_key, create_subkey, set_subkey_value
import sys

def config_registry():

    # === Query Registry For ZoomFactor Value ===

    # Connect to registry

    reg_connection = connect_registry()

    # Find root key

    root_key_exists, root_key = check_root_key(reg_connection)

    # Find subkey if root key exists and return ZoomFactor value

    subkey_exists, ie_original_zoom = check_subkey(reg_connection, root_key_exists, root_key)

    # === Set ZoomFactor Registry Value To 100% For Selenium ===

    # Create root key if required

    root_key_created = create_root_key(root_key_exists, reg_connection)

    # Create ZoomFactor subkey if required

    subkey_created = create_subkey(subkey_exists, root_key)

    # If ZoomFactor subkey exists already, ensure this is set to 100%

    subkey_set = set_subkey_value(10000, ie_original_zoom, root_key, 'config')

    # Return original ZoomFactor value to reset this following completion 
    # of speed test

    return ie_original_zoom

if __name__ == '__main__':

    config_registry()