#-----------------------------------
# Imports
#-----------------------------------

from typing import Dict

from .box_library_data import AbstractBoxData

#-----------------------------------
# Class
#-----------------------------------

class AbstractBoxLibraryImporter :
    """Est la classe abstraite commune permettant de charger des boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def import_box (self, path : str, file_name : str, absolute_yaml_file : str, boxes : Dict[str, AbstractBoxData]) -> Dict[str, AbstractBoxData]:
        """Est la méthode pour charger des boxes depuis des fichiers."""
        raise(NotImplementedError(f"{type(self).__name__}.import_box() not implemented yet"))