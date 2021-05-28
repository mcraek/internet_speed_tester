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


    Description:    This function is used for terminating the IE session started with fast.com
                    both at time of successful program completion, and in the event the
                    program reaches a non-recoverable error




'''


def terminate_web_session (arguments_received, log_name, option, ie_original_zoom, browser_instance):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import      sys         # Allows terminating program in the event of an error w/ exit()

    # 3rd party functions installed to project Python executable

    from 		selenium        import	webdriver       # Used for terminating web browser session

    # Functions built as part of this project

    from        output_progress     import      output_progress     # Prints to console as well as debug log file when -v or -d options are specified
    from        set_ie_zoom         import      set_ie_zoom         # Used for resetting zoom level of Internet Explorer back to what it was


    # ============================== Begin Function ============================== #

    # Terminate IE Session

    if option == 'graceful':

        message = 'Program complete, terminating IE instance\n'
        output_progress(arguments_received, message, log_name)

        browser_instance.close()

    elif option == 'error':

        message = ' Fatal error encountered. Terminating program.'
        output_progress(arguments_received, message, log_name)

        browser_instance.close()

    # Reset IE Zoom level back to its original setting

    set_ie_zoom(arguments_received, log_name, 'set_zoom', ie_original_zoom)

    # Exit program

    sys.exit()