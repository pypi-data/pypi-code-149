#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from enum import Enum
from typing import Iterable, List, Any

# PyQt5 Imports
from PyQt5.QtCore import QPointF, QMarginsF, QRectF, QSize, QSizeF, Qt, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.event_signal_data import EventSignalData
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement
from muphyn.packages.interface.models.signals_model.abstract_connection_model import AbstractConnectionModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel, InputConnectionGroupModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel, OutputConnectionGroupModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.shapes.basic_shape import Rectangle, Circle, Polygon, Text
from muphyn.packages.interface.utils.graphical_items import BoxModelInfoArea
from muphyn.packages.interface.utils.interface_constants import MuphynFonts

#-----------------------------------
# Class
#-----------------------------------

io_margin : int = 4
name_margin : QPointF = QPointF(10, 5)

class BoxType(Enum):
    Math = 1
    Signal = 2
    Source = 3

class AbstractBoxModel (AbstractMoveableGraphicalElement) :
    """Est la classe abstraite des éléments capable d'être rendu sous forme de boxes et affichés à l'écran."""

    # -------------
    # Constants
    # -------------
    MinimunBoxWidth = 80
    MinimunBoxHeight = 80

    # -------------
    # Signals
    # -------------    
    input_count_changed = pyqtSignal()
    output_count_changed = pyqtSignal()

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, size : QSizeF, rotation : float = 0.0, 
                    text : str = '', box_type: BoxType = BoxType.Signal, icon: str = None, parent : QGraphicsItem = None) :
        self._font_metrics_used = None

        AbstractMoveableGraphicalElement.__init__(self, name, position, size, rotation, text, parent)

        # Inputs
        self._inputs : List[InputConnectionModel] = []
        self._inputs_groups: dict[str, InputConnectionGroupModel] = {}

        # Outputs
        self._outputs : List[OutputConnectionModel]  = []
        self._outputs_groups: dict[str, OutputConnectionGroupModel] = {}

        self._size_text : QSize = QSize(0, 0)

        self._box_type = box_type

        if box_type == BoxType.Math:
            self.box_body: Rectangle = Rectangle(QPointF(InputConnectionModel.ItemWidth, 0), 
                AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight, border_color=Qt.GlobalColor.black, fill_color=Qt.GlobalColor.white, parent=self)
        elif box_type == BoxType.Signal:
            self.box_body: Polygon = Polygon( 
                [
                    QPointF(InputConnectionModel.ItemWidth, 0), 
                    QPointF(InputConnectionModel.ItemWidth, AbstractBoxModel.MinimunBoxHeight), 
                    QPointF(InputConnectionModel.ItemWidth + AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight/2)
                ],
                border_color=Qt.GlobalColor.black, 
                fill_color=Qt.GlobalColor.white,
                parent=self
                )
        elif box_type == BoxType.Source:
            radius = min(AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight) / 2
            center = QPointF(AbstractBoxModel.MinimunBoxWidth/2, AbstractBoxModel.MinimunBoxHeight/2) + QPointF(InputConnectionModel.ItemWidth, 0)
            self.box_body: Circle = Circle(center, radius, 
                border_color=Qt.GlobalColor.black, fill_color=Qt.GlobalColor.white, parent=self)
        else:
            raise(f"AbstractBoxModel.__init__(): Box Type is not supported: {box_type}")

        
        # Name 
        box_name_position = self.box_body.boundingRect().bottomLeft() + self.box_body.pos()
        self.name_label: Text = Text(name, box_name_position, text_max_width=AbstractBoxModel.MinimunBoxWidth, 
            font=MuphynFonts.BoxModelDetailsFont, alignment=Qt.AlignmentFlag.AlignHCenter, parent=self)

        # Box Body hiver event
        self.box_body.setAcceptHoverEvents(True)        
        self.box_body.hoverEnterEvent = self.boxBodyHoverEnterEvent
        self.box_body.hoverLeaveEvent = self.boxBodyHoverLeaveEvent

        # Box Details
        margins = 5
        if box_type == BoxType.Source:
            margins = 15
        elif box_type == BoxType.Signal:
            margins = QMarginsF(0, 20, 40, 20)
        self.box_details = BoxModelInfoArea(self.box_body.boundingRect().size(), self.name, image_path=icon, value=None, margins=margins, parent=self.box_body)
    
        # Init UI update handler
        self._should_recompute_inputs = False
        self._should_recompute_outputs = False
        self._should_recompute_box_details = False

    # -------------
    # Properties
    # -------------
    @property
    def inputs (self) -> Iterable[InputConnectionModel] :
        """Permet de récuperer les signaux d'entrées."""
        for inputs_group in self._inputs_groups.values():
            for input_ in inputs_group.inputs:
                yield input_

    @property
    def input_len (self) -> int :
        """Permet de récuperer le nombre d'entrées."""
        return sum([inputs_group.count for inputs_group in self._inputs_groups.values()])

    @property
    def inputs_groups(self) -> dict[str, InputConnectionGroupModel]:
        return self._inputs_groups

    @property
    def outputs (self) -> Iterable[OutputConnectionModel] :
        """Permet de récuperer les signaux de sorties."""
        for outputs_group in self._outputs_groups.values():
            for output in outputs_group.outputs:
                yield output

    @property
    def output_len (self) -> int :
        """Permet de récuperer le nombre de sorties."""
        return sum([outputs_group.count for outputs_group in self._outputs_groups.values()])

    @property
    def outputs_groups(self) -> dict[str, OutputConnectionGroupModel]:
        return self._outputs_groups

    @AbstractGraphicalElement.text.setter
    def text (self, text_ : str) -> None :
        AbstractGraphicalElement.text = text_
    
    @property
    def minimum_size (self) -> QSizeF :
        """Permet de récuperer la taille minimum de la boxes."""
        return QSizeF(AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight) if self.rotation() % 180 == 0 else QSizeF(AbstractBoxModel.MinimunBoxHeight, AbstractBoxModel.MinimunBoxWidth)

    @property
    def signals (self) -> Iterable[SignalLinkModel] :
        """Permet de récueperer la liste des liens connectés à la box."""

        _buff_already_passed = []

        for input_ in self.inputs :
            for signal in input_._links : 
                if signal in _buff_already_passed :
                    continue

                yield signal
                _buff_already_passed.append(signal)

        for output in self.outputs :
            for signal in output._links : 
                if signal in _buff_already_passed :
                    continue

                yield signal
                _buff_already_passed.append(signal)

    @property
    def size(self) -> QSizeF:
        return self.box_body.size

    @size.setter
    def size(self, new_size: QSizeF) -> None:
        self.setSize(new_size)

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        if hasattr(self, "_bounding_rect"):
            return self._bounding_rect
        else:
            return super().boundingRect()

    def setIcon(self, icon):
        self.box_details.setIcon(icon)

    def setRotation (self, angle: float) -> None :
        angle = ((angle//90)%4)*90
        super().setRotation(angle)

    def setSize(self, new_size: QSizeF):
        # Handle Width
        if new_size.width() < AbstractBoxModel.MinimunBoxWidth:
            new_size.setWidth(AbstractBoxModel.MinimunBoxWidth)

        # Handle Height
        if new_size.height() < AbstractBoxModel.MinimunBoxHeight:
            new_size.setHeight(AbstractBoxModel.MinimunBoxHeight)

        if self.box_body.size != new_size:

            if self._box_type == BoxType.Math:
                self.box_body.size = new_size

            elif self._box_type == BoxType.Signal:
                self.box_body.points = [
                    QPointF(InputConnectionModel.ItemWidth, 0), 
                    QPointF(InputConnectionModel.ItemWidth, new_size.height()), 
                    QPointF(InputConnectionModel.ItemWidth + new_size.width(), new_size.height()/2)
                ]

            elif self._box_type == BoxType.Source:
                self.box_body.center = QPointF(new_size.width()/2, new_size.height()/2) + QPointF(InputConnectionModel.ItemWidth, 0)
                self.box_body.radius = min(AbstractBoxModel.MinimunBoxWidth, new_size.height()) / 2

            else:
                raise(f"AbstractBoxModel.__init__(): Box Type is not supported: {self._box_type}")

            self.update_ui()

    def setValue(self, value: Any):
        self.box_details.set_value(value)

    def add_inputs_groups(self, inputs_group: dict[str, dict], infinite_groups_reset=False):
        
        should_update_ui = False

        for name, group_data in inputs_group.items() :
            if name in self._inputs_groups:
                LogManager().error(f"{self._name}: Try to add a duplicated input group {name}")
            else:
                should_update_ui = True 
                
                # Get isInfinite parameter
                is_infinite = group_data["isInfinite"]

                # Get count parameter
                count = group_data["minimumCount"] if is_infinite and infinite_groups_reset else group_data["count"]

                # Add inputs group
                self._inputs_groups[name] = InputConnectionGroupModel(name, is_infinite, group_data["type"], 
                    group_data["minimumCount"], group_data["maximumCount"], count, parent=self)

        # Update UI
        if should_update_ui:
            self.update_ui()

    def add_inputs_group(self, name: str, group_data: dict):
        if name in self._inputs_groups:
            LogManager().error(f"{self._name}: Try to add a duplicated input group {name}")
        else:            
            # Add inputs group
            self._inputs_groups[name] = InputConnectionGroupModel(name, group_data["isInfinite"], group_data["type"], 
                group_data["minimumCount"], group_data["maximumCount"], group_data["count"], parent=self)

            self.update_ui()

    def append_input (self, group_name : str) -> InputConnectionModel :
        """Permet d'insérer une entrée dans la box."""
        if group_name in self._inputs_groups:
            # Get input group
            input_group = self._inputs_groups[group_name]

            # Append new input
            input_ = input_group.append_input()

            # Update UI
            self._should_recompute_inputs = True
            self.update_ui()

            self.input_count_changed.emit()

            return input_
        else:
            return None

    def insert_input (self, input_index : int, group_name : str) -> InputConnectionModel :
        """Permet d'insérer une entrée dans la box."""

        if group_name in self._inputs_groups:
            # Get input group
            input_group = self._inputs_groups[group_name]

            # Append new input
            input_ = input_group.insert_input(input_index)

            # Update UI
            self._should_recompute_inputs = True
            self.update_ui()

            self.input_count_changed.emit()

            return input_
        else:
            return None

    def get_inputs_group(self, group_name: int|str) -> InputConnectionGroupModel:
        if type(group_name) == int:
            group_name = list(self._inputs_groups)[group_name]

        if group_name in self._inputs_groups:
            return self._inputs_groups[group_name]

    def remove_input (self, input_group_name: str, input_ : InputConnectionModel) -> None :
        """Permet de suppprimer une entrée de la box."""

        # Remove all existing links
        for i in range(len(input_._links)) :
            self.diagram_model.remove_element(input_._links[i])

        # Remove input
        self._inputs_groups[input_group_name].remove_input(input_)
        input_.deleteLater()

        # Recompute box model
        self._should_recompute_inputs = True
        self.update_ui()

        self.input_count_changed.emit()

    def clear_inputs(self, group_name: str = None):
        # Clear all infinite input group
        if group_name is None:
            for inputs_group in self._inputs_groups:
                inputs_group.clear_inputs()
                
        # Clear by input name
        else:
            self._inputs_groups[group_name].clear_input()

    def add_outputs_groups(self, outputs_groups: dict[str, dict], infinite_groups_reset=False):
        
        should_update_ui = False

        for name, group_data in outputs_groups.items() :
            if name in self._outputs_groups:
                LogManager().error(f"{self._name}: Try to add a duplicated output group {name}")
            else:
                should_update_ui = True 
                
                # Get isInfinite parameter
                is_infinite = group_data["isInfinite"]

                # Get count parameter
                count = group_data["minimumCount"] if is_infinite and infinite_groups_reset else group_data["count"]

                # Add outputs group
                self._outputs_groups[name] = OutputConnectionGroupModel(name, is_infinite, group_data["type"], 
                    group_data["minimumCount"], group_data["maximumCount"], count, parent=self)

        # Update UI
        if should_update_ui:
            self.update_ui()

    def add_outputs_group(self, name: str, group_data: dict):
        if name in self._outputs_groups:
            LogManager().error(f"{self._name}: Try to add a duplicated output group {name}")
        else:
            # Calc x-Axis position
            x_axis_position = self.box_body.boundingRect().width() + AbstractConnectionModel.ItemWidth

            # Calculate y-axis group position
            y_group_position = sum([outputs_group.boundingRect().height() for outputs_group in self._outputs_groups.values()])
            
            # Add outputs group
            self._outputs_groups[name] = OutputConnectionGroupModel(name, group_data["isInfinite"], group_data["type"], 
                group_data["minimumCount"], group_data["maximumCount"], group_data["count"], group_position=QPointF(x_axis_position, y_group_position), parent=self)

            # Update UI
            self.update_ui()

    def append_output (self, group_name : str) -> OutputConnectionModel :
        """Permet d'insérer une entrée dans la box."""
        if group_name in self._outputs_groups:
            # Get output group
            output_group = self._outputs_groups[group_name]

            # Append new output
            output_ = output_group.append_output()

            # Update UI
            self._should_recompute_outputs = True
            self.update_ui()

            self.output_count_changed.emit()

            return output_
        else:
            return None

    def insert_output (self, output_index : int, group_name : str) -> OutputConnectionModel :
        """Permet d'insérer une entrée dans la box."""

        if group_name in self._outputs_groups:
            # Get output group
            output_group = self._outputs_groups[group_name]

            # Append new output
            output_ = output_group.insert_output(output_index)

            # Update UI
            self._should_recompute_outputs = True
            self.update_ui()

            self.output_count_changed.emit()

            return output_
        else:
            return None

    def get_outputs_group(self, group_name: int|str) -> OutputConnectionGroupModel:
        if type(group_name) == int:
            group_name = list(self._outputs_groups)[group_name]

        if group_name in self._outputs_groups:
            return self._outputs_groups[group_name]

    def remove_output (self, output_group_name: str, output_ : OutputConnectionModel) -> None :
        """Permet de suppprimer une entrée de la box."""

        # Remove all existing links
        for i in range(len(output_._links)) :
            self.diagram_model.remove_element(output_._links[i])

        # Remove output
        self._outputs_groups[output_group_name].remove_output(output_)
        output_.deleteLater()

        # Recompute box model
        self._should_recompute_outputs = True
        self.update_ui()

        self.output_count_changed.emit()

    def clear_outputs(self, group_name: str = None):
        # Clear all infinite output group
        if group_name is None:
            for outputs_group in self._outputs_groups:
                outputs_group.clear_outputs()
                
        # Clear by output name
        else:
            self._outputs_groups[group_name].clear_output()

    def update_box_size(self):
        # Calulate New Box Height
        new_box_height = max(self.input_len, self.output_len) * (AbstractConnectionModel.ItemHeight + 10)
        if new_box_height < AbstractBoxModel.MinimunBoxHeight:
            new_box_height = AbstractBoxModel.MinimunBoxHeight

        # Calculate new size
        self.setSize(QSizeF(self.box_body._size.width(), new_box_height))
        self._should_recompute_inputs = True
        self._should_recompute_outputs = True
        self._should_recompute_box_details = True
        
    def recompute_inputs_positions (self) -> None :
        """Permet de recalculer les positions des entrées."""

        # Is should not recompute → don't do anything
        if not(self._should_recompute_inputs) or len(self._inputs_groups) == 0:
            return
        self._should_recompute_inputs = False

        # Calculate total height
        biggest_io_groups = self._inputs_groups if self.input_len > self.output_len else self._outputs_groups
        total_inputs_groups_height = sum([io_group.boundingRect().height() for io_group in biggest_io_groups.values()])

        # Calculate total margin
        total_margin = self.box_body.boundingRect().height() - total_inputs_groups_height

        # Calculate margin between inputs groups
        height_margin = total_margin / (len(self._inputs_groups) + 1)

        # Init y_axis position
        y_axis_position = height_margin - 5
        
        # Recompute all inputs groups position
        for inputs_group in self._inputs_groups.values():
            # Update inputs group position
            inputs_group.setPos(QPointF(0, y_axis_position))

            # Calculate next inputs group position
            y_axis_position += inputs_group.boundingRect().height() + height_margin - 5

    def recompute_outputs_positions (self) -> None :
        """Permet de recalculer les positions des entrées."""

        # Is should not recompute → don't do anything
        if not(self._should_recompute_outputs) or len(self._outputs_groups) == 0:
            return
        self._should_recompute_outputs = False

        # Calculate total height
        biggest_io_groups = self._outputs_groups if self.input_len > self.output_len else self._outputs_groups
        total_outputs_groups_height = sum([io_group.boundingRect().height() for io_group in biggest_io_groups.values()])

        # Calculate total margin
        total_margin = self.box_body.boundingRect().height() - total_outputs_groups_height

        # Calculate margin between outputs groups
        height_margin = total_margin / (len(self._outputs_groups) + 1)

        # Init y_axis position
        y_axis_position = height_margin - 5

        # Calc x-Axis position
        x_axis_position = self.box_body.boundingRect().width() + AbstractConnectionModel.ItemWidth

        # Recompute all outputs groups position
        for outputs_group in self._outputs_groups.values():
            # Update outputs group position
            outputs_group.setPos(QPointF(x_axis_position, y_axis_position))

            # Calculate next outputs group position
            y_axis_position += outputs_group.boundingRect().height() + height_margin - 5

    def recompute_box_details(self):
        if not self._should_recompute_box_details:
            return 
        self._should_recompute_box_details = False

        # Recompute box name position
        self.name_label.setPos(self.box_body.boundingRect().bottomLeft() + self.box_body.pos())
        

        # Update box detail bounding rect
        self.box_details.set_bounding_rect(self.box_body.boundingRect().size())

    def update_ui(self):
        # Update box body size
        self.update_box_size()

        # Recompute intputs position
        self.recompute_inputs_positions()
        
        # Recompute outputs position
        self.recompute_outputs_positions()
        
        # Recompute box details
        self.recompute_box_details()

        # Recalculate bounding box
        old_bounding_rect = self.boundingRect()
        bounding_rect = self.box_body.boundingRect().translated(self.box_body.pos())
        for ios_group in [*self._inputs_groups.values(), *self._outputs_groups.values()]:
            bounding_rect = bounding_rect.united(ios_group.connectors_bounding_rect().translated(ios_group.pos()))

        self._bounding_rect = bounding_rect
        
        # Recompute intputs position
        self.update(self._bounding_rect.united(old_bounding_rect).united(self.name_label.boundingRect()))
        

    def mouseMoveEvent (self, event : QGraphicsSceneMouseEvent) -> None :
        return super().mouseMoveEvent(event)

    def mousePressEvent (self, event : QGraphicsSceneMouseEvent) -> None :
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None :
        return super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        return super().mouseDoubleClickEvent(event)
    
    def itemChange (self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any :
        if change == QGraphicsItem.ItemSelectedChange :
            self.selectionChanged(EventSignalData(self, value))

        # If Item is deleted
        elif change == QGraphicsItem.GraphicsItemChange.ItemSceneChange and value is None:
            if self.isUnderMouse():
                # Reinitialise Cursor 
                while QApplication.overrideCursor() is not None:
                    QApplication.restoreOverrideCursor()

        return super().itemChange(change, value)

    def selectionChanged (self, param : EventSignalData) -> None :
        # If one item is selected
        if param.value == 1 and param.sender == self:
            self.setZValue(2)

            # Update Pen
            self.box_body.line_style = Qt.PenStyle.DashLine
        else:
            self.setZValue(1)

            # Update Pen
            self.box_body.line_style = Qt.PenStyle.SolidLine

    def boxBodyHoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        QApplication.setOverrideCursor(Qt.SizeAllCursor)
        return super().hoverEnterEvent(event)

    def boxBodyHoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        while QApplication.overrideCursor() is not None:
            QApplication.restoreOverrideCursor()
        return super().hoverLeaveEvent(event)