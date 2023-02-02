#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Iterable, List

# PyQt5 Imports
from PyQt5.QtWidgets import QGraphicsScene

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.links_model.link_type import LinkType
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder

#-----------------------------------
# Class
#-----------------------------------

class AbstractDiagramModel :
    """ESt la classe abstraite commune aux modèles des éléments graphiques capables de modifier des diagrammes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_elements : Iterable[AbstractGraphicalElement] = []) :

        self._scene = None
        self._graphical_elements : List[AbstractGraphicalElement] = list(graphical_elements)

    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur d'action."""
        if hasattr(self._scene, 'actions_holder') :
            return self._scene.actions_holder

        return None
    
    @property
    def editor_type (self) -> str :
        """Permet de récuperer le type d'éditeur à utiliser."""
        return "diagram-editor"

    @property
    def graphical_elements (self) -> Iterable[AbstractGraphicalElement] :
        """Permet de récuperer la liste des éléments graphiques affichés dans l'interface graphique."""
        return self._graphical_elements
        
    @property
    def selected_elements (self) -> Iterable[AbstractGraphicalElement] :
        """Permet de récuperer la liste des éléments graphiques sélectionnés."""

        for graphic_element in self._graphical_elements :

            if graphic_element.isSelected() :
                yield graphic_element
                
    @property
    def elements_len (self) -> int :
        """Permet de récuperer le nombre d'éléments graphiques contenus dans le modèle."""
        return self._graphical_elements.__len__()

    @property
    def box (self) -> Iterable[AbstractBoxModel] :
        """Permet de récuperer la liste des éléments graphiques qui sont des boxes."""
        
        for graphic_element in self._graphical_elements :
            if isinstance(graphic_element, AbstractBoxModel) :
                yield graphic_element

    @property
    def scene (self) -> QGraphicsScene :
        """Permet de récuperer la scène dans auquel est liée le modèle."""
        return self._scene

    @scene.setter
    def scene (self, scene_ : QGraphicsScene) -> None : 
        """Permet de modifier la scène du diagramme."""

        if not(self._scene is None) :
            for el in self._graphical_elements :
                if el in self._scene.items() :
                    self._scene.removeItem(el) 

        self._scene = scene_

        if not(self._scene is None) :
            
            for el in self._graphical_elements : 
                if not(el in self._scene.items()) :
                    self._scene.addItem(el)

    # -------------
    # Methods
    # -------------

    def __len__ (self) -> int :
        """Permet de récuperer le nombre d'éléments contenus dans le modèle de diagramme."""
        return self._graphical_elements.__len__()

    def add_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet d'ajouter un élément au modèle."""
        
        if graphical_element is None :
            return

        self._graphical_elements.append(graphical_element)
        graphical_element.diagram_model = self
        
        if not(self._scene is None) :
            self._scene.addItem(graphical_element)

    def remove_element (self, graphical_element : AbstractGraphicalElement) -> None : 
        """Permet de supprimer un élément du modèle."""
        
        if graphical_element is None : 
            return
        
        if not(self._scene is None) :
            self._scene.removeItem(graphical_element)
            graphical_element.deleteLater()

        graphical_element.diagram_model = None
        self._graphical_elements.remove(graphical_element)

    def link_nodes (self, input_, output, input_index : int = -1, output_index : int = -1, link_value : float = 0.5, link_type : LinkType = LinkType.SQUARE, link_text : str = '') -> SignalLinkModel :
        """Permet de relier deux noeuds."""
            
        if input_ is None :
            return None

        if output is None :
            return None

        if input_index == -1 :
            input_index = len(input_)

        if output_index == -1 :
            output_index = len(output)

        if isinstance(input_, InputConnectionModel) and isinstance(output, OutputConnectionModel) :
            
            if not(input_.data_type == output.data_type) :
                LogManager().error('input_ and output does not have the same type.')
                return

            if len(input_) > 0 : 
                LogManager().error('the input_ has already a link')
                return
            
            link : SignalLinkModel = SignalLinkModel(output.data_type, input_, output, link_type, link_text)
            link.link_value = link_value

            output.insert_link(output_index, link)
            input_.add_link(link)
            
            self.add_element(link)

            return link
        
        else :
            LogManager().error('input_ and output cannot be bound.')

    def get_element_by_graphical_index (self, graphical_index : int) -> AbstractGraphicalElement : 
        """Permet de récuperer un élément graphique grâce à son index."""

        for el in self.graphical_elements :
            if el.graphical_index == graphical_index :
                return el

        for el in self.graphical_elements :
            if isinstance(el, AbstractBoxModel) :
                for input_ in el.inputs :
                    if input_.graphical_index == graphical_index :
                        return input_

                for output in el.outputs :
                    if output.graphical_index == graphical_index :
                        return output

        return None