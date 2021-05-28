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



	Description: 	Receives / validates arguments passed to the main program and sets defaults in the event
                    certain arguments are not passed to the program.

                    Arguments passed are case insensitive
					
'''

def check_arguments():

    # ============================== Import Built-in Dependencies ============================== #

    import argparse # Used for parsing arguments passed to program


    # ============================== Begin Function ============================== #

    # Specify valid arguments for program and set default values accordingly.

    parser = argparse.ArgumentParser(description='Set options for the Internet speed test')

    parser.add_argument('-d', '--debug', dest='Debug', choices=['true','false'], type=str.lower,
                        help='if set to true, will output verbose logs including errors to same directory as program',
                        default='false')

    parser.add_argument('-of', '--outfileresults', dest='OutputFiles', choices=['true','false'], type=str.lower,
                        help='determines whether download / upload speeds are output to files within same directory as program for parsing',
                        default='false')

    parser.add_argument('-s', '--silent', dest='Silent', choices=['true','false'], type=str.lower,
                        help='if set to true, hides console and outputs results to text file in same directory as program. debug is not set to true automatially',
                        default='false')

    parser.add_argument('-v', '--verbose', dest='Verbose', choices=['true','false'], type=str.lower,    # Specifying type of str.lower converts user
                                                                                                        # arguments to lower case making their input
                                                                                                        # case insensitive
                        help='specify whether show verbose output to console', default='false')
    
    passed_arguments = (parser.parse_args())    # Validate arguments passed to program against above permitted arguments
                                                    # vars returns the arguments as a dictionary which can be parsed as key > value

    # Return validated arguments to main program so it can pass them to other functions that may use them

    return passed_arguments