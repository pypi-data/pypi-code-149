#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from datetime import date
from typing import Iterable

# Project Imports
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel

#-----------------------------------
# Class
#-----------------------------------

class BoxCompositeModel (AbstractBoxModel, AbstractDiagramModel) :
    """Est le modèle pour l'éditeur de box composite."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, name : str, path : str, creator : str, date : date, version : float, inputs : Iterable[BoxInputModel] = [], outputs : Iterable[BoxOutputModel] = [], graphical_elements : Iterable[AbstractGraphicalElement] = []) :
        
        AbstractBoxModel.__init__(self, name, path, creator, date, version, inputs, outputs)
        AbstractDiagramModel.__init__(self, graphical_elements)