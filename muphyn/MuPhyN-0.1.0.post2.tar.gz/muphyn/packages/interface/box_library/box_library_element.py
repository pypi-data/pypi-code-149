#-----------------------------------
# Imports
#-----------------------------------

import enum
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData
from muphyn.packages.interface.box_library.library_element import LibraryElement

class BoxLibraryElementRole(enum.IntEnum):
    BOX_DATA = 1

#-----------------------------------
# Class
#-----------------------------------

class BoxLibraryElement (LibraryElement) :

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_data : AbstractBoxData) :
        LibraryElement.__init__(self, box_data.box_name)
        
        self._box_data : AbstractBoxData = box_data

    # -------------
    # Properties
    # -------------

    @property
    def box_data (self) -> AbstractBoxData :
        """Permet de récuperer les données de la box à instancier."""
        return self._box_data
