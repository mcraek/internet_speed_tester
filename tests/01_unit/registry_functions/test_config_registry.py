# === Import required functions / libraries ===

# --- Built-in ---

from unittest.mock import patch

# --- Built for project ---

from internet_speed_tester.registry_functions.config_registry \
    import config_registry

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Patch all functions imported into config_registry and verify
# it returns a class of info.


def test_config_registry():

    with patch('internet_speed_tester.registry_functions.query_registry.connect_registry'), \
                patch('internet_speed_tester.registry_functions.query_registry.check_root_key'), \
                patch('internet_speed_tester.registry_functions.query_registry.check_subkey'), \
                patch('internet_speed_tester.registry_functions.set_registry.create_root_key'), \
                patch('internet_speed_tester.registry_functions.set_registry.create_subkey'), \
                patch('internet_speed_tester.registry_functions.set_registry.set_subkey_value'):

        reg_info = config_registry(args, log)

        assert None not in (reg_info.subkey_set, reg_info.ie_original_zoom,
                            reg_info.root_key)
