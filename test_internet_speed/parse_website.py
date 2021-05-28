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



	Description: 	Custom-built to work with fast.com where site is controlled / parsed with the 3rd party Selenium
                    browser utility for Python.

                    HTML elements are parsed on the page, and at several points the website is allowed to fully load
                    either waiting for certain HTML elements to have a specific class, or in one instance, become
                    clickable

                    This function is heavily dependent on specific HTML element ID names / classes at fast.com. 
                    In the event any of these change by the site developers, this should hopefully be caught and 
                    output to console / debug logs when using the --verbose True, or --debug True options passed 
                    to main program.

                    Checks for each HTML element / class name are performed using the check_html_element function
                    which will throw an error / exit the program if an HTML element specifically referenced by
                    this program no longer exists or is changed.
					
'''

def parse_website(log_name, arguments_received, option, ie_original_zoom, site = 'fast.com', browser_instance = 'not_set'):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import                              sys                 # Allows terminating program in the event of an error w/ exit()
    from		decimal     import	    Decimal				# Allows rounding to two decimal places / performing math functions
    import                              time                # Allows forcing a pause with sleep function

    # 3rd party functions installed to project Python executable

    from		pynput.keyboard					import	    Key, Controller		        # Allows simulating key presses / hotkeys (used for sending Alt+Space+N for minimizing 
                                                                                        # IE Browser window w/ Selenium)

    from 		selenium						import	    webdriver                   # Allows controlling web browser, same with next two below this
    from 		selenium.webdriver.common.by 	import 	    By                          
    from		selenium.webdriver.support.ui 	import 	    WebDriverWait
    from 		selenium.webdriver.support 		import 	    expected_conditions as EC   # Allows confirming sites have loaded
    from        selenium.webdriver.ie.options   import      Options                     # Allows ignoring IE Protected Zone settings

    # Functions built as part of this project

    from		get_path		        import	    get_path	                # Returns path of resources script references such as drivers (works in production 
                                                                                # when program is an exe / Also in Dev)

    from        convert_speed           import      convert_speed               # Converts download / upload speeds from mbps to MB / s
  
    from        print_msg               import      print_msg                   # Allows outputting text to console as program continues
    from        check_html_element      import      check_html_element          # Allows seraching for HTML elements to see if they still exist
    from        output_progress         import      output_progress             # Prints to console as well as debug log file when -v or -d options are specified
    from        terminate_web_session   import      terminate_web_session       # Used for terminating program gracefully or exiting in the event of a fatal error
    from        hide_window             import      hide_window


    # ============================== Begin Function ============================== #


    # --------------- Start IE Web Session  --------------- #

    if option == 'initialize':

        message = 'Establishing Internet Explorer session...'
        output_progress(arguments_received, message, log_name)

        # Open IE window, return browser instance back to program to pass to other functions

        try:

            ie_driver_path = get_path('test_internet_speed/drivers/IEDriverServer.exe')     # Define path to Internet Explorer web driver for Selenium to use
                                                                                            # Use get_path to return path of file depedning on if program is run
                                                                                            # in production as a single exe, or in developemnet by calling the 
                                                                                            # script

            ie_driver = get_path('test_internet_speed\\drivers\\IEDriverServer.exe')        # Define driver location for Python to use

            # Define option specifying Selenium should not require IE to have Protected Mode
            # enabled on all zones within Internet Options/Security, otherwise program errors
            # out if run as an exe

            ie_options = Options()
            ie_options.ignore_protected_mode_settings = True
            
            ie = webdriver.Ie(executable_path=ie_driver, options=ie_options)                # Initializes browser

            # Hide IE Window

            hide_window('WebDriver - Internet Explorer')    # Name of window to hide confirmed by looking at Task Manager, expanding IE when site was loaded
                                                            # and looking at the name of the tab

            message = 'IE session started\n'
            output_progress(arguments_received, message, log_name)

            return ie       # Returns browser object to main program so it can be passed again to this function

        except:
            
            message = 'Error starting Selenium Internet Explorer option. Cannot locate IEDriverServer.exe within ' + ie_driver_path
            output_progress(arguments_received, message, log_name)

            sys.exit()
    

    # --------------- Navigate to website & Minimize IE Window  --------------- #

    elif option == 'get_site':

        message = 'Navigating to ' + site + '...\n'
        output_progress(arguments_received, message, log_name)

        try:

            browser_instance.get('http://www.' + site) # Navigate to the website
        
        except:

            message = 'Unable to navigate to ' + site
            output_progress(arguments_received, message, log_name)

            terminate_web_session(arguments_received, log_name, 'error', ie_original_zoom, browser_instance)
    
        


    # --------------- Allow site to fully load  --------------- #

    elif option == 'wait':

        # There is an HTML element with an ID of "show-more-details-link" that displays 
        # when the speed test is complete. This is a button that becomes clickable when 
        # the page has loaded. Here we wait a maximum of 120 seconds for the page to load 
        # before throwing an error. The page is considered fully loaded when the button 
        # is clickable
	
        # Handy documentation on Selenium / confirming pages are loaded (there are many 
        # different ways: https://selenium-python.readthedocs.io/waits.html#explicit-waits)

        # Confirm the HTML element still exists

        site_loaded_element_id = 'show-more-details-link'
        
        # Wait for page to finish loading

        message = 'Waiting for site to fully load...'
        output_progress(arguments_received, message, log_name)

        check_html_element(arguments_received, log_name, site_loaded_element_id, browser_instance, ie_original_zoom)

        try:

            element = WebDriverWait(browser_instance, 120).until(

                EC.element_to_be_clickable( (By.ID, site_loaded_element_id) )

            )

            message = 'The page has fully loaded\n'
            output_progress(arguments_received, message, log_name)

        except:

            message = 'Failed to verify site has loaded. Check the ' + site_loaded_element_id + ' HTML element id still becomes clickable when site is fully loaded.'
            output_progress(arguments_received, message, log_name)

            terminate_web_session(arguments_received, log_name, 'error', ie_original_zoom, browser_instance)


    # --------------- Get the download speed  --------------- #

    elif option == 'get_download_speed':

        message = 'Obtaining download speed value...'
        output_progress(arguments_received, message, log_name)

        # First, check HTML element used for obtaining speed still exists, then pull the value

        down_html_id = 'speed-value'
        check_html_element(arguments_received, log_name, down_html_id, browser_instance, ie_original_zoom)

        down_speed_value = browser_instance.find_element_by_id(down_html_id).text

        # Convert value to MB / s

        message = 'Download speed found. Converting this from mbps to MB / s\n'
        output_progress(arguments_received, message, log_name)

        down_speed_value_converted = convert_speed(down_speed_value)
        return down_speed_value_converted


    # --------------- Get the upload speed  --------------- #

    elif option == 'get_upload_speed':

        message = 'Obtaining upload speed value...'
        output_progress(arguments_received, message, log_name)

        # Check HTML link element used for starting upload speed test still exists

        upload_link_id = 'show-more-details-link'
        check_html_element(arguments_received, log_name, upload_link_id, browser_instance, ie_original_zoom)

        # Store text from link. This is used to click the link

        upload_link_text = (browser_instance.find_element_by_id(upload_link_id)).text

        # Pull upload speed by clicking show more info link and grabbing the value from there

        try:
            
            upload_link = browser_instance.find_element_by_link_text(upload_link_text)
            upload_link.click()
        
        except:

            message = 'Failed to start upload test by clicking link with HTML ID: ' + upload_link_id + ' with text contents of: ' + upload_link_text + '. Perhaps something has changed in the HTML for this'
            output_progress(arguments_received, message, log_name)

            terminate_web_session(arguments_received, log_name, 'error', ie_original_zoom, browser_instance)

        # Confirm upload speed has finished calculating before pulling value

        message = 'Waiting for upload test to complete...'
        output_progress(arguments_received, message, log_name)

        # First define a class which can be used to create an object from an HTML element passed to it
        # from here we can associate / run particular functions against the object passed and the attributes
        # we define. Source on waiting for objects to change css class: 
        # https://pymbook.readthedocs.io/en/latest/classes.html

        class element_has_css_class(object):
            
            # __init__ must be called to create the object from the passed element and define attributes for it

            def __init__(self, locator, css_class):

                self.locator = locator
                self.css_class = css_class

            # Now that the object is defined, the following finds the HTML element we passed to the class
            # and checks if it has a particular CSS class, otherwise returns false

            def __call__(self, browser_instance):

                element = browser_instance.find_element(*self.locator)   # Finding the referenced element

                if self.css_class in element.get_attribute("class"):

                    return element
                
                else:

                    return False

        # Wait until an element with id='myNewInput' has class 'myCSSClass'

        try:

            upload_html_id = 'upload-value'
            check_html_element(arguments_received, log_name, upload_html_id, browser_instance, ie_original_zoom) # Check the element still exists

            # Define parameters which control maximum wait time for CSS class to be applied to the element / which CSS class we are expecting

            css = 'extra-measurement-value-container succeeded' # By inspecting HTML elements on the page in Dev mode, it was found the upload-value HTML element gets this class when the page
                                                                # is fully loaded after running the Upload speed test
            
            wait = WebDriverWait(browser_instance, 120) # Here we define the maximum wait time WebDriver will allow before throwing an error and assuming a timeout has occurred
            
            element = wait.until(element_has_css_class((By.ID, upload_html_id), css))


        except:

            message = 'Failed to verify upload speed test complete by waiting for the ' + upload_html_id + ' to have a CSS class of ' + css + '. Verify this class still applies to the element once the upload speed test is completed.'
            output_progress(arguments_received, message, log_name)

            terminate_web_session(arguments_received, log_name, 'error', ie_original_zoom, browser_instance)

        # Pull the upload speed value by grabbing the text value of the upload HTML element 

        upload_speed_value = browser_instance.find_element_by_id(upload_html_id).text

        # Convert value to MB / s
        
        message = 'Upload speed found. Converting this from mbps to MB / s\n'
        output_progress(arguments_received, message, log_name)

        upload_speed_value_converted = convert_speed(upload_speed_value)
        return upload_speed_value_converted


