#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import List

# PyQt5 Imports
from PyQt5.QtCore import QPointF, QSizeF, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.interface.graphical_actions.diagram_move_graphical_element_action import DiagramMoveGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_resize_graphical_element_action import DiagramResizeGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_rotate_graphical_element_action import DiagramRotateGraphicalElementAction
from muphyn.packages.interface.models.event_signal_data import EventSignalData
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class AbstractMoveableGraphicalElement (AbstractGraphicalElement) :
    """Est la classe abstraite commune aux éléments graphiques qui peuvent être bougé dans l'interface."""

    # -------------
    # Signals
    # -------------

    position_changed = pyqtSignal()
    size_changed = pyqtSignal()
    rotation_changed = pyqtSignal()

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, size : QSizeF, rotation : float = 0.0, text : str = '', parent : QGraphicsItem = None) :
        
        AbstractGraphicalElement.__init__(self, name, position, rotation, text, parent)

        self._old_pos = position
        self._old_rot = rotation
        
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)

        self.xChanged.connect(self.position_changed_method)
        self.yChanged.connect(self.position_changed_method)
        self.rotationChanged.connect(self.rotation_changed_method)
    
    # -------------
    # Methods
    # -------------
    def size_changed_method (self) -> None :
        self.size_changed.emit()

    def resize (self, param : EventSignalData) -> None :

        bounding_rect = self.boundingRect()

        old_size = self.size

        x2 = param.value.x() / 2
        y2 = param.value.y() / 2
        bounding_rect.adjust(-x2, -y2, x2, y2)

        self.prepareGeometryChange()
        # self.update()

        if bounding_rect.width() < 0 :
            bounding_rect.setWidth(0)
    
        if bounding_rect.height() < 0 :
            bounding_rect.setHeight(0)

        #UNDO REDO Stuff

        if self.action_size_semaphore :
            return

        if not(hasattr(self, 'diagram_model')) :
            return

        if self.diagram_model is None : 
            return

        if self.diagram_model.actions_holder is None :
            return
        
        last_action = self.diagram_model.actions_holder.last_action
        if not(last_action is None) :
            if isinstance(last_action, DiagramResizeGraphicalElementAction) :
                if last_action.graphical_index == self.graphical_index :
                    last_action.new_size = self.size
                    return
        
        self.diagram_model.actions_holder.append(DiagramResizeGraphicalElementAction(self, old_size, self.size))

    # -------------
    # Slots
    # -------------
    @pyqtSlot()
    def position_changed_method (self) -> None : 
        self.position_changed.emit()

        #UNDO REDO Stuff

        new_pos = self.pos()

        if self._old_pos == new_pos :
            return

        if self.action_pos_semaphore :
            return

        if not(hasattr(self, 'diagram_model')) :
            return

        if self.diagram_model is None : 
            return

        if self.diagram_model.actions_holder is None :
            return
        
        last_action = self.diagram_model.actions_holder.last_action

        if not(last_action is None) :
            if isinstance(last_action, DiagramMoveGraphicalElementAction) :

                if self.graphical_index == last_action._graphical_element_index :
                    last_action.new_position = new_pos
                    self._old_pos = new_pos
                    return

                if last_action.contains_index(self.graphical_index) :
                    return

        selection : List[AbstractGraphicalElement] = []

        for selected_element in self.diagram_model._scene.selectedItems() :
            selection.append(selected_element)

        self.diagram_model.actions_holder.append(DiagramMoveGraphicalElementAction(self, selection, self._old_pos, new_pos))
        self._old_pos = new_pos

    @pyqtSlot()
    def rotation_changed_method (self) -> None :
        self.rotation_changed.emit()

        new_rot = self.rotation()

        #UNDO REDO Stuff

        if self._old_rot == new_rot :
            return

        if self.action_rot_semaphore :
            return

        if not(hasattr(self, 'diagram_model')) :
            return

        if self.diagram_model is None : 
            return

        if self.diagram_model.actions_holder is None :
            return
        
        last_action = self.diagram_model.actions_holder.last_action

        if not(last_action is None) :
            if isinstance(last_action, DiagramRotateGraphicalElementAction) :
                if last_action.graphical_index == self.graphical_index :
                    last_action.new_rotate = new_rot
                    self._old_rot = new_rot
                    return
        
        self.diagram_model.actions_holder.append(DiagramRotateGraphicalElementAction(self, self._old_rot, new_rot))
        self._old_rot = new_rot
    