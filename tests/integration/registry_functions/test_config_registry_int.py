# === Import required functions / libraries ===

# --- Built for project ---

from internet_speed_tester.registry_functions.config_registry \
    import config_registry

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Test config_registry can access HKCU key and return / set
# values for the ZoomFactor subkey on the system test
# is run on


def test_config_registry():

    reg_info = config_registry(args, log)

    assert reg_info.subkey_set or not reg_info.subkey_set
    assert type(reg_info.ie_original_zoom) is int
    assert reg_info.root_key is not None
