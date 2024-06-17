import os
import re

def get_files ( path, type, omissions = '' ):

	result = [ ]


	for ( root, dirs, file ) in os.walk ( path ):

		for entry in file:

			record = f"{root}/{entry}"


			if type in entry:

				result.append ( record )

			else:

				continue


	return result
