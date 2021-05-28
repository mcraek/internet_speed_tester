#!../bin/env python

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


	File name: test_internet_speed.py
	Author: KM
	Date created: 2019 - 06 - 09
	Python Version: 3.7

	Description:	Used in combination with the Selenium 3rd party module for navigating to and interacting with fast.com
					Pulls download / upload Internet speeds from the site and returns them to several locations based on
					arguments passed to the program:

					To Debug log files,
					To separate download / upload text files
					To console
						
'''

def test_internet_speed():

	# //--- Debug --- // #

		# Copy and paste the following line into a PoSh terminal to test running the program using your virtual environment
		# Accepts arguments as well:
		# & "D:\Scripts\Python\test_internet_speed\bin\env\Scripts\python.exe" "D:\Scripts\Python\test_internet_speed\test_internet_speed\test_internet_speed.py" -v True

	# //--- Debug --- // #

	# ============================== Import Dependencies ============================== #

	# Built-in functions

	from	datetime	import		datetime		# Used for logging current date / time of check
	import							subprocess		# Used for hiding console for --silent option								

	# Functions built as part of this project

	from	check_arguments			import		check_arguments			# Allows parsing / checking arguments passed to program from commandline

	from 	test_site_connection 	import 		test_site_connection 	# Checks connections to websites using ICMP echo
	from	set_ie_zoom				import		set_ie_zoom				# Checks / sets the ZoomFactor IE HKCU registry key value for Selenium functionality
	from	parse_website			import		parse_website			# Used for controlling IE web browser with Selenium
	from	print_msg				import		print_msg				# Print messages to console with auto time.sleep
	from	output_progress			import		output_progress			# Prints to console as well as debug log file when -v or -d options are specified
	from	output_results			import		output_results			# Outputs speed test results dependent on args passed to program: --debug, --outfileresults
	from    terminate_web_session   import      terminate_web_session	# Used for terminating program gracefully or exiting in the event of a fatal error
	from	hide_window				import		hide_window				# Used for hiding console / IE browser

	#  ============================== Check / Handle arguments passed to program, also set default values here for parameters if necessary  ============================== #

	arguments_received = vars(check_arguments()) 	# Parse arguments submitted to program and store them into a variable
													# This is used to pass the arguments to further commands below.
													# If the user executes the program with no arguments passed. This will
													# set default values.
													# Important note: Do not pass sys.argv to argparse. It automatically
													# handles this, and passing sys.argv just confuses / breaks things with it

	# Store / format current date / time

	date = datetime.now()
	date = date.strftime("%d-%m-%Y %H-%M")
	log_name = date + '-log.txt' # Set log file name for program results

	# Set variable defaults

	debug = 'false'
	output_file = 'true'
	verbose = 'false'
	silent = 'false'
			
	# --------------- Output starting messages to user / set initial variables for program --------------- #

	output_progress(arguments_received, '------------------- Internet Speed Test Checker v. 0.5 -------------------\n', log_name)
	output_progress(arguments_received, 'Starting speed test timestamped: ' + str(date + '\n'), log_name)

	# --------------- Reset variables to values explicitly passed to program /  hide console if silent option passed  --------------- #

	if arguments_received['Debug'] == 'true':
		
		debug = 'true'
		print_msg('Debug logging enabled. Verbose output will be saved to ' + log_name + ' file within program directory')

	if arguments_received['OutputFiles'] == 'true':

		output_file = 'true'
		print_msg('Results will be output to separate Download / Upload speed vlaue text files within program directory')

	if arguments_received['Verbose'] == 'true':

		verbose = 'true'
		print_msg('Verbose option specified. Program progress will be output to console')

	if arguments_received['Silent'] == 'true':

		hide_window('test_internet_speed.exe')


	# ============================== Begin Function ============================== #

	# --------------- Test connection to the site --------------- #

	site = 'fast.com'
	connection_successful = test_site_connection(site)
	message = 'Testing connection to ' + site

	output_progress(arguments_received, message, log_name)

	if connection_successful == False: # Access return object from test above after moving it to its own function

		message = 'Connection to ' + site + ' failed. Check your connection. Website may also be down...'
		output_progress(arguments_received, message, log_name)
		sys.exit()

	else:

		message = site + ' appears to be online and reachable\n'
		output_progress(arguments_received, message, log_name)


	#  --------------- Set IE zoom level to 100% (Selenium requires this in order to identify elements correctly) --------------- #

	ie_original_zoom = set_ie_zoom(arguments_received, log_name, 'get_original_value') # First store the original zoom value

	message = 'Verifying Internet Explorer zoom level set to 100%'
	output_progress(arguments_received, message, log_name)

	if ie_original_zoom != 100000:

		message = 'Internet Explorer zoom level is not 100%. This will be configured and reset back to orginal setting after program completion...\n'
		output_progress(arguments_received, message, log_name)
		set_ie_zoom(arguments_received, log_name, 'set_zoom') # Set zoom to 100%
									

	#  ---------------  Start session to site with Selenium  --------------- #

	# Start Selenium web session

	session = parse_website(log_name, arguments_received, 'initialize', ie_original_zoom) # Start an IE web session

	# Navigate to fast.com with our session

	parse_website(log_name, arguments_received, 'get_site', ie_original_zoom, site, session)

	# Allow site to load before proceeding

	parse_website(log_name, arguments_received, 'wait', ie_original_zoom, site, session)

	#  ---------------  Pull Download / Upload Speed Values  --------------- #

	# Pull download speed by getting the text of the download speed element

	downstream_value = parse_website(log_name, arguments_received, 'get_download_speed', ie_original_zoom, site, session)

	# Pull upload speed by clicking show more info link / grabbing value after test completes

	upstream_value = parse_website(log_name, arguments_received, 'get_upload_speed', ie_original_zoom, site, session)

	#  ---------------  Output Results of Speed Test  --------------- #

	# Results will output to console, and separate debug / speed test results files depending on
	# args passed to program: --debug, --outfileresults

	output_results(arguments_received, date, log_name, str(downstream_value), str(upstream_value))

	#  ---------------  Terminate IE Session to Site  --------------- #

	terminate_web_session(arguments_received, log_name, 'graceful', ie_original_zoom, session)

	#  ---------------  Return IE zoom level back to original setting / close out registry access  --------------- #

	set_ie_zoom(arguments_received, log_name, 'set_zoom', ie_original_zoom)

# Execute the program

test_internet_speed()