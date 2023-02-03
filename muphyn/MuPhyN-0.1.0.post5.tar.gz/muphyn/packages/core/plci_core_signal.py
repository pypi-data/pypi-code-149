#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from .plci_core_data import Data
from .plci_core_data_type import DataType

#-----------------------------------
# Class
#-----------------------------------

class Signal :
    """Est la classe qui gère les différents signaux du diagramme."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, index_ : int, signal_type_ : DataType, default_value_ : Any, 
            name_: str = "", input_name: str = "", output_name: str = "") :

        self._index = index_
        self._signal_type = signal_type_
        self._data = Data(self._signal_type, default_value_)
        self._name = name_
        self._input_name = input_name
        self._output_name = output_name

    # -------------
    # Properties
    # -------------
    
    @property
    def index (self) -> int :
        """Permet de récuperer l'index."""    
        return self._index

    @property
    def signal_type (self) -> DataType :
        """Permet de récuperer le type de signal."""
        return self._signal_type
    
    @property
    def data (self) -> Data :
        """Permet de récuperer la donnée actuelle du signal."""
        return self._data

    @data.setter
    def data (self, data_ : Data) -> None : 
        """Permet de modifier la donnée interne du signal."""

        if (self._data.data_type == data_.data_type)  :
            self._data = data_
            return

    @property 
    def value (self) -> Any :
        """Permet de récuperer la valeur actuelle du signal."""
        return self._data.value

    @property 
    def name (self) -> str :
        """Permet de récuperer le nom du signal"""
        return self._name

    @name.setter
    def name (self, name_ : str):
        """Permet de modifier le nom du signal"""
        self._name = name_

    @property 
    def input_name (self) -> str :
        """Permet de récuperer le nom du signal"""
        return self._input_name

    @input_name.setter
    def input_name (self, new_input_name : str):
        """Permet de modifier le nom du signal"""
        self._input_name = new_input_name

    @property 
    def output_name (self) -> str :
        """Permet de récuperer le nom du signal"""
        return self._output_name

    @output_name.setter
    def output_name (self, new_output_name : str):
        """Permet de modifier le nom du signal"""
        self._output_name = new_output_name
        
    def __str__ (self) -> str :
        """Permet de retourner un string décrivant le signal."""
        return "Signal [ " + str(self.index) + " -> " + str(self._signal_type) + "]"