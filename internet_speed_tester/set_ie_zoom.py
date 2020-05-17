def set_ie_zoom(args, log_name, option,zoom_value = 100000):

    # 100000 is the decimal equivalent of 100% for the DWORD reg key this edits

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

    ie_key_location = r'Software\Microsoft\Internet Explorer\Zoom'
    zoom_key_name = 'ZoomFactor'

    # Open up root key location in registry, full access & Define Key name for Editing

    try:

        message = 'Attempting to obtain write access to registry key ' + \
        'within HKCU at for reading / setting IE zoom value' + ie_key_location
        output_progress(args, message, log_name)

        ie_zoom_key_access = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)

    except:

        message = 'Unable to open the registry key. Terminating program.'
        output_progress(args, message, log_name)
        sys.exit()

    # Return original key value

    if option == 'get_original_value':

        try:

            message = 'Attempting to obtain original value of the ' + \
            zoom_key_name + ' registry key for returning to this after ' + \
            'program completion'
            
            output_progress(args, message, log_name)
            
            # Access decimal value with [0], [1] would access hex value

            ie_original_zoom = (winreg.QueryValueEx(
                ie_zoom_key_access, zoom_key_name))[0]

            return ie_original_zoom

        except:

            message = 'Unable to find key value. Terminating program.'
            output_progress(args, message, log_name)
            sys.exit()

    # Modify zoom level key, default to 100%

    if option == 'set_zoom':

        try:

            message = 'Attempting to modify the value of the ' + \
            zoom_key_name + ' registry key to ' + str(zoom_value)
            
            output_progress(args, message, log_name)

            # This modifies the decimal value of the DWORD key
            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 
            1, winreg.REG_DWORD, zoom_value) 

        except:

            message = 'Unable to modify the key value. Terminating program.'
            output_progress(args, message, log_name)

            sys.exit()

    # Close Registry Key Access

    message = 'Removing write access to the ' + \
    'registry at ' + ie_key_location

    output_progress(args, message, log_name)

    # Remomve access to key (reopened later when changing setting back)
    winreg.CloseKey(ie_zoom_key_access) 
