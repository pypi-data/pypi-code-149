
# PyQt5 imports
from PyQt5.QtWidgets import QTabWidget

# Project imports
from muphyn.packages.interface.editors.abstract_editor import AbstractEditor
from muphyn.packages.interface.editors.diagram_editor import GraphicsView
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.graphical_actions.diagram_add_graphical_element_action import DiagramAddGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_paste_graphical_element_action import DiagramPasteGraphicalElementAction
from muphyn.packages.interface.graphical_actions.diagram_remove_graphical_element_action import DiagramRemoveGraphicalElementAction
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel

class MultiPhysicsDiagramEditor(AbstractEditor):

    def __init__(self, tab_holder: QTabWidget, diagram_model: AbstractDiagramModel, actions_holder: ActionsHolder):
        super().__init__(tab_holder, diagram_model, actions_holder)

        # Add graphics view
        self._graphics_view : GraphicsView = GraphicsView(self, self._actions_holder, diagram_model) 
        self._graphics_view.setGeometry(0, 0, self.width(), self.height())

        # Activate mouse tracking
        self.setMouseTracking(True)

    # -------------
    # Properties
    # -------------
    @property
    def diagram_model(self) -> AbstractDiagramModel:
        return self._editable_model

    # -------------
    # Core Methods
    # -------------
    def add_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet d'ajouter un élément graphique à l'interface."""

        if graphical_element is None :
            return

        self.diagram_model.add_element(graphical_element)

    def rem_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet de supprimer un élément graphique de l'interface."""

        self.diagram_model.remove_element(graphical_element)
        graphical_element.deleteLater()

    def add_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.add_graphical_element(graphical_element)
        
    def rem_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.rem_graphical_element(graphical_element)

    def clear (self) -> None :
        to_delete = [el for el in self.elements() if not isinstance(el, AbstractLinkModel)]
        for el in to_delete :
            self.rem_item(el)

    # -------------
    # Graphical Methods
    # -------------
    def delete_selection (self) -> None :
        action = DiagramRemoveGraphicalElementAction(self._graphics_view._diagram_model, self.selected_elements())
        action.do()
        self.actions_holder.append(action)

class OpenModelicaDiagramEditor(MultiPhysicsDiagramEditor):

    def __init__(self, tab_holder: QTabWidget, diagram_model: AbstractDiagramModel, actions_holder: ActionsHolder):
        super().__init__(tab_holder, diagram_model, actions_holder)