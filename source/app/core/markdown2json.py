import os
import subprocess
import json

from utilities.util                         import Util

class Markdown2Json:

    def __init__( self, arguments ):

        ####    GLOBALS     ################################

        self.arguments = arguments

        self.files     = [ ]

        self.JSON      = { }

        ####    INITIALIZATION    ##########################

        self.init ( )

    ####    INITIATORS  ########################################################

    def init ( self ):

        self.get_files ( )

        self.compile   ( )

        self.save_json ( )

    ####    FUNCTIONS     ######################################################

    def get_files ( self ):

        source = self.arguments [ 'source' ];


        if ( Util.is_file ( source ) ):                     # If: file

            self.files.append ( source )


        if ( Util.is_directory ( source ) ):                # If: directory

            self.files = Util.get_files ( source, '.md' )


    def compile ( self ):

        for file in self.files:

            name = os.path.basename ( file ).replace ( '.md', '' )


            with open ( file, 'r' ) as reader:

                self.JSON [ name ] = reader.read ( )


    def save_json ( self ):

        FILE = f"{self.arguments [ 'destination' ]}/md2json.js"


        if Util.is_file ( FILE, None ):

            subprocess.run ( f'rm -f {FILE}', shell = True )

        else:

            directory = os.path.dirname ( FILE )


            if Util.is_directory ( directory ) is False:

                os.makedirs ( directory )


        with open ( FILE, 'w' ) as writer:

            writer.write ( 'let md2json =\n' )

            writer.write ( str ( json.dumps ( self.JSON, indent = 4 ) ) )



