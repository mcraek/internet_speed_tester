# === Import required functions / libraries ===

# --- Built for project ---

from internet_speed_tester.web_scraping_functions.initialize_ie_session \
    import start_ie_session

from internet_speed_tester.registry_functions.config_registry \
    import config_registry

# Setup arguments to pass to set_registry functions

args = {'log': False, 'verbose': False}
log = "log"

# Validate start_ie_session is capable of starting / returning an IE
# session on the system program is run on. Also validate the IE
# window is hidden


def test_start_ie_session():

    # This requires IE ZoomFactor level be set to 100%

    reg_info = config_registry(args, log)

    # Test start_ie_session

    browser_instance, window_hidden = start_ie_session(args, log, reg_info.ie_original_zoom)

    assert browser_instance is not None
    assert window_hidden

    # Terminate IE instance

    browser_instance.close()
