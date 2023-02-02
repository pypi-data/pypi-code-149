#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from muphyn.packages.interface.graphical_actions.abstract_graphical_action import AbstractGraphicalAction

#-----------------------------------
# Functions
#-----------------------------------

def _lst_contains_element (lst : QListWidget, el : str) -> bool :
    """Est la méthode appelée pour savoir si un élément est déjà contenu dans la liste."""
    
    for i in range(lst.__len__()) :
        item = lst.item(i)

        if item.text() == el :
            return True 

    return False

#-----------------------------------
# Class
#-----------------------------------

class LibraryDialogAddAction (AbstractGraphicalAction) :
    """Est l'action défaisable pour ajouter des éléments dans la liste."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, lst : QListWidget, element : str) :
        self._lst = lst
        self._element : str = element

    # -------------
    # Methods
    # -------------

    def do (self) :
        
        if not _lst_contains_element(self._lst, self._element) :
            QListWidgetItem(self._element, self._lst)

    def undo (self) :
        
        for i in range(self._lst.__len__()) :
            item = self._lst.item(i)

            if item.text() == self._element :
                self._lst.takeItem(i)
                return