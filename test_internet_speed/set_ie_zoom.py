'''

						//----------// LICENSING //----------//

			This file is part of the test_internet_speed program and is free software:
			you can redistribute it and/or modify it under the terms of the
			GNU General Public License as published by the Free Software Foundation,
			either version 3 of the License, or (at your option) any later version.
			This program is distributed in the hope that it will be useful,
			but WITHOUT ANY WARRANTY; without even the implied warranty of
			MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
			GNU General Public License for more details.
			You should have received a copy of the GNU General Public License
			along with this program. If not, see <https://www.gnu.org/licenses/>.

						//----------// LICENSING //----------//


	Description: 	The Selenium module for this project used to control Internet Explorer requires IE to be
                    set to a 100% zoom value in order to properly parse / interact with webpages.

                    This value is controlled through the ZoomFactor DWORD registry key within the HKCU hive.

                    In the context of this program, this function is used to first obtain the original value
                    this was set to for IE, change it to 100% for Selenium functionality, then change it
                    back to the original value when the program completes, or exits in error.
					
'''

def set_ie_zoom(arguments_received, log_name, option,zoom_value = 100000): # 100000 is the decimal equivalent of 100% for the DWORD reg key this edits

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import		winreg	    # Allows modifying registry key value for HKCU to ensure IE Browser zoom level 
						    # is set to 100% (Selenium requires this)

    import      sys         # Allows terminating program in the event of an error w/ exit()

    # Functions built as part of this project

    from        output_progress     import      output_progress     # Prints to console as well as debug log file when -v or -d options are specified

    
    # ============================== Begin Function ============================== #

    # Define Registry key location & name

    ie_key_location = r'Software\Microsoft\Internet Explorer\Zoom'
    zoom_key_name = 'ZoomFactor'

    # Open up root key location in registry, full access & Define Key name for Editing

    try:

        message = 'Attempting to obtain write access to registry key within HKCU at for reading / setting IE zoom value' + ie_key_location
        output_progress(arguments_received, message, log_name)

        ie_zoom_key_access = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ie_key_location, 0, winreg.KEY_ALL_ACCESS)

    except:

        message = 'Unable to open the registry key. Terminating program.'
        output_progress(arguments_received, message, log_name)
        sys.exit()

    # Return original key value

    if option == 'get_original_value':

        try:

            message = 'Attempting to obtain original value of the ' + zoom_key_name + ' registry key for returning to this after program completion'
            output_progress(arguments_received, message, log_name)

            ie_original_zoom = (winreg.QueryValueEx(ie_zoom_key_access, zoom_key_name))[0] # Access decimal (not hex) value with [0], [1] would access hex value
            return ie_original_zoom

        except:

            message = 'Unable to find key value. Terminating program.'
            output_progress(arguments_received, message, log_name)
            sys.exit()

    # Modify zoom level key, default to 100%

    if option == 'set_zoom':

        try:

            message = 'Attempting to modify the value of the ' + zoom_key_name + ' registry key to ' + str(zoom_value)
            output_progress(arguments_received, message, log_name)

            winreg.SetValueEx(ie_zoom_key_access, zoom_key_name, 1, winreg.REG_DWORD, zoom_value) # This modifies the decimal value of the DWORD key

        except:

            message = 'Unable to modify the key value. Terminating program.'
            output_progress(arguments_received, message, log_name)

            sys.exit()
	
	# Close Registry Key Access

    message = 'Removing write access to the registry at ' + ie_key_location + '\n'
    output_progress(arguments_received, message, log_name)

    winreg.CloseKey(ie_zoom_key_access) # Close off access to key (reopened later when changing it back to original zoom setting)
