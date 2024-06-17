import sys

from utilities.util     import Util
from core.markdown2json import Markdown2Json

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		Markdown2Json ( arguments )


main ( sys.argv )
