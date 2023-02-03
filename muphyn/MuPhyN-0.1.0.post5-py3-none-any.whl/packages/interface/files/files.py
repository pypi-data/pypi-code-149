#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import os
import yaml

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.files.abstract_exporter import AbstractExporter
from muphyn.packages.interface.files.abstract_importer import AbstractImporter
from muphyn.packages.interface.files.simulation_files.simulation_exporter import SimulationExporter
from muphyn.packages.interface.files.simulation_files.simulation_importer import SimulationsImporter
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.models.editable_models.box_code_model import BoxCodeModel
from muphyn.packages.interface.models.editable_models.box_composite_model import BoxCompositeModel
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel 
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.editors.abstract_editor import AbstractEditor

#-----------------------------------
# Functions
#-----------------------------------

def load (path : str) -> AbstractEditableModel :
    """Permet de charger le modèle se trouvant au chemin passé en paramètre."""
    
    importer : AbstractImporter = None
        
    with open(path) as file_data : 

        yaml_data = yaml.load(file_data, Loader = yaml.FullLoader)
        
        name = os.path.basename(path)
        
        path = path[:-name.__len__()]
        if name.endswith('.yaml') :
            name = name[:-('.yaml'.__len__())]

        if 'simulation' in yaml_data :
            importer = SimulationsImporter()
            data = yaml_data['simulation']

        if importer is None : 
            return None

        return importer.open(data, path, name)

def save (model : AbstractEditableModel, path : str) -> bool :
    """Permet de sauvegarder le modèle au chemin passé en paramètre."""
    
    exporter : AbstractExporter = None

    if isinstance(model, SimulationModel):
        exporter = SimulationExporter()

    elif isinstance(model, BoxCompositeModel) :
        LogManager().debug('Save box composite !')
        raise Exception('no exporter found for box composite model')

    elif isinstance(model, SchedulerModel) :
        LogManager().debug('Save scheduler !')
        raise Exception('no exporter found for scheduler model')

    elif isinstance(model, BoxCodeModel) :
        LogManager().debug('Save box code !')
        raise Exception('no exporter found for box code model')

    return exporter.save(model, path)

def export (editor : AbstractEditor, argument : str) :
    """Permet d'exporter l'éditeur sous une forme voulue."""