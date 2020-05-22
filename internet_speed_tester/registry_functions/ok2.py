from ok import connect_registry, check_root_key, check_subkey
from ok3 import create_root_key
import sys

# === Query Registry For ZoomFactor Value ===

# Connect to registry

reg_connection = connect_registry()

# Find root key

root_key_exists, root_key = check_root_key(reg_connection)

# Find subkey if root key exists and return ZoomFactor value

subkey_exists, ie_original_zoom = check_subkey(reg_connection, root_key_exists, root_key)

# === Set ZoomFactor Registry Value To 100% For Selenium ===

# Create root key if required

root_key_found = create_root_key(root_key_exists)

# Create ZoomFactor subkey if required

