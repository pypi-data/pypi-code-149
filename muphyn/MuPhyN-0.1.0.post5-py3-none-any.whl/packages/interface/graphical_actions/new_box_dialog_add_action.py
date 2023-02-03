#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Any

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox

from muphyn.packages.interface.graphical_actions.abstract_graphical_action import AbstractGraphicalAction
from muphyn.packages.core.plci_core_data_type import DataType

#-----------------------------------
# Class
#-----------------------------------

class NewBoxDialogAddAction (AbstractGraphicalAction) :
    """Est l'action capable d'ajouter un item dans un des tableau."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, source : Any, text : str, table : QTableWidget) :
        AbstractGraphicalAction.__init__(self, source)
        self._table = table
        self._current_index = -1
        self._was_already_added = False
        self._old_data : List[str] = []
        self._text : str = text

    # -------------
    # Properties
    # -------------

    @property
    def current_index (self) -> int :
        """Permet de récuperer l'index au moment où la nouvelle valeur a été ajouté."""
        return self._current_index

    @property 
    def table (self) -> QTableWidget :
        """Permet de récuperer le tableau dans lequel l'item a été ajouté."""
        return self._table

    @property
    def was_already_added (self) -> bool :
        """
        Permet de savoir si c'est la deuxième fois que le do est appelée.
        Permet de rajouter une ligne de données contenant les valeurs avant suppression.
        """
        return self._was_already_added

    @property
    def old_data (self) -> List[str] :
        """Permet de récuperer les données qui se trouvait dans le tableau avant le undo."""
        return self._old_data
    
    # -------------
    # Method
    # -------------

    def do (self) -> None :

        self._current_index = self._table.rowCount()
        self._table.setRowCount(self._table.rowCount() + 1)
        self._table.setRowHeight(self._current_index, 20)

        if self._was_already_added :
            self._table.setItem(self._current_index, 0, QTableWidgetItem(self._old_data[0]))
            
            combo_type = QComboBox()
            for data_type in DataType :
                combo_type.addItem(data_type.__str__().lower())
            combo_type.setCurrentText(self._old_data[1])

            self._table.setCellWidget(self._current_index, 1, combo_type)

            combo_input_count = QComboBox()
            for i in range(9) :
                combo_input_count.addItem(str(i + 1))
            combo_input_count.addItem('Infinity')
            combo_input_count.setCurrentText(self._old_data[2])

            self._table.setCellWidget(self._current_index, 2, combo_input_count)

            self._table.setItem(self._current_index, 3, QTableWidgetItem(self._old_data[3]))

        else :
            self._table.setItem(self._current_index, 0, QTableWidgetItem(self._text + ' ' + str(self._current_index + 1)))

            combo_type = QComboBox()
            for data_type in DataType :
                combo_type.addItem(data_type.__str__().lower())
            combo_type.setCurrentText('float')

            self._table.setCellWidget(self._current_index, 1, combo_type)

            combo_input_count = QComboBox()
            for i in range(9) :
                combo_input_count.addItem(str(i + 1))
            combo_input_count.addItem('Infinity')

            self._table.setCellWidget(self._current_index, 2, combo_input_count)
            self._table.setItem(self._current_index, 3, QTableWidgetItem('0'))

    def undo (self) -> None :

        self._was_already_added = True

        self._old_data.append(self._table.item(self._current_index, 0).text())
        self._old_data.append(self._table.cellWidget(self._current_index, 1).currentText())
        self._old_data.append(self._table.cellWidget(self._current_index, 2).currentText())
        self._old_data.append(self._table.item(self._current_index, 3).text())

        self._table.removeRow(self._current_index)