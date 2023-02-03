#-----------------------------------
# Imports
#-----------------------------------

from typing import List

from muphyn.packages.interface.graphical_actions.abstract_graphical_action import AbstractGraphicalAction

#-----------------------------------
# Class
#-----------------------------------

class ActionsHolder : 
    """Est la classe permettant de lister les actions réalisée."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        self._undo_list : List[AbstractGraphicalAction] = []
        self._redo_list : List[AbstractGraphicalAction] = [] 

    # -------------
    # Properties
    # -------------

    @property
    def undo_count (self) -> int :
        """Permet de récuperer le nombre d'actions contenues dans la liste des actions à défaire."""
        return self._undo_list.__len__()

    @property
    def redo_count (self) -> int :
        """Permet de récuperer le nombre d'actions contenues dans la liste des actions à refaire."""
        return self._redo_list.__len__()

    @property
    def last_action (self) -> AbstractGraphicalAction:
        """Permet de récuperer la dernoère action "done"."""
        
        if len(self._undo_list) == 0 :
            return None

        return self._undo_list[0]

    # -------------
    # Methods
    # -------------

    def clear (self) :
        """Permet de vider les listes d'actions."""
        
        self._undo_list.clear()
        self._redo_list.clear()

    def undo (self) :
        """Permet de réaliser la dernière action contenue dans la liste."""

        if len(self._undo_list) > 0 :

            action = self._undo_list[0]
            action.undo()
            self._redo_list.insert(0, action)
            self._undo_list.remove(action)


    def redo (self) :
        """Permet de re-réaliser la dernière action qui a été dé-faite."""

        if len(self._redo_list) > 0 :

            action = self._redo_list[0]
            action.do()
            self._undo_list.insert(0, action)
            self._redo_list.remove(action)
    
    def append (self, action : AbstractGraphicalAction) : 
        """Permet d'ajouter une action dans la liste."""

        self._undo_list.insert(0, action)
        self._redo_list.clear()

    