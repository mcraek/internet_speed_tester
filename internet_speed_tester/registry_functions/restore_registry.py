# === Import dependencies ===

# Built-in

import winreg

# Custom

from internet_speed_tester.misc_functions import output_progress
from internet_speed_tester.registry_functions.set_registry2 import set_subkey


def delete_key(args, log_name, registry, reg_connection, key):

    reg_setting = getattr(registry, key)

    # Remove subkey if it didn't exist before

    if not getattr(reg_setting, 'subkey_exists'):

        try:

            message = str(reg_setting.subkey_name) + ' subkey did not exist prior to running speed test. ' + \
                'Deleting it from ' + str(reg_setting.root_key_path)
            
            output_progress(args, message, log_name)

            winreg.DeleteValue(reg_setting.subkey_access, reg_setting.subkey_name)

        except Exception as e:

            message = 'Failed to delete the subkey. Error message: ' + str(e)
            output_progress(args, message, log_name)

    else:

        message = 'The ' + str(reg_setting.subkey_name) + ' subkey already existed prior to running speed test.' 
        output_progress(args, message, log_name)


def recover_registry(args, log_name, registry, reg_connection):

    # Restores registry settings that were altered prior to running speed test

    # Restore IE Zoom Factor

    delete_key(args, log_name, registry, reg_connection, 'zoom_info')