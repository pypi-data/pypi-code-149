#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import yaml
from typing import Any, Dict

# PyQt5 Imports
from PyQt5.QtCore import QPointF

# Project Imports
from muphyn.packages.interface.graphical_actions.abstract_diagram_action import AbstractDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

#-----------------------------------
# Class
#-----------------------------------

class DiagramPasteGraphicalElementAction (AbstractDiagramAction) :
    """Est l'action capable de coller le contenus d'une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, diagram_editor, diagram_model : Any, content_paste : str) :
        
        AbstractDiagramAction.__init__(self, diagram_model)

        self._serialized_diagram = None
        self._diagram_editor = diagram_editor
        self._content_paste = content_paste
        self._elements_indices = []

    # -------------
    # Methods
    # -------------

    def set_or_get_graphical_index (self, age : AbstractGraphicalElement, dictionary : Dict) -> None :
        """Permet de récuperer ou de sélectionner le graphical index pour l'élément passé en paramètre."""
        
        if 'graphical_index' in dictionary : 
            age.graphical_index = dictionary['graphical_index']
        
        else :
            dictionary['graphical_index'] = age.graphical_index
            self._should_reload = True

            if isinstance(age, SignalLinkModel) or isinstance(age, AbstractBoxModel) : 
                if not(age.graphical_index in self._elements_indices) :
                    self._elements_indices.append(age.graphical_index)

    def do (self) :
        
        self._diagram_editor.unslect_elements()

        if self._serialized_diagram is None : 
            self._serialized_diagram = yaml.load(self._content_paste, yaml.FullLoader)

        if 'MuPhyN' in self._serialized_diagram :
            
            signals = self._serialized_diagram['MuPhyN']['signals']
            
            for signal in signals : 
                signal['input'] = None
                signal['output'] = None

            for box_dict in self._serialized_diagram['MuPhyN']['boxes'] :
                # Build new Box Model from data dict
                box_model = BoxModel.fromDict(box_dict)

                # Move new Box Model
                box_model.setPos(box_model.pos() + QPointF(box_model.size.width()/2, box_model.size.height()/2))

                # Get Graphical Index of new box
                self.set_or_get_graphical_index(box_model, box_dict)

                # Add new Box Model to diagram editor
                self._diagram_model.add_element(box_model)

                # Set new Box Model as selected
                box_model.setSelected(True)

    def undo (self) :
        
        for element_index in self._elements_indices :

            element = self.diagram_model.get_element_by_graphical_index(element_index)

            if element is None : 
                continue

            if isinstance(element, SignalLinkModel) :
                element.unbind()
                self.diagram_model.remove_element(element)

        for element_index in self._elements_indices :

            element = self.diagram_model.get_element_by_graphical_index(element_index)

            if element is None : 
                continue

            if not(isinstance(element, SignalLinkModel)) :
                self.diagram_model.remove_element(element)