#-----------------------------------
# Imports
#-----------------------------------

from .plci_core_data_type import DataType
from typing import Any

#-----------------------------------
# Class
#-----------------------------------

class Data : 
    """Est l'objet contenant les données transité par les signaux."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, data_type_ : DataType, value_ : Any = None) :

        self._data_type = data_type_   

        if value_ is None :
            self._value = self._data_type.default_value()
        
        else :
            self._value = value_

    # -------------
    # Properties
    # -------------

    @property
    def data_type (self) -> DataType : 
        """Permet de récuperer le type de la donnée."""
        return self._data_type

    @property
    def value (self) -> Any :
        """Permet de récuperer la valeur actuelle."""
        return self._value

    def __str__ (self) -> str :
        """Permet de récuperer la données sous la forme d'un string."""
        return "Data [" + str(self.data_type) + " | value : " + str(self.value) + "]" 
