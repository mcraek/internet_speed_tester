def set_registry(args, reg_info, option, log_name, zoom_factor_changed = False):

    # === Import required functions / libraries ===

    # --- Built-in ---

    # Allows modifying HKCU reg key for setting IE zoom level
    import winreg

    # Terminates program in event of an error
    import sys

    # --- Built for project ---

    from output_progress import output_progress


    # === Begin function ===

    # Define Registry key location & name

    ie_key_location = r'Software\\Microsoft\\Internet Explorer\\Zoom'
    zoom_key_name = 'ZoomFactor'
    zoom_value = 10000
    

    # Define function for connecting to root key for RW access to values

    def connect_key(root_key):

        ie_zoom_key_access = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)

        return ie_zoom_key_access

    # --- Create root key and ZoomFactor key if they don't already exist ---
    # if the key exists, ensure the value is set for the ZoomFactor to be 100%
    
    # - Set new value option

    if option == 'initial-set':

        zoom_factor_changed = False

        if not reg_info.root_key_exists:

            message = 'Creating Zoom HKCU root key...'
            output_progress(args, message, log_name)
            winreg.CreateKey(reg_info.reg_connection, ie_key_location)

        if not reg_info.subkey_exists:

            message = 'Creating ZoomFactor subkey...'
            output_progress(args, message, log_name)

            ie_zoom_key_access = connect_key(reg_info.root_key)
            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, zoom_value)

        else:

            # If ZoomFactor subkey exists, ensure this is set to 100%

            if reg_info.ie_original_zoom != 10000:

                message = 'Current IE ZoomFactor setting is ' + \
                str(reg_info.ie_original_zoom) + '. This needs to be set to 10000 (100%)' + \
                ' for Selenium to work properly.\nSetting value. This will be restored' + \
                ' to the original setting once the speed test completes...'

                output_progress(args, message, log_name)

                ie_zoom_key_access = connect_key(reg_info.root_key)
                winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, zoom_value)
                zoom_factor_changed = True

        return zoom_factor_changed

    # - Set original value option

    elif option == 'restore-setting':

        ie_zoom_key_access = connect_key(reg_info.root_key)
        winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 0, winreg.REG_DWORD, reg_info.ie_original_zoom)







