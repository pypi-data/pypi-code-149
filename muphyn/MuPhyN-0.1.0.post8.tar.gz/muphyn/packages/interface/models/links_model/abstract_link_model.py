#-----------------------------------
# Imports
#-----------------------------------

# general Imports
from typing import Iterable, Any

# PyQt5 Imports
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF, pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.links_model.link_type import LinkType
from muphyn.packages.interface.shapes.basic_shape.shapes import Path
from muphyn.packages.interface.utils.interface_constants import MuphynPens

#-----------------------------------
# Class
#-----------------------------------
class AbstractLinkModel (AbstractGraphicalElement) :
    """Est la classe abstraites aux classes représentant des liens entre les noeuds."""

    # -------------
    # Constants
    # -------------
    LinkToBoxMargin = 20
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, input : Any, output : Any, link_type : LinkType, 
                  text : str = '') :
        # Save Input & Output model
        self._input_model : Any = input
        self._output_model : Any = output

        # Get absolute position of Input & Output
        input_position : QPointF = self._input_model.absolute_connector_center
        output_position : QPointF = self._output_model.absolute_connector_center

        # Init previous position
        self._last_input_position = input_position
        self._last_output_position = output_position

        # Points
        points = AbstractLinkModel.calc_path_points(input_position, output_position)

        # Calculate origin
        bounding_rect = AbstractLinkModel.calc_bounding_rect(points)

        # Calculate all points from origin
        points = [point - bounding_rect.topLeft() for point in points]
        
        # Calculate steps
        if link_type == LinkType.SQUARE:
            steps = AbstractLinkModel.build_straight_path(points)
        elif link_type == LinkType.CURVED:
            steps = AbstractLinkModel.build_curved_path(points)
        else:
            LogManager().Error("AbstractLinkModel.__init__() : Wrong link type {type(link_type)}")
            return

        # Set Position
        AbstractGraphicalElement.__init__(self, 'link', bounding_rect.topLeft(), 0, text, None)
        
        # Append path
        self._path = Path(steps, parent=self)
        self._path.pen = MuphynPens.SelectedLinkPen if self.isSelected() else MuphynPens.UnSelectedLinkPen

        # Set Link parameters
        self._link_type : LinkType = link_type
        self._link_value : float = 0.8

        self._input_model.position_changed.connect(self.input_changed)
        self._input_model.size_changed.connect(self.input_changed)
        self._input_model.rotation_changed.connect(self.input_changed)

        if self._input_model.box_model is not None :
            self._input_model.box_model.position_changed.connect(self.input_changed)
            self._input_model.box_model.size_changed.connect(self.input_changed)
            self._input_model.box_model.rotation_changed.connect(self.input_changed)

        self._output_model.position_changed.connect(self.output_changed)
        self._output_model.size_changed.connect(self.output_changed)
        self._output_model.rotation_changed.connect(self.output_changed)

        if self._output_model.box_model is not None:
            self._output_model.box_model.position_changed.connect(self.output_changed)
            self._output_model.box_model.size_changed.connect(self.output_changed)
            self._output_model.box_model.rotation_changed.connect(self.output_changed)

        self._about_to_erased = False

    # -------------
    # Properties
    # -------------
    @AbstractGraphicalElement.rot.setter
    def rot (self, rot_ : float) -> None :
        ...

    @property
    def color(self) -> QColor:
        return self._path.border_color
    
    @property
    def input (self) -> Any :
        """Permet de récuperer le noeud d'entrée du lien."""
        return self._input_model

    @property 
    def output (self) -> Any :
        """Permet de récuperer le noeud de sortie du lien."""
        return self._output_model

    @property
    def link_type (self) -> LinkType :
        """Permet de récuperer le type de lien entre les deux noeuds."""
        return self._link_type

    @link_type.setter
    def link_type (self, link_type_ : LinkType) -> None :
        """Permet de modifier le type de lien entre les deux noeuds."""

        if self._link_type == link_type_ :
            return

        old_value = self._link_type

        self._link_type = link_type_

        if self._link_value > 1.0 or self._link_value < 0.0 :
            self._link_value = 0.5

        if self.action_param_semaphore :
            return

        self.param_changed.emit(self, 'link_type', old_value, self._link_type)

    @property
    def link_value (self) -> float :
        """
        Permet de récuperer la valeur du lien :
        - en cas de lien courbe : la courbure du lien.
        - en cas de lien carré : le pourcentage avant que le lien ne se brise.
        """
        return self._link_value

    @link_value.setter
    def link_value (self, link_value_ : float) -> None :
        """Permet de modifier la valeur du lien."""

        if self._link_value == link_value_ :
            return

        old_value = self._link_value

        self._link_value = link_value_

        if self._link_value > 1.0 or self._link_value < 0.0 :
            self._link_value = 0.5

        if self.action_param_semaphore :
            return

        self.param_changed.emit(self, 'link_value', old_value, self._link_value)


    # -------------
    # Methods
    # -------------
    @pyqtSlot()
    def input_changed (self) :
        """Est la méthode appelée lorsque la poistion du noeud 1 change."""
        self.self_update()

    @pyqtSlot()
    def output_changed (self) :
        """Est la méthode appelée lorsque la position du noeud 2 change."""
        self.self_update()

    def boundingRect(self) -> QRectF:
        return self._path.boundingRect()

    def setRotation(self, rot_ : float) -> None :
        ...
 
    def self_update (self) -> None :
        """Est la méthode appelée lorsque la position ou la taille du node 2 est modifiée."""
        if self.scene() is None :
            return

        # get new input & output positions
        input_position = self._input_model.absolute_connector_center
        output_position = self._output_model.absolute_connector_center
        
        # Points
        points = AbstractLinkModel.calc_path_points(input_position, output_position)

        # Calculate origin
        bounding_rect = AbstractLinkModel.calc_bounding_rect(points)

        # Calculate all points from origin
        points = [point - bounding_rect.topLeft() for point in points]
        
        # Calculate steps
        steps = AbstractLinkModel.build_straight_path(points)
        self._path.steps = steps

        # Update Link Position
        self.setPos(bounding_rect.topLeft())

        # Calc bounding rect
        min_x = min(input_position.x(), self._last_input_position.x(), output_position.x(), self._last_output_position.x()) - AbstractLinkModel.LinkToBoxMargin
        min_y = min(input_position.y(), self._last_input_position.y(), output_position.y(), self._last_output_position.y())
        max_x = max(input_position.x(), self._last_input_position.x(), output_position.x(), self._last_output_position.x()) + AbstractLinkModel.LinkToBoxMargin
        max_y = max(input_position.y(), self._last_input_position.y(), output_position.y(), self._last_output_position.y())
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)

        # Update Scene 
        self.scene().update(min_x, min_y, width, height)

        self._last_input_position = input_position
        self._last_output_position = output_position

    def unbind (self) -> None :
        """Permet de détruire le lien entre les deux noeuds."""

        if self._about_to_erased :
            return

        if self in self._input_model._links :
            self._input_model.remove_link(self)
            self._input_model.is_connected = False
            self._input_model.update(self._input_model.boundingRect())

        if self in self._output_model._links :
            self._output_model.remove_link(self)
            self._output_model.update(self._output_model.boundingRect())
        
        self._about_to_erased = True

    def itemChange (self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any:
        if change == QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged :
            self._path.pen = MuphynPens.SelectedLinkPen if bool(value) else MuphynPens.UnSelectedLinkPen
            self.self_update()

        return super().itemChange(change, value)

    def to_dict(self) -> dict:
        """Est la méthode appelée pour créer un dictionnaire contenant les données d'un lien entre des entrées/sorties."""

        signal_dict = {}

        signal_dict['value'] = 0.0
        signal_dict['data_type'] = self.data_type.__str__()
        signal_dict['index'] = -1
        signal_dict['link_type'] = self.link_type.__str__()
        signal_dict['link_value'] = self.link_value
        signal_dict['text'] = self.text
    
        return signal_dict

    # --------------
    # Static Methods
    # --------------
    def calc_path_points(start_point: QPointF, end_point: QPointF):
        """
        This function assumes that the link start from the input of a box
        & ends in the output of the other box
        """
        # 2 points case
        """
        end_point[]--x
                     |
                     x--[] start_point
        """
        # Set Margin to start/end points
        start_point.setX(start_point.x() - AbstractLinkModel.LinkToBoxMargin)
        end_point.setX(end_point.x() + AbstractLinkModel.LinkToBoxMargin)

        # Round points position
        start_point = QPointF(start_point.toPoint())
        end_point = QPointF(end_point.toPoint())

        if start_point.x() > end_point.x():
            if start_point.y() == end_point.y():
                return [
                    start_point + QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
                    end_point - QPointF(AbstractLinkModel.LinkToBoxMargin, 0)
                ]
            else:
                # Calculate intermediate X
                x_intermediate = (start_point.x() + end_point.x()) / 2

                # Append Intermediate points
                return [
                    start_point + QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
                    QPointF(x_intermediate, start_point.y()),
                    QPointF(x_intermediate, end_point.y()),
                    end_point - QPointF(AbstractLinkModel.LinkToBoxMargin, 0)
                ]
        else:
            # 4 points case
            """
            x-[] 
            |
            x---------x
                      |     
                   []-x
            """
            # Calculate intermediate coordinates
            y_intermediate = int((start_point.y() + end_point.y()) / 2)

            # Append Intermediate points
            return [
                start_point + QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
                start_point,
                QPointF(start_point.x(), y_intermediate),
                QPointF(end_point.x(), y_intermediate),
                end_point,
                end_point - QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
            ]

    def calc_bounding_rect(points: Iterable[QPointF]) -> QRectF:
        min_x = min([point.x() for point in points])
        max_x = max([point.x() for point in points])
        min_y = min([point.y() for point in points])
        max_y = max([point.y() for point in points])

        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        return QRectF(min_x, min_y, width, height)

    def build_straight_path(points: Iterable[QPointF]):
        return [Path.Step(point) for point in points]

    def build_curved_path(points: Iterable[QPointF]):
        factor = 0.2
        path = QtGui.QPainterPath(points[0])

        last_end_point = QPointF
        for index, corner in enumerate(points[1: -1]):
            # Calculate middle of corner segments
            middle_point_1 = (points[index] + corner) / 2
            middle_point_2 = (points[index+2] + corner) / 2

            start_point = (1-factor) * middle_point_1 + factor * corner
            end_point = (1-factor) * middle_point_2 + factor * corner

            path.cubicTo(start_point, corner, end_point)

        path.lineTo(points[-1])

        return path