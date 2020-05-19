def query_registry(args, log_name):

    # Creates / returns class containing info on ZoomFactor registry key

    # === Import required functions / libraries ===

    # --- Built-in ---

    # Allows modifying HKCU reg key for setting IE zoom level
    import winreg

    # --- Built for project ---

    from output_progress import output_progress

    # === Begin function ===

    # Define reg key location & name

    ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
    zoom_key_name = 'ZoomFactor'

    # Initialize error message variable

    error = ''

    # Determine if HKCU can be connected to, store connection to return

    message = 'Attempting connection to HKCU hive'
    output_progress(args, message, log_name)

    try:

        reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        registry_connected = True
        message = 'Connected to HKCU successfully'
        output_progress(args, message, log_name)

    except Exception:

        reg_connection = None
        message = 'Failed to connect to HKCU'
        output_progress(args, message, log_name)
        error += message
        registry_connected = False

    # If connected to HKCU, determine if Zoom root key
    # and ZoomFactor subkey exists

    if registry_connected:

        message = 'Checking for HKCU:' + ie_key_location + ' registry key'
        output_progress(args, message, log_name)

        # Check if root key exists

        try:

            root_key = winreg.OpenKey(reg_connection, ie_key_location)
            root_key_exists = True
            message = 'Root key found.'
            output_progress(args, message, log_name)

        except Exception:

            root_key = None
            root_key_exists = False

            # If root key isn't found, the subkey will not exist either
            subkey_exists = False
            ie_original_zoom = None

            message = 'Root key not found.'
            output_progress(args, message, log_name)

        # If root key exists, check if subkey exists

        # Define function for connecting to root key for RW access to values

        if root_key_exists:

            def connect_key(root_key):

                ie_zoom_key_access = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    ie_key_location, 0, winreg.KEY_ALL_ACCESS)

                return ie_zoom_key_access

            # Connect to root key with RW access to values within

            try:

                ie_zoom_key_access = connect_key(root_key)

                ie_original_zoom = (winreg.QueryValueEx(
                    ie_zoom_key_access, zoom_key_name))[0]

                message = 'Subkey found.'
                output_progress(args, message, log_name)
                subkey_exists = True

            except Exception:

                message = 'Subkey not found.'
                output_progress(args, message, log_name)
                subkey_exists = False
                ie_original_zoom = None

    # If no connection to registry made, set values to None

    else:

        registry_connected = False
        reg_connection = None
        root_key = None
        root_key_exists = None
        subkey_exists = None
        ie_original_zoom = None

    # Build class to return values in

    def build_class(a, b, c, d, e, f):

        class RegistryQueryResults:

            pass

        results = RegistryQueryResults()

        results.registry_connected = a
        results.reg_connection = b
        results.root_key = c
        results.root_key_exists = d
        results.subkey_exists = e
        results.ie_original_zoom = f

        return results

    # Pass query results to class

    query_result = build_class(
        registry_connected, reg_connection, root_key, root_key_exists,
        subkey_exists, ie_original_zoom)

    return query_result
