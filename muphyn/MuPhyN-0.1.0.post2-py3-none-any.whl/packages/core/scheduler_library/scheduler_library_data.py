#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, Any
from ..plci_core_scheduler import Scheduler
from ..plci_core_scheduler_exception import SchedulerException

#-----------------------------------
# Class
#-----------------------------------

class SchedulerData : 
    """Est la classe commune des classes de données de bibliothèque."""

    # -------------
    # Constructors
    # -------------
    def __init__ (
            self, 
            scheduler_name : str, 
            scheduler_library : str,
            scheduler_method : Callable[[Scheduler], SchedulerException],
            creator : str,
            date_created : Any,
            version : float
        ) :
        
        self._scheduler_name : str = scheduler_name
        self._scheduler_library : str = scheduler_library
        self._scheduler_method : Callable[[Scheduler], SchedulerException] = scheduler_method
        self._creator = creator
        self._date_created = date_created
        self._version = version

    # -------------
    # Properties
    # -------------

    @property 
    def scheduler_name (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return self._scheduler_name

    @property
    def scheduler_library (self) -> str :
        """Pemet de récuperer la bibliothèque du planificateur."""
        return self._scheduler_library

    @property
    def scheduler_method (self) -> Callable[[Scheduler], SchedulerException] :
        """Permet de récuperer la méthode du planificateur."""
        return self._scheduler_method

    @property
    def creator (self) -> str :
        """Permet de récuperer le nom de la personne qui a créé le planificateur."""
        return self._creator

    @property
    def date_created (self) -> Any :
        """Permet de récuperer la date à laquelle le planificateur a été créée."""
        return self._date_created

    @property
    def version (self) -> float :
        """Permet de récuperer la version du planificateur."""
        return self.version

    # -------------
    # Methods
    # -------------
    
    def construct_scheduler (self) -> Scheduler :
        """Permet de générer un planificateur."""
        return Scheduler(self._scheduler_name, self._scheduler_method)

    def __str__ (self) -> str :
        """Permet de récuperer l'importeur de planificateur sous la forme de texte."""
        return self._scheduler_library + '.' + self._scheduler_name