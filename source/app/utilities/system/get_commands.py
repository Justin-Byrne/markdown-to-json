import os

from .parse_commands 			import parse_commands

from .validation.is_file      	import is_file
from .validation.is_directory 	import is_directory

ERROR = -1

def get_commands   ( commands ):

	arguments = parse_commands ( commands )


	if arguments [ 'help_menu' ]:

		menu = [
			'Markdown to JSON converter for jsdoc-to-markdown output\n\n'
			'python3 md2json.py {<source>} [<destination>] [flags]\n\n'
			'PATHS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n\n'
			'source:\t\tDirectory of JSDoc markdown file(s)\n\n'
			'    usage:\t    "../jsdoc-to-markdown"\n\n'
			'destination:\tDirectory of JSON output\n\n'
			'    usage:\t    "../markdown-to-json"\n\n'
			'FLAGS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n\n'
			'-h, --help\tDisplay this help menu\n\n'
			'    usage:\t    --help\n'
		]

		for line in menu:

			print ( line )


		return ERROR;


	if arguments [ 'source' ] == None: 																# CHECK WHETHR A SOURCE IS PRESENT

		print ( ' >> [ERROR] Md2Json.py\n\t~ Requires a single source !' )

		return ERROR


	if arguments [ 'source' ] != None and arguments [ 'destination' ] == None: 						# IF ONLY SOURCE IS PRESENT MIRROR AS DESTINATION

		if arguments [ 'source' ] [ len ( arguments [ 'source' ] ) - 1 ] == '/':

			arguments [ 'source' ] = arguments [ 'source' ] [ :-1 ]


		if is_directory ( arguments [ 'source'] ):

			arguments [ 'destination' ] = f"{arguments [ 'source' ]}"

		elif is_file ( arguments [ 'source' ], None ):

			arguments [ 'destination' ] = f"{os.path.dirname ( arguments [ 'source' ] )}"


	return arguments
