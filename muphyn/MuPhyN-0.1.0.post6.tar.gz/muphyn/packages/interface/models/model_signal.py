#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, List, Any

#-----------------------------------
# Class
#-----------------------------------

class ModelSignal : 
    """Est la classe permettant de gérer des listeners de manière abstraite."""

    # -------------
    # Contructors
    # -------------

    def __init__ (self) : 
        self._slots : List[Callable] = []

    # -------------
    # Methods
    # -------------

    def emit (self, **kwargs : Any) :
        """Permet d'appeler chacun des slots avec les arguments passés."""

        for slot in self._slots : 
            slot(kwargs)

    def connect (self, slot_ : Callable) :
        """Permet d'ajouter le slot à la liste des slots."""

        if slot_ is None : 
            return

        if not(slot_ in self._slots) : 
            self._slots.append(slot_) 

    def disconnect (self, slot_ : Callable) :
        """Permet de supprimer le slot de la liste des slots."""

        if slot_ in self._slots :
            self._slots.remove(slot_)
    