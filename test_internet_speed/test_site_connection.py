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


	Description: 	Runs a ping test to a site passed to it.
                    Uses cmd.exe on Windows to perform the test, and as long as the output
                    of the ping test does not include 'Lost = 4' meaning all of the default
                    ping count Windows sends to a site are lost, will return True. 
                    
                    Otherwise returns false if all four pings are lost 
					
'''

def test_site_connection(site):

    # ============================== Import Built-in Dependencies ============================== #

    import subprocess # Allows running ping utility on Windows systems


    # ============================== Begin Function ============================== #

    # Run ping test to site received as argument

    ping_test = subprocess.run([ 'ping', site ], capture_output=True)
    ping_results = ping_test.stdout.decode() # This captures the std output of the ping command run by cmd.exe on Windows

    # Windows sends four echo requests by default. As long as all four are not lost, return True to indicate a successful connection

    if '%' in ping_results and 'Lost = 4' not in ping_results:  

        return True

    else:

        return False