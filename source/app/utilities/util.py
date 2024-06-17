# SYSTEM
from .system.validation.is_directory    import is_directory
from .system.validation.is_file         import is_file
from .system.validation.is_flag         import is_flag
from .system.get_commands               import get_commands
from .system.file.get_files             import get_files
from .system.file.set_file              import set_file

# CUSTOM
from .custom.validation.is_extension    import is_extension
from .custom.debug.view_arguments       import view_arguments

class Util:

    def __init__ (  ): pass

    ####    SYSTEM  ########################################

    # VALIDATION

    def is_directory       ( path )                                 : return is_directory       ( path )

    def is_file            ( path,   type = None )                  : return is_file            ( path, type )

    def is_flag            ( string, flag = '-'  )                  : return is_flag            ( string, flag )

    # COMMAND

    def get_commands       ( commands )                             : return get_commands       ( commands )

    # FILE

    def get_files          ( path, type, omissions = '' )           : return get_files          ( path, type, omissions )

    def set_file           ( source, destination )                  : return set_file           ( source, destination )

    ####    CUSTOM  ########################################

    # VALIDATION

    def is_extension       ( line, list )                           : return is_extension       ( line, list )

    # DEBUG

    def view_arguments     ( arguments )                            : return view_arguments     ( arguments )
