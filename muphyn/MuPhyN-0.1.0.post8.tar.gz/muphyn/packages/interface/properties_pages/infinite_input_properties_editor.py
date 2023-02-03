#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Any

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QListWidgetItem

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.graphical_actions.diagram_add_input_to_box_action import DiagramAddInputToBoxAction
from muphyn.packages.interface.graphical_actions.diagram_remove_inputs_from_box_action import DiagramRemoveInputsFromBoxAction
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionGroupModel
from muphyn.packages.interface.properties_pages.abstract_infinite_io_properties_editor import AbstractInfiniteIOPropertiesEditor
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.properties_pages.infinite_io_properties_item import InifiniteIOPropertiesItem


#-----------------------------------
# Class
#-----------------------------------

class InfiniteInputPropertiesEditor (AbstractInfiniteIOPropertiesEditor) :
    """Est la classe qui décrit le fonctionnement du panneau pour éditer les propriétés des entrées infinies."""


    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_model : BoxModel, input_group: InputConnectionGroupModel) :

        AbstractInfiniteIOPropertiesEditor.__init__(self, box_model, input_group.name, input_group.data_type, 
            input_group.minimum_count, input_group.maximum_count)
       
        # 
        for input_index, input_ in enumerate(input_group.inputs):
            if input_group.is_infinite : 
                # Create ghost item
                item = QListWidgetItem(self._tbl_connection)

                # Add ghost item to list
                self._tbl_connection.addItem(item)

                # Create io item
                item_widget = InifiniteIOPropertiesItem(input_index+1, input_)

                # Set item geometry
                item.setSizeHint(item_widget.minimumSizeHint())

                # Replace ghost item by IO properties item
                self._tbl_connection.setItemWidget(item, item_widget)

        # Set button enabled if count < maximum count
        self._btn_add.setEnabled(self._tbl_connection.count() < self.maximum_count)

        # Enable remove button if count > mimimum count
        self._btn_remove.setEnabled(self._tbl_connection.count() > self._minimum_count)

        # Set minimum height
        self._tbl_connection.setMinimumHeight(AbstractInfiniteIOPropertiesEditor.ItemHeight)
        self._input_changed_semaphore = False

        # Connect input count changed signal
        self.box_model.input_count_changed.connect(self.box_model_input_count_changed)
        # self.box_model.param_changed.connect(self.on_box_model_param_changed)

        
    # -------------
    # Methods
    # -------------
    
    def contains_input (self, input : Any) -> int : 
        """Permet de savoir si l'entrée est contenue dans la liste."""

        for element_index in range(self._tbl_connection.count()) :
            item = self._tbl_connection.item(element_index)
            item_widget = self._tbl_connection.itemWidget(item)
            item_input = item_widget._connection_model

            if item_input.graphical_index == input.graphical_index :
                return element_index

        return -1


    def box_model_input_count_changed (self) -> None :
        """Est la méthode appelée losque le nombre d'entrée le box est modifié."""

        if self._input_changed_semaphore : 
            return

        # Get inputs group
        inputs_group = self._box_model.get_inputs_group(self._group_name)

        # Remove items
        for element_index in range(self._tbl_connection.count() - 1, -1, -1) :
            item = self._tbl_connection.item(element_index)
            item_widget = self._tbl_connection.itemWidget(item)
            input_ = item_widget._connection_model

            if not(input_ in inputs_group.inputs) :
                item_widget : InifiniteIOPropertiesItem = self._tbl_connection.itemWidget(item)
                self._tbl_connection.takeItem(self._tbl_connection.indexFromItem(item).row())
                item_widget.deleteLater()

        # Adding Items
        for input_index, input_ in enumerate(inputs_group.inputs):
            # Determine if input is already in the list
            element_index = self.contains_input(input_)

            # Add element in the list in the input is already there
            if element_index == -1:
                # Create list ghost item
                item = QListWidgetItem(self._tbl_connection)

                # Add ghost item to the list
                self._tbl_connection.addItem(item)

                # Replace ghost widget by InifiniteIOPropertiesItem
                item_widget = InifiniteIOPropertiesItem(input_index + 1, input_)
                self._tbl_connection.setItemWidget(item, item_widget)

        if self._tbl_connection.count() > 0 :
            item.setSizeHint(self._tbl_connection.itemWidget(self._tbl_connection.item(0)).minimumSizeHint())

        self.recompute_connection_numbers()
        
        # Set button enabled if count < maximum count
        self._btn_add.setEnabled(self._tbl_connection.count() < self.maximum_count)

        # Enable remove button if count > mimimum count
        self._btn_remove.setEnabled(self._tbl_connection.count() > self._minimum_count)

    def translate_ui (self) -> None :
        super().translate_ui()
        
        self._lbl_connection_mode_value.setText(QCoreApplication.translate(self.objectName(), u"Input", None))

    def button_add_click (self) -> None :
        # Build adding input action
        action = DiagramAddInputToBoxAction(
            self.box_model,
            self._group_name
        )
        action.do()
        self.actions_holder.append(action)

    def button_remove_click (self) -> None :
        # Get input to remove
        inputs_group = self.box_model.get_inputs_group(self._group_name)
        inputs_to_remove = [inputs_group.inputs[-1]]
        
        # Build input removal action
        action = DiagramRemoveInputsFromBoxAction(
            self._box_model,
            self._group_name,
            inputs_to_remove
        )

        # Remove input
        action.do()

        # Add action to action holder
        self.actions_holder.append(action)

    def unload (self) -> None :
        # Disconect input count changed event 
        self.box_model.input_count_changed.disconnect(self.box_model_input_count_changed)