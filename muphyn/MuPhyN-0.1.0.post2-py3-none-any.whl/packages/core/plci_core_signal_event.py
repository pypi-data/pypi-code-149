#-----------------------------------
# Imports
#-----------------------------------

from .plci_core_data import Data
from .plci_core_signal import Signal
from typing import Any

#-----------------------------------
# Class
#-----------------------------------

class SignalEvent :
    """Est la classe qui décrit le contenu d'un événement triggé par les boxes pour modifier les valeur des signaux."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, signal_ : Signal, box_ : Any, new_signal_data : Data) :
        self._signal = signal_
        self._box = box_
        self._last_signal_data = signal_.data
        self._new_signal_data = new_signal_data

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
    def last_signal_data (self) -> Data :
        """Permet de récuperer la donnée qui se trouvait sur le signal avant le changement."""
        return self._last_signal_data

    @property
    def last_signal_value (self) -> Data :
        """Permet de récuperer la valeur qui se trouvait sur le signal avant le changement."""
        return self._last_signal_data.value

    @property
    def new_signal_data (self) -> Data :
        """Permet de récuperer la nouvelle donnée."""
        return self._new_signal_data
    
    @property
    def new_signal_value (self) -> Any :
        """Permet de récuperer la nouvelle valeur."""
        return self._new_signal_data.value