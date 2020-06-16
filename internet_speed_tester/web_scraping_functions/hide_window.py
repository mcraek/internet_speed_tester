# === Import dependencies ===

# Custom

from internet_speed_tester.misc_functions import output_progress

# 3rd party

import win32gui  # (installed with pip install pywin32)


def window_enum_handler(hwnd, all_windows):

    # Enumerate / return all windows matching window_name

    window_name = 'WebDriver - Internet Explorer'
    window_text = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)

    if window_text.find(window_name) >= 0:

        all_windows.append((hwnd, window_text, class_name))


def hide_ie_window(args, log_name):

    # Hide Internet Explorer window

    try:
        
        message = 'Attempting to hide IE window...'
        output_progress(args, message, log_name)

        all_windows = []
        win32gui.EnumWindows(window_enum_handler, all_windows)

        for hwnd, text, class_name in all_windows:

            win32gui.ShowWindow(hwnd, False)

        return True

    except Exception as e:

        message = 'Unable to hide IE window. Proceeeding with test. Error message: ' + str(e)
        output_progress(args, message, log_name)

        return False
