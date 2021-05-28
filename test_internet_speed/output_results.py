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


        Description:    Outputs download / upload speed values passed to it to separate text files in program directory.
                        Also outputs to console and debug logs as well.

                        Output is dependent on usage of the --outfiles and --debug options passed to main program
					
'''

def output_results(arguments_received, date, log_name, downstream_value, upstream_value):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import                                          os                     # Creates text file containing download / upload speeds

    # Functions built as part of this project

    from        output_progress         import          output_progress         # Writes to console / logfile depending on options passed to program
    from        print_msg               import          print_msg               # Writes to console only


    # ============================== Begin Function ============================== #

    # Output results to separate text files in program directory

    if arguments_received['OutputFiles'] == 'true':

        # Form filenames for download / upload speed files

        downspeed_name = date + '-DownstreamResults.txt'
        uploadspeed_name = date + '-UpstreamResults.txt'

        # Output download speed result to text file

        downspeed_file = open(downspeed_name,  'w')
        downspeed_file.write(downstream_value)
        downspeed_file.close()

        # Output upload speed result to text file

        uploadspeed_file = open(uploadspeed_name, 'w')
        uploadspeed_file.write(upstream_value)
        uploadspeed_file.close()

        message = 'Download / upload speeds saved to the following text files in the program directory: ' + '\n' + downspeed_name + '\n' + uploadspeed_name + '\n'
        (arguments_received, message, log_name)

# Output results to console, will output to debug file as well if --debug option used

    message = 'Speed test complete. Here are the results: ' + '\n\n' + 'Download speed (MB / s): '+ downstream_value + '\n' + 'Upload speed (MB / s): ' + upstream_value + '\n'
    print_msg(message)