import re
import os

from os.path 					import dirname, abspath, expanduser

def parse_commands ( commands ):

	#### 	GLOBALS 	####################################

	arguments = {
		'source':      None,
		'destination': None,
		'help_menu':   False
	}

	regexes = {
		'help_menu':  r'\s*-h\s*|\s*--help\s*',
		'locations':  r'(\/\w+[^\s*]+)',
	}

	#### 	FUNCTIONS 	####################################

	def check_command_line ( ):

		for i in range ( 1, len ( commands ) ):

			command = commands [ i ]


			for regex in regexes:

				if ( re.search ( regexes [ regex ], command ) ):

					match regex:

						case 'help_menu':

							arguments [ 'help_menu' ] = True

							break

						case 'locations':

							if arguments [ 'source' ] == None:

								arguments [ 'source' ] = command

							elif arguments [ 'destination' ] == None:

								arguments [ 'destination' ] = command


	#### 	LOGIC 		####################################

	check_command_line ( )


	return arguments
