#-----------------------------------
# Imports
#-----------------------------------

from datetime import date
from typing import Iterable
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.editable_models.abstract_code_model import AbstractCodeModel
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel

#-----------------------------------
# Class
#-----------------------------------

class BoxCodeModel (AbstractBoxModel, AbstractCodeModel) :
    """Est le model des boxes dont le comportement est décrit par du code."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, path : str, creator : str, date : date, version : float, code : str = '', inputs : Iterable[BoxInputModel] = [], outputs : Iterable[BoxOutputModel] = []) : 
        
        AbstractBoxModel.__init__(self, name, path, creator, date, version, inputs, outputs)
        AbstractCodeModel.__init__(self, code)