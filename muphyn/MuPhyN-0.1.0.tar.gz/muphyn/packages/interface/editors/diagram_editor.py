#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import ctypes, yaml
from typing import Iterable, List

# PyQt5 Imports
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal, QPointF
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsSceneDragDropEvent, QGraphicsView, QTabWidget, QApplication, QMenu, QAction
from muphyn.packages.core.simulation.model_parser.open_modelica_model_parser import OpenModelicaModelParser

# Project Imports
from muphyn.packages.interface.editors.abstract_editor import AbstractEditor
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.graphical_actions.diagram_add_graphical_element_action import DiagramAddGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_paste_graphical_element_action import DiagramPasteGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_remove_graphical_element_action import DiagramRemoveGraphicalElementAction
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.graphical_models.resizers.abstract_resizer import AbstractResizer
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel
import muphyn.packages.interface.files.simulation_files.simulation_exporter as exporter

from muphyn.packages.interface.widgets.multiphysics_model_previewer import MultiphysicsModelPreviewer
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.widgets.StandardActions import RotateLeftAction, RotateRightAction, DeleteAction

#-----------------------------------
# Classes
#-----------------------------------

class SceneEditor (QGraphicsScene) :
    """Est la scéne graphique dans laquelle les éléments sont dessinés."""    

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, diagram_editor : QGraphicsView, actions_holder : ActionsHolder, diagram_model : AbstractDiagramModel) :

        QGraphicsScene.__init__(self, diagram_editor)
        self._diagram_editor = diagram_editor
        self._actions_holder = actions_holder
        self._diagram_model = diagram_model
        self.setParent(diagram_editor)

    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur d'action."""
        return self._actions_holder

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model

    # -------------
    # Methods
    # -------------

    def dropEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        if event.mimeData().hasUrls() :
            parent = self.parent()
            next_parent = parent.parent()

            while not(next_parent is None) :
                parent = next_parent
                next_parent = parent.parent()

            for url in event.mimeData().urls() :
                self._diagram_editor.open_file(url.toLocalFile())

        else :
            if event.possibleActions() == Qt.CopyAction and event.mimeData().data('action') == 'new box' :
                
                box_data : AbstractBoxData = ctypes.cast(int(event.mimeData().data('box_data')), ctypes.py_object).value

                offset_x, offset_y = [float(offset) for offset in event.mimeData().data('offset').split(";")]

                new_box_position = event.scenePos() + QPointF(offset_x, offset_y)

                action = DiagramAddGraphicalElementAction(self._diagram_editor._diagram_model, [{'box_data': box_data, 'pos': new_box_position}])
                action.do()
                self.actions_holder.append(action)
        
                event.accept()

            else :
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if hasattr(graphical_element, 'inputs') :
                        for input in graphical_element.inputs :
                            if input.isUnderMouse() :
                                input.dropEvent(event)
                                if event.isAccepted() :
                                    return

        super().dropEvent(event)

    def dragEnterEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        
        if event.mimeData().hasUrls() :
            event.accept()
        
        else :

            if event.possibleActions() == Qt.CopyAction and event.mimeData().data('action') == 'new box' :
                    event.accept()
            
            if not(event.isAccepted()) : 
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if hasattr(graphical_element, 'inputs') :
                        for input in graphical_element.inputs :
                            if input.isUnderMouse() :
                                input.dragEnterEvent(event)
                                if event.isAccepted() :
                                    return
            
        super().dragEnterEvent(event)
            
    
    def dragMoveEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        
        if event.mimeData().hasUrls() :
            event.accept()

        else :
            if event.possibleActions() == Qt.CopyAction and event.mimeData().data('action') == 'new box' :
                event.accept()
            else :
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if isinstance(graphical_element, AbstractBoxModel) :
                        if hasattr(graphical_element, 'inputs') :
                            for input in graphical_element.inputs :
                                if input.isUnderMouse() :
                                    input.dragMoveEvent(event)
                                    if event.isAccepted() :
                                        return

        super().dragEnterEvent(event)

    def selected_elements (self) -> Iterable :
        """Permet de récuperer les éléments sélectionnés dans l'interface."""

        for item in self.selectedItems() :
            if isinstance(item, AbstractGraphicalElement) :
                if isinstance(item, AbstractResizer) :
                    continue

                yield item


