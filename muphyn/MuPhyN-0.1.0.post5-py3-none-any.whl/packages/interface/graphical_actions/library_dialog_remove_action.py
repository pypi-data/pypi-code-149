#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict

from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from muphyn.packages.interface.graphical_actions.abstract_graphical_action import AbstractGraphicalAction

#-----------------------------------
# Class
#-----------------------------------

class LibraryDialogRemoveAction (AbstractGraphicalAction) :
    """Est l'action défaisable pour supprimer des éléments dans la liste."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, lst : QListWidget, elements : List[str]) :
        self._lst = lst

        self._elements : Dict[str, int] = {}
        
        for element in elements :
            self._elements[element] = 0

    # -------------
    # Methods
    # -------------

    def do (self) :
        
        for element in self._elements :

            for i in range(self._lst.__len__()) :
                item = self._lst.item(i)

                if item.text() == element :
                    self._elements[element] = i
                    self._lst.takeItem(i)
                    break

    def undo (self) :
        
        for element in self._elements.__reversed__() :
            index = self._elements[element]
            QListWidgetItem(element)
            self._lst.insertItem(index, element)
