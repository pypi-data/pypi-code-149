#-----------------------------------
# Imports
#-----------------------------------

from datetime import date
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel

#-----------------------------------
# Class
#-----------------------------------

class SchedulerEditorModel (AbstractEditableModel) :
    """Est la classe qui décrit les données contenues dans un éditeur de planificateur."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, name : str, path : str, creator : str, date : date, version : float, code : str = '') :
        
        AbstractEditableModel.__init__(self, name, path, creator, date, version)
        