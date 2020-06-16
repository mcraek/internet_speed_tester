# === Import Dependenies ===

# Built-in

import sys

# Custom

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.registry_functions import set_subkey_value

# 3rd party

from selenium import webdriver


def end_web_session(args, log_name, option, registry, browser_instance):

    # Closes IE browser, restores original IE ZoomFactor value

    # Reset IE Zoom level back to its original setting if it was modified

    if registry.subkey_set:

        message = '+++ Restoring original IE ZoomFactor value'
        output_progress(args, message, log_name)

        try:

            set_subkey_value(args, log_name, None, registry.ie_original_zoom, registry.root_key, 'restore')

            print('Complete!')

        except Exception as e:
            
            message = 'Unable to restore original IE Zoom level. Error message: ' + str(e)
            output_progress(args, message, log_name)
            
    # Terminate IE Session

    if option == 'graceful':

        message = 'Program complete, terminating IE instance\n'
        output_progress(args, message, log_name)

        try:

            browser_instance.close()

        except Exception as e:

            message = 'Error closing browser intance. Error message: \n' + str(e)
            output_progress(args, message, log_name)

    elif option == 'error':

        message = ' Fatal error encountered. Terminating program.'
        output_progress(args, message, log_name)

        try:

            browser_instance.close()
                    
        except Exception as e:

            message = 'Error closing browser intance. Error message: \n' + str(e)
            output_progress(args, message, log_name)

        sys.exit()
