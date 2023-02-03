#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict, Any
from muphyn.packages.interface.graphical_actions.abstract_diagram_action import AbstractDiagramAction
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.signals_model.abstract_signal_model import AbstractSignalModel

#-----------------------------------
# Class
#-----------------------------------

class DiagramAddGraphicalElementAction (AbstractDiagramAction) :
    """Est le type d'action qui permet d'ajouter des éléments dans l'écran."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, diagram_model : Any, constructors_ : List[Dict]) :
        
        AbstractDiagramAction.__init__(self, diagram_model)

        self._elements_indices = []
        self._constructors = constructors_
    
    # -------------
    # Methods
    # -------------

    def do (self) :
        
        for constructor in self._constructors :
            # Build Box Model
            box_model = BoxModel.fromBoxData(constructor['box_data'], position=constructor['pos'])

            # Add Box Model to diagram
            self.diagram_model.add_element(box_model)

            box_model_inputs = list(box_model.inputs)
            box_model_outputs = list(box_model.outputs)

            if 'graphical_index' in constructor :
                box_model.graphical_index = constructor['graphical_index']

                for input_index, input in enumerate(constructor['inputs']) :
                    box_model_inputs[input_index].graphical_index = input

                for output_index, output in enumerate(constructor['outputs']) :
                    box_model_outputs[output_index].graphical_index = output

            else :
                constructor['graphical_index'] = box_model.graphical_index
                constructor['inputs'] = []
                constructor['outputs'] = []

                for input in box_model.inputs : 
                    constructor['inputs'].append(input.graphical_index)

                for output in box_model.outputs : 
                    constructor['outputs'].append(output.graphical_index)

            self._elements_indices.append(box_model.graphical_index)

    def undo (self) :
        
        for graphical_element in self.diagram_model._graphical_elements :

            if graphical_element.graphical_index in self._elements_indices :

                if isinstance(graphical_element, AbstractSignalModel) :
                    graphical_element.unbind()

                self.diagram_model.remove_element(graphical_element)


            if len(self._elements_indices) == 0 : 
                break