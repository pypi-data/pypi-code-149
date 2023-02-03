#-----------------------------------
# Imports
#-----------------------------------

from muphyn.packages.core.plci_core_data_type import DataType

#-----------------------------------
# Classs
#-----------------------------------

class AbstractSignalModel : 
    """Est la classe abstraite commune aux signaux typés dans l'interface."""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, data_type : DataType) :

        self._data_type : DataType = data_type

    # -------------
    # Properties
    # -------------

    @property
    def data_type (self) -> DataType :
        """Permet de récuperer le type de l'élément."""
        return self._data_type

    @data_type.setter
    def data_type (self, data_type_ : DataType) -> None :
        """Permet de modifier le type de l'élément."""
        self._data_type = data_type_
        
    @property
    def is_connected_to_input (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""
        ...