class GraphicsView (QGraphicsView) :
    """Est la vue graphique dans laquelle la scène graphique est placée.""" 

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, graphical_editor : AbstractEditor, actions_holder : ActionsHolder, diagram_model : AbstractDiagramModel) : 

        QGraphicsView.__init__(self, graphical_editor)

        self._diagram_model : AbstractDiagramModel = diagram_model 
        self._graphical_editor = graphical_editor
        self._actions_holder = actions_holder

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setDragMode(QGraphicsView.RubberBandDrag)

        self._diagram_model.scene = SceneEditor(self, actions_holder, diagram_model)
        self._diagram_model.scene.selectionChanged.connect(self.scene_elements_selected_changed)
        
        self.setScene(self._diagram_model.scene)

        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self._sliding_mouse_event_started =  False

        self.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)
        self.setRenderHint(QPainter.RenderHint.TextAntialiasing, on=True)

    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur d'action."""
        return self._actions_holder

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model

    # -------------
    # Methods
    # -------------
    def add_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet d'ajouter un élément graphique à l'interface."""

        if graphical_element is None :
            return

        self._diagram_model.add_element(graphical_element)

    def rem_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet de supprimer un élément graphique de l'interface."""

        self._diagram_model.remove_element(graphical_element)
        graphical_element.deleteLater()

    
    def mousePressEvent (self, event : QtGui.QMouseEvent):
        """Est l'événement appelée lorsque l'utilisateur appuie sur un bouton de sa souris."""


        if event.button() == Qt.MidButton :
            self.__prevMousePos = event.pos()
            self._sliding_mouse_event_started = True
            event.accept()

        elif event.button() == Qt.RightButton:
            while QApplication.overrideCursor() is not None:
                QApplication.restoreOverrideCursor()
            graphical_element_under_mouse = None
            for graphical_element in self.parent()._diagram_model.graphical_elements :
                if graphical_element.isUnderMouse():
                    graphical_element_under_mouse = graphical_element
                    break

            # If Right Click on Box
            if graphical_element_under_mouse is not None:
                # Init Context Menu Object
                contextMenu = QMenu()

                # Init possible actions
                rotate_left = QAction()
                rotate_right = QAction()
                delete_item = QAction()

                # Add actions if right-click on box
                if isinstance(graphical_element_under_mouse, AbstractBoxModel):
                    # Load Action
                    rotate_left = RotateLeftAction()
                    rotate_right = RotateRightAction()
                    delete_item = DeleteAction("Delete Box")

                    # Append Actions
                    contextMenu.addActions([rotate_left, rotate_right, delete_item])
                    
                # Add actions if right-click on link
                elif isinstance(graphical_element_under_mouse, AbstractLinkModel):
                    # Load Action
                    delete_item = DeleteAction("Delete Link")

                    # Append Actions
                    contextMenu.addActions([delete_item])

                # Add Separator
                contextMenu.addSeparator()

                #
                open_model = 0
                if isinstance(graphical_element_under_mouse, BoxModel):
                    if graphical_element_under_mouse.box_type == "multiphysics-simulation":
                        # Open Modelica
                        open_model = contextMenu.addAction("Open Modelica Model")
                        contextMenu.addSeparator()

                # General Actions
                remove_selected_elements = DeleteAction("Remove Selected Boxes")
                contextMenu.addActions([remove_selected_elements])

                action = contextMenu.exec_(event.screenPos().toPoint())
                
                if action == rotate_left:
                    new_rotation = (graphical_element_under_mouse.rotation() - 90) % 360
                    graphical_element_under_mouse.setRotation(new_rotation)
                elif action == rotate_right:
                    new_rotation = (graphical_element_under_mouse.rotation() + 90) % 360
                    graphical_element_under_mouse.setRotation(new_rotation)
                elif action == delete_item:
                    action = DiagramRemoveGraphicalElementAction(self._diagram_model, [graphical_element_under_mouse])
                    action.do()
                    self.actions_holder.append(action)
                elif action == remove_selected_elements:
                    action = DiagramRemoveGraphicalElementAction(self._diagram_model, self.selected_elements())
                    action.do()
                    self.actions_holder.append(action)
                elif action == open_model:
                    model_path = graphical_element_under_mouse._parameters["model_path"]["value"]
                    try:
                        # Open new tab with OM model
                        om_parser = OpenModelicaModelParser(model_path)
                        previewer = MultiphysicsModelPreviewer(om_parser, parent=self)
                        previewer.open()
                    except Exception as e:
                        LogManager().error(f"Can't open Open Modelica Previewer: {e}")
                else:
                    pass
            else:
                # Init Context Menu Object
                contextMenu = QMenu()

                # Init Action
                remove_selected_elements = DeleteAction("Remove Selected Boxes")

                # Add action to context menu
                contextMenu.addActions([remove_selected_elements])

                # Open Right-click menu
                action = contextMenu.exec_(event.screenPos().toPoint())
                
                if action == remove_selected_elements:
                    action = DiagramRemoveGraphicalElementAction(self._diagram_model, self.selected_elements())
                    action.do()
                    self.actions_holder.append(action)
                else:
                    pass

        else:
            super().mousePressEvent(event)

    def mouseMoveEvent (self, event : QtGui.QMouseEvent) :
        """Est l'événement appelée lorsque l'utilisateur bouge sa souris dans l'élément graphique."""
        
        if event.buttons() == Qt.MidButton :
            
            if not(self._sliding_mouse_event_started) :
                self.__prevMousePos = event.pos()
                self._sliding_mouse_event_started = True
            
            else :
                offset = self.__prevMousePos - event.pos()
                self.__prevMousePos = event.pos()

                self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
                self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())

            event.accept()

        else :
            
            return super().mouseMoveEvent(event)


    def mouseReleaseEvent (self, event: QtGui.QMouseEvent) -> None :
        """Est l'événement appelée lorsque l'utilisateur relache un bouton de sa souris."""

        if event.button() == Qt.MidButton :
            self._sliding_mouse_event_started = False
            event.accept()

        else :
            return super().mouseReleaseEvent(event)

    def wheelEvent (self, event: QtGui.QWheelEvent) -> None :
        """Est l'événement appelée lorsque l'utilisateur bouge sa souris dans l'élément graphique."""

        if event.modifiers() == Qt.ControlModifier :

            self.zoom(event.angleDelta().y() / 120)
            event.accept()

        else :
            super().wheelEvent(event) 

    def zoom (self, value : int) -> None :
        
        if value == 0 :
            value = 1

        elif value > 0 :
            value *= 1.125

        elif value < 0 :
            value *= -0.825
        
        self.scale(value, value)

    def scene_elements_selected_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie la sélection d'éléments à l'écran."""
        self.elements_selected_changed.emit(self.selected_elements)
    
    def selected_elements (self) -> Iterable :
        """Permet de récuperer les éléments sélectionnés dans l'interface."""
        
        for item in self._diagram_model.scene.selected_elements() :
            yield item

class DiagramEditor (AbstractEditor) :
    """Est l'élément graphique capable d'éditer des simulation ou des boxes composites.""" 

    # -------------
    # Constructors
    # -------------

    def __init__ (self, tab_holder : QTabWidget, diagram_model : AbstractDiagramModel, actions_holder : ActionsHolder) :

        AbstractEditor.__init__(self, tab_holder, diagram_model, actions_holder)

        self._diagram_model = diagram_model
        self._graphics_view : GraphicsView = GraphicsView(self, self._actions_holder, diagram_model) 
        self._graphics_view.setGeometry(0, 0, self.width(), self.height())
        self._graphics_view.elements_selected_changed.connect(self.graphics_view_elements_selected_changed)
        self.setMouseTracking(True)

    # -------------
    # Properties
    # -------------

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model 
    
    # -------------
    # Methods
    # -------------

    def copy (self) -> None :
        
        serializer = {}
        serializer['MuPhyN'] = {}
        serializer['MuPhyN']['boxes'] = []
        serializer['MuPhyN']['signals'] = []

        box_copied = []
        for box_model in self.selected_elements() :
            if isinstance(box_model, BoxModel) :

                if not(box_model in box_copied) : 
                    box_copied.append(box_model)
                
        link_copied : List[AbstractLinkModel] = []
        for link_model in self.selected_elements() :
            if isinstance(link_model, AbstractLinkModel) :

                if link_model.input.parent() in box_copied and link_model.output.parent() in box_copied :
                
                    if link_model in link_copied :
                        continue

                    link_dict = exporter.export_signal(len(link_copied), link_model)
                    serializer['MuPhyN']['signals'].append(link_dict)
                    link_copied.append(link_model)

        for box_model in box_copied :

            box_dict = box_model.to_dict()

            # box_dict = exporter.export_box(box_model)

            # box_dict['inputs'] = [] 
            # for input_model in box_model.inputs : 
                
            #     input_dict = exporter.export_input(input_model)
            #     input_dict['signal_index'] = -1
            #     if len(input_model) > 0 :
            #         link : AbstractLinkModel = input_model._links[0]
            #         if link in link_copied :
            #             input_dict['signal_index'] = link_copied.index(link)

            #     box_dict['inputs'].append(input_dict)

            # box_dict['outputs'] = [] 
            # for output_model in box_model.outputs : 

            #     output_dict = exporter.export_output(output_model)
            #     output_dict['signal_indices'] = []

            #     for link in output_model._links :
            #         if link in link_copied :
            #             output_dict['signal_indices'].append(link_copied.index(link))

            #     box_dict['outputs'].append(output_dict)


            serializer['MuPhyN']['boxes'].append(box_dict)
        
        cb = QApplication.clipboard()
        cb.clear(mode = cb.Clipboard)
        cb.setText(yaml.dump(serializer).__str__())

    def cut (self) -> None :
        
        self.copy()
        self.delete_selection()

    def paste (self) -> None :

        cb = QApplication.clipboard()
        cb_text = cb.text().strip()

        if cb_text.__len__() == 0 :
            return

        action = DiagramPasteGraphicalElementAction(self, self.diagram_model, cb_text)
        action.do()
        self.actions_holder.append(action)

    def resizeEvent (self, event : QtGui.QResizeEvent) -> None :
        self._graphics_view.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(event)

    def graphics_view_elements_selected_changed (self, elements) -> None :
        """Est la méthode appelée lorsque l'utilisateur change la sélection."""
        self.elements_selected_changed.emit(elements)
    
    def selected_elements (self) -> Iterable :
        for item in self._graphics_view.selected_elements() :
            yield item

    def unslect_elements (self) -> None :
        for el in self.selected_elements() :
            el.setSelected(False) 

    def elements (self) -> Iterable[AbstractGraphicalElement] :
        for chld in self._graphics_view._diagram_model._graphical_elements :
            if isinstance(chld, AbstractGraphicalElement) :

                if isinstance(chld, InputConnectionModel) or isinstance(chld, OutputConnectionModel) :
                    continue

                yield chld 

    def zoom (self, value : int) -> None :
        self._graphics_view.zoom(value)

    def add_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.add_graphical_element(graphical_element)
        
    def rem_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.rem_graphical_element(graphical_element)

    def delete_selection (self) -> None :
        action = DiagramRemoveGraphicalElementAction(self._graphics_view._diagram_model, self.selected_elements())
        action.do()
        self.actions_holder.append(action)

    def clear (self) -> None :
        to_delete = []
        for el in self.elements() :
            if isinstance(el, AbstractLinkModel) :
                continue
            to_delete.append(el)

        for el in to_delete :
            self.rem_item(el)