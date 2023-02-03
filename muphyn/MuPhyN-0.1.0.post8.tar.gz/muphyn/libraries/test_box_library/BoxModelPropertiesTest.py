#-----------------------------------
# Imports
#-----------------------------------
import os
from typing import List
from muphyn.packages.core.plci_core_box import Box
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.core.simulation.om_sim import OpenModelicaSimulation
from muphyn.packages.core.simulation.model_parser.open_modelica_model_parser import OpenModelicaModelParser
from muphyn.packages.core.plci_core_scheduler_event import SchedulerEvent


"""
Notes:
 - If the initialization of the node is made in the _init_function then we won't access to the inputs first value 
    → (must implement a way to create firsts values)
 - If the outputs are read before the step is made we get one  step lag ;
 - If the inputs are set before the step then we get one step lag
"""

#-----------------------------------
# Functions
#-----------------------------------
def _step_simumation (box: Box, event_: SchedulerEvent) -> List :
    pass

def _finish_simulation (box: Box) -> List :
    for name, value in box.params.items():
        print(name, value)
    return []