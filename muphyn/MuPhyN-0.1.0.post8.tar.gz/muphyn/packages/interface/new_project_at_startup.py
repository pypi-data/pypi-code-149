#-----------------------------------
# Imports
#-----------------------------------
 
import os
import pathlib
from datetime import date

from PyQt5.QtCore import QCoreApplication

from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.user_data.user_data import UserData
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel

#-----------------------------------
# Functions
#-----------------------------------

def new_project_on_startup (user_data : UserData, schedulers_libraries : SchedulersLibraries) -> SimulationModel :
    """Permet de créer un nouveau projet vide au démarrage du projet."""

    name = QCoreApplication.translate("_new_project_on_startup", "New Project", None)
    path = pathlib.Path(__file__).parent.parent.parent.absolute().__str__() + os.sep.__str__()
    
    creator = user_data.user_name
    _date = date.today() 
    version = 1.0

    step_time = 0.1
    stop_time = 10
    
    scheduler = None
    for sch in schedulers_libraries.schedulers :
        scheduler = sch
        break

    scheduler_params = SchedulerParams(stop_time, step_time)
    if not(scheduler is None) :
        scheduler_model : SchedulerModel = SchedulerModel(scheduler.scheduler_library, scheduler.scheduler_name, scheduler_params)
    else : 
        scheduler_model : SchedulerModel = SchedulerModel('', '', scheduler_params)
    
    return SimulationModel(name, path, creator, _date, version, scheduler_model)