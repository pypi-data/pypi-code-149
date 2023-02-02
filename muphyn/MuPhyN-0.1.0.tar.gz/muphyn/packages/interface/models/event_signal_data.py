#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

#-----------------------------------
# Class
#-----------------------------------

class EventSignalData :
    """Est la classe des événements véhiculés par les resizers."""

    # -------------
    # Contructors
    # -------------

    def __init__ (self, sender : Any, value : Any) :
        self._sender : Any = sender
        self._value : Any = value

    # -------------
    # Properties
    # -------------

    @property
    def sender (self) -> Any :
        return self._sender

    @property
    def value (self) -> Any :
        return self._value