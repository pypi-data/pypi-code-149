#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, Generic, Iterator, Type, TypeVar, List

from muphyn.packages.core.utils.log_manager import LogManager

#-----------------------------------
# Generic Type
#-----------------------------------

T = TypeVar('T', bound = Callable)

#-----------------------------------
# Class
#-----------------------------------

class ModelsEvent (Generic[T]) :
    """Est la classe qui permet de contenir des listeners de toute sorte."""

    # -------------
    # Contructors
    # -------------

    def __init__(self) -> None:
        super().__init__()

        self._list : List[T] = []

    # -------------
    # Methods
    # -------------

    def __iter__ (self) -> Iterator[Type[T]] :
        """Permet de récuperer un itérateur pour boucler sur tous les éléments du tableau."""
        return self._list.__iter__()

    def __add__ (self, value) -> None :
        """Permet d'ajouter un événement."""

        if value is None :
            return
            
        if isinstance(value, T.__bound__) :
            self._list.append(value)

    def __sub__ (self, value) -> None :
        """Permet de supprimer un événement."""

        if value is None : 
            return

        if isinstance(value, type(T)) :
            self._list.remove(value)

    def clear (self) -> None :
        """Permet de supprimer tous les événements."""
        self._list.clear()

    def __len__ (self) -> int : 
        """Permet de récuperer la taille de la liste des événements."""
        return self._list.__len__()

    def __getitem__ (self, key : int) -> Type[T] :
        """Permet de récuperer l'événement à l'index demandé."""
        return self._list.__getitem__(key)
    
    def __setitem__ (self, key : int, value : Type[T]) -> None :
        """Empèche une erreur et ne fait rien en cas de tentative d'appel de la méthode."""
        LogManager().error('model event set item does nothing !!!')

    def __contains__ (self, item : Type[T]) -> bool :
        """Permet de savoir si l'événement se trouve déjà dans la liste."""
        return self._list.__contains__(item)