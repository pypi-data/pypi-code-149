#-----------------------------------
# Imports
#-----------------------------------

from .plci_core_data import Data
from .plci_core_signal import Signal
from typing import Any

#-----------------------------------
# Class
#-----------------------------------

class SchedulerEvent :
    """Est la classe qui décrit le contenu d'un événement du planificateur pour modifier les entrées d'une box."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, signal_ : Signal, box_ : Any, new_signal_data : Data, timing_ : float, scheduler_ : Any) :
        self._signal = signal_
        self._box = box_
        self._new_signal_data = new_signal_data
        self._timing = timing_
        self._scheduler = scheduler_
    
    # -------------
    # Properties
    # -------------

    @property 
    def signal (self) -> Signal : 
        """Permet de récuperer le signal de l'événement."""
        return self._signal

    @property
    def box (self) -> Any :
        """Permet de récuperer la box de l'événement."""
        return self._box

    @property
    def new_signal_data (self) -> Data :
        """Permet de récuperer la nouvelle donnée."""
        return self._new_signal_data
    
    @property
    def new_signal_value (self) -> Any :
        """Permet de récuperer la nouvelle valeur."""
        return self._new_signal_data.value

    @property
    def timing (self) -> float :
        """Permet de récuperer le timing de l'événément."""
        return self._timing

    @property 
    def scheduler (self) -> Any :
        """Permet de récuperer le planificateur."""
        return self._scheduler

    @property 
    def step_time (self) -> float :
        """Permet de récuperer le pas de temps de la simulation."""
        return self._scheduler.step_time

    @property
    def stop_time (self) -> float :
        """Permet de récuperer le temps de fin de la simulation."""
        return self._scheduler.stop_time