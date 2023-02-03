#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QListWidgetItem

from muphyn.packages.interface.graphical_actions.diagram_remove_outputs_from_box_action import DiagramRemoveOutputsFromBoxAction
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionGroupModel
from muphyn.packages.interface.properties_pages.abstract_infinite_io_properties_editor import AbstractInfiniteIOPropertiesEditor
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.properties_pages.infinite_io_properties_item import InifiniteIOPropertiesItem
from muphyn.packages.interface.graphical_actions.diagram_add_output_to_box_action import DiagramAddOutputToBoxAction


#-----------------------------------
# Class
#-----------------------------------

class InfiniteOutputPropertiesEditor (AbstractInfiniteIOPropertiesEditor) :
    """Est la classe qui décrit le fonctionnement du panneau pour éditer les propriétés des sorties infinies."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_model : BoxModel, output_group: OutputConnectionGroupModel) :

        AbstractInfiniteIOPropertiesEditor.__init__(self, box_model, output_group.name, output_group.data_type, 
            output_group.minimum_count, output_group.maximum_count)

        # 
        for output_index, output_ in enumerate(output_group.outputs):
            if output_group.is_infinite : 
                # Create ghost item
                item = QListWidgetItem(self._tbl_connection)
                
                # Add ghost item to list
                self._tbl_connection.addItem(item)

                # Create io item
                item_widget = InifiniteIOPropertiesItem(output_index+1, output_)
                
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
        self._output_changed_semaphore = False

        # Connect output count changed signal
        self.box_model.output_count_changed.connect(self.box_model_output_count_changed)

        
    # -------------
    # Methods
    # -------------
    
    def contains_output (self, output : Any) -> int : 
        """Permet de savoir si la sortie est contenue dans la liste."""

        for element_index in range(self._tbl_connection.count()) :
            item = self._tbl_connection.item(element_index)
            item_widget = self._tbl_connection.itemWidget(item)
            item_output = item_widget._connection_model

            if item_output.graphical_index == output.graphical_index:
                return element_index

        return -1

    def box_model_output_count_changed (self) -> None :
        """Est la méthode appelée losque le nombre de sortie le box est modifié."""

        if self._output_changed_semaphore : 
            return

        # Get inputs group
        outputs_group = self._box_model.get_outputs_group(self._group_name)

        # Remove items
        for element_index in range(self._tbl_connection.count() - 1, -1, -1) :
            item = self._tbl_connection.item(element_index)
            item_widget = self._tbl_connection.itemWidget(item)
            output = item_widget._connection_model

            if not(output in outputs_group.outputs) :
                item_widget : InifiniteIOPropertiesItem = self._tbl_connection.itemWidget(item)
                self._tbl_connection.takeItem(self._tbl_connection.indexFromItem(item).row())
                item_widget.deleteLater()

        # Adding Items
        for output_index, output in enumerate(outputs_group.outputs):
            # Determine if output is already in the list
            element_index = self.contains_output(output)

            # Add element in the list in the output is already there
            if element_index == -1:
                # Create list ghost item
                item = QListWidgetItem(self._tbl_connection)

                # Add ghost item to the list
                self._tbl_connection.addItem(item)

                # Replace ghost widget by InifiniteIOPropertiesItem
                item_widget = InifiniteIOPropertiesItem(output_index + 1, output)
                self._tbl_connection.setItemWidget(item, item_widget)

        if self._tbl_connection.count() > 0 :
            item.setSizeHint(self._tbl_connection.itemWidget(self._tbl_connection.item(0)).minimumSizeHint())

        self.recompute_connection_numbers()
        
        # Set button enabled if count < maximum count
        self._btn_add.setEnabled(self._tbl_connection.count() < self.maximum_count)

        # Enable remove button if count > mimimum count
        self._btn_remove.setEnabled(self._tbl_connection.count() > self._minimum_count)

    def init_ui (self) -> None :
        super().init_ui()

    def translate_ui (self) -> None :
        super().translate_ui()
        
        self._lbl_connection_mode_value.setText(QCoreApplication.translate(self.objectName(), u"Input", None))

    def button_add_click (self) -> None :
        
        action = DiagramAddOutputToBoxAction(
            self._box_model, 
            self._group_name
        )
        action.do()
        self.actions_holder.append(action)

    def button_remove_click (self) -> None :
        # Get output to remove
        outputs_group = self.box_model.get_outputs_group(self._group_name)
        outputs_to_remove = [outputs_group.outputs[-1]]
        
        # Build output removal action
        action = DiagramRemoveOutputsFromBoxAction(
            self._box_model,
            self._group_name,
            outputs_to_remove
        )

        # Remove output
        action.do()

        # Add action to action holder
        self.actions_holder.append(action)

    def unload (self) -> None :
        self._box_model.output_count_changed.disconnect(self.box_model_output_count_changed)