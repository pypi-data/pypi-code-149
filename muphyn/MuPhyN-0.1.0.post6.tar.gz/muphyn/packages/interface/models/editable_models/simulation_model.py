#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from datetime import date
from typing import Iterable

# Project Imports
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class SimulationModel (AbstractEditableModel, AbstractDiagramModel) :
    """Est le modèle pour l'éditeur de simulation."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, name : str, path : str, creator : str, date : date, version : float, scheduler_model : SchedulerModel, graphical_elements : Iterable[AbstractGraphicalElement] = []) :
        
        AbstractEditableModel.__init__(self, name, path, creator, date, version)
        AbstractDiagramModel.__init__(self, graphical_elements)
        
        self._scheduler_model : SchedulerModel = scheduler_model

    # -------------
    # Properties
    # -------------

    @property
    def scheduler_model (self) -> SchedulerModel :
        """Permet de récuperer le modèle de planificateur."""
        return self._scheduler_model

    @scheduler_model.setter
    def scheduler_model (self, scheduler_model_ : SchedulerModel) -> None :
        """Permet de modifier le modèle de planificateur."""
        self._scheduler_model = scheduler_model_