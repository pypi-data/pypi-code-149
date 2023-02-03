#-----------------------------------
# Imports
#-----------------------------------

from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams

#-----------------------------------
# Class
#-----------------------------------

class SchedulerModel :
    """Est le model de données pour l'éditeur des planificateurs."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, library : str, name : str, params : SchedulerParams) :

        self._library : str = library
        self._name : str = name
        self._params = params

    # -------------
    # Properties
    # -------------
    @property
    def completeName(self) -> str:
        return f"{self._library}.{self._name}"
    
    @property
    def library (self) -> str :
        """Permet de récuperer le bibliothèque dans laquelle se trouve le planificateur."""
        return self._library
    
    @library.setter 
    def library (self, library_ : str) -> None :
        """Permet de modifier la bibliothèque dans laquelle se trouve le planificateur."""
        self._library : str = library_

    @property
    def name (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return self._name
    
    @name.setter
    def name (self, name_ : str) -> None :
        """Permet de modifier le nom du planificateur."""
        self._name = name_

    @property
    def params (self) -> SchedulerParams :
        """Permet de récuperer les paramètres du planificateur."""
        return self._params
    
    @params.setter
    def params (self, params_ : SchedulerParams) -> None :
        """Permet de modifier les paramètres du planificateur."""
        self._params = params_ 