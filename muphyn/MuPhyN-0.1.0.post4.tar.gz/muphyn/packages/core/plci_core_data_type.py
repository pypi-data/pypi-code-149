#-----------------------------------
# Import
#-----------------------------------

from enum import Enum
from typing import Any
    
#-----------------------------------
# Class
#-----------------------------------

class DataType(Enum) : 
    """Est l'enum qui décrit les types acceptés dans les signaux."""


    UNDIFINED = -1
    """Est le type qui définis un objet indéfinis."""

    STRING = 0,
    """Est le type qui définis un string."""

    INT = 1,
    """Est le type qui définis un entier."""

    FLOAT = 2,
    """Est le type qui définis un nombre à virgule flottante."""

    BOOLEAN = 3,
    """Est le type qui définis un boolean."""
    
    OBJECT = 4,
    """Est le type qui définis un objet."""

    ANYFILE = 5
    """Est le type qui définis un chemin vers un fichier existant ou non."""

    DIRECTORY = 6
    """Est le type qui définis un chemin vers un dossier existant."""

    EXISTINGFILE = 7
    """Est le type qui définis un chemin vers un fichier existant."""

    EXISTINGFILES = 8
    """Est le type qui définis une liste de chemins pointant chacun vers un fichier existant."""

    CHOICE = 9

    def __str__ (self) :
        """Permet de retourner le data type sous la forme d'un nom."""
        return self.name.lower()

    def default_value (self) -> Any :
        """Permet de récuperer la valeur par défaut des données suivant le type."""

        if self == DataType.STRING :
            return ""

        elif self == DataType.INT :
            return 0

        elif self == DataType.FLOAT :
            return 0.0

        elif self == DataType.BOOLEAN :
            return False

        elif self == DataType.ANYFILE :
            return ""

        elif self == DataType.DIRECTORY :
            return ""

        elif self == DataType.EXISTINGFILE :
            return ""

        elif self == DataType.EXISTINGFILES :
            return []

        elif self == DataType.CHOICE:
            return []
        
        else:
            return None


#-----------------------------------
# Functions
#-----------------------------------

def get_data_type (value) -> DataType :
    """Permet de retourner un data type suivant la valeur passé en paramètre."""
    if isinstance(value, str) :
        
        for type in DataType :
            if type.__str__() == value.lower() :

                return type

    elif isinstance(value, int) :
        return DataType[value]

    elif isinstance(value, DataType) : 
        return value
    
    return DataType.UNDIFINED