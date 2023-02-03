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

class NewBoxDialogRemoveAction (AbstractGraphicalAction) :
    """Est l'action capable de supprimer des items dans un des tableau."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, source : Any, table : QTableWidget) :
        AbstractGraphicalAction.__init__(self, source)
        self._table = table
        self._data : List[List[str]] = []
        self._was_already_removed : bool = False

    # -------------
    # Properties
    # -------------

    @property 
    def table (self) -> QTableWidget :
        """Permet de récuperer le tableau dans lequel l'item a été ajouté."""
        return self._table

    @property
    def data (self) -> List[List[str]] :
        """Permet de récuperer les données qui ont été supprimées dans le but de les rajouter dans le tableau."""
        return self._data

    @property
    def was_already_removed (self) -> bool :
        """
        Permet de savoir si c'est la deuxième fois que le do est appelée.
        Permet de supprimer les lignes de données contenant les valeurs avant rajout.
        """
        return self._was_already_removed
    
    # -------------
    # Method
    # -------------

    def do (self) -> None :
        
        if self._was_already_removed :
            
            self._data.reverse()

            for row_data in self._data :

                row_data[1] = self._table.item(row_data[0], 0).text()
                row_data[2] = self._table.cellWidget(row_data[0], 1).currentText()
                row_data[3] = self._table.cellWidget(row_data[0], 2).currentText()
                row_data[4] = self._table.item(row_data[0], 3).text()

                self._table.removeRow(row_data[0])
                
        else :

            for d in self._data :
                d.clear()
            self._data.clear()

            rows : List[int] = []
            for i in self._table.selectedIndexes() :
                rows.append(i.row())

            rows.sort()
            rows.reverse()

            for row in rows :
                current_data : List[str] = []

                current_data.append(row)
                current_data.append(self._table.item(row, 0).text())
                current_data.append(self._table.cellWidget(row, 1).currentText())
                current_data.append(self._table.cellWidget(row, 2).currentText())
                current_data.append(self._table.item(row, 3).text())

                self._data.append(current_data)
                self._table.removeRow(row)
                
        self._was_already_removed = True
            
    def undo (self) -> None :

        self._data.reverse()
        for row_data in self._data :
            self._table.insertRow(row_data[0])
            self._table.setItem(row_data[0], 0, QTableWidgetItem(row_data[1]))

            combo_type = QComboBox()
            for data_type in DataType :
                combo_type.addItem(data_type.__str__().lower())
            combo_type.setCurrentText(row_data[2])

            self._table.setCellWidget(row_data[0], 1, combo_type)

            combo_input_count = QComboBox()
            for i in range(9) :
                combo_input_count.addItem(str(i + 1))
            combo_input_count.addItem('Infinity')
            combo_input_count.setCurrentText(row_data[3])

            self._table.setCellWidget(row_data[0], 2, combo_input_count)
            self._table.setItem(row_data[0], 3, QTableWidgetItem(row_data[4]))

            self._table.setRowHeight(row_data[0], 20)