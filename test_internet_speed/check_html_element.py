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

	Description:    Will check if an HTML element ID still exists on a web page. If it cannot find the element
                    program exits.
					
'''

def check_html_element(arguments_received, log_name, element_id, browser_instance, ie_original_zoom):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import                                      sys                 # Allows program exit function

    # 3rd party functions installed to project Python executable

    from 		selenium    	    import	    webdriver           # Allows finding HTML elements by ID via Selenium

    # Functions built as part of this project
    
    from        print_msg                   import      print_msg                   # Prints messages to console
    from        output_progress             import      output_progress             # Prints to console as well as debug log file when -v or -d options are specified
    from        terminate_web_session       import      terminate_web_session       # Used for terminating program gracefully or exiting in the event of a fatal error


    # ============================== Begin Function ============================== #

    try:

        message = 'Checking if HTML element ID ' + element_id + ' still exists...'
        output_progress(arguments_received, message, log_name)

        browser_instance.find_element_by_id(element_id)

    except:

        message = 'Unable to find HTML element. Perhaps site HTML coding has changed...'
        output_progress(arguments_received, message, log_name)

        terminate_web_session(arguments_received, log_name, 'error', ie_original_zoom, browser_instance)