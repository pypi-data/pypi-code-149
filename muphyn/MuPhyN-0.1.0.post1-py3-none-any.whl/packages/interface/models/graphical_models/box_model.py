#-----------------------------------
# Imports
#-----------------------------------
import copy
import traceback
from typing import Iterable, Any, Dict

from PyQt5.QtCore import QPointF, QSizeF
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData

from muphyn.packages.core.plci_core_data_type import DataType, get_data_type
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel, BoxType
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager

#-----------------------------------
# Class
#-----------------------------------

class BoxModel (AbstractBoxModel) :
    """Est le model graphique des boxes affichées à l'écran."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, library : str, name : str, position : QPointF, size : QSizeF, rotation : float, 
                  can_be_loaded : bool = True, text : str = '', icon: str = None) :
        
        self._library = library
        self._parameters : Dict[str, Any]= {}

        if library == "Boxes.Sources":
            box_type = BoxType.Source
        elif library == "Boxes.Signals":
            box_type = BoxType.Signal
        else:
            box_type = BoxType.Math

        AbstractBoxModel.__init__(self, name, position, size, rotation, text, box_type, icon, None)

        self._can_be_loaded : bool = can_be_loaded
        self.setZValue(1)

    # -------------
    # Properties
    # -------------

    @property
    def library (self) -> str : 
        """Permet de récuperer le nom de la bibliothèque dans laquelle se trouve la box."""
        return self._library

    @library.setter
    def library (self, library_ : str) -> None :
        """Permet de modifier le nom de la bibliothèque dans laquelle se trouve la box."""
        self._library = library_ or ''

    @property
    def can_be_loaded (self) -> bool :
        """Permet de savoir si la box actuelle est bien présente dans la bibliothèques."""
        return self._can_be_loaded

    @can_be_loaded.setter
    def can_be_loaded (self, can_be_loaded_ : bool) -> None : 
        """Permet de modifier le fait que la box actuelle est bien présente dans la bibliothèque."""
        self._can_be_loaded : bool = can_be_loaded_

    @property
    def rendered_text (self) -> str :
        return super().rendered_text

    @rendered_text.setter
    def rendered_text(self, rendered_text_ : str) -> None :

        self._text = rendered_text_

    # -------------
    # Methods
    # -------------

    def set_parameter (self, name : str, value : object) -> None :
        """Permet de modifier la valeur du paramètre.""" 

        old_value = self._parameters[name]['value']
        if value == old_value :
            return

        parameter = self._parameters[name]

        # Set Value
        parameter['value'] = value

        # Handle callback
        if "callback" in parameter:
            callback = parameter["callback"]
            try:
                callback(self)
            except:
                LogManager().error(traceback.format_exc())

        if self._action_param_semaphore:
            return
            
        self.param_changed.emit(self, 'params.'+name, old_value, value)
    
    def get_parameter (self, name : str) -> Dict :
        """Permet de récuperer les données d'un paramètre."""
        return self._parameters[name]

    def get_parameters (self) -> Iterable[str] :
        """Permet de récuperer la liste des paramètres."""
        for key in self._parameters :
            yield key

    def get_parameters_len (self) -> int :
        """Permet de récuperer la taille du tableau de paramètres."""
        return self._parameters.__len__()

    def create_parameter(self, parameter_name : str, parameter_type : DataType, parameter_value : object) -> None :
        """Permet de créer un slot pour le paramètre voulu."""
        self._parameters[parameter_name] = {}
        self._parameters[parameter_name]['type'] = parameter_type
        self._parameters[parameter_name]['value'] = parameter_value

    def to_dict(self) -> dict:
        box_dict = {
            "name": self.name,
            "library": self.library,
            "text": self.text,
            "geometry": {
                "x": self.x(),
                "y": self.y(),
                "width": self.size.width(),
                "height": self.size.height(),
                "rotation": self.rotation()
            },
            "inputs_groups": [],
            "outputs_groups": [],
            "params": {param: self.get_parameter(param)['value'] for param in self.get_parameters()}
        }

        return box_dict

    def reconstructor(self):
        pass

    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def fromBoxData(
            box_data: AbstractBoxData, 
            position: QPointF = QPointF(0, 0), 
            size: QSizeF = QSizeF(AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight),
            rotation: float = 0
        ):

        # Handle Geometry value
        ## Size
        if size.width() < AbstractBoxModel.MinimunBoxWidth:
            size.setWidth(AbstractBoxModel.MinimunBoxWidth)
        if size.height() < AbstractBoxModel.MinimunBoxHeight:
            size.setHeight(AbstractBoxModel.MinimunBoxHeight)
        
        ## Rotation
        rotation = ((rotation // 90) % 4) * 90

        # Build Box Model
        box_model = BoxModel(
            library=box_data.box_library,
            name=box_data.box_name,
            position=position,
            size=QSizeF(AbstractBoxModel.MinimunBoxWidth, AbstractBoxModel.MinimunBoxHeight),
            rotation=0, can_be_loaded=True, text="", icon=box_data.icon
        )

        box_model.box_type = box_data.box_type

        # Inputs
        box_model.add_inputs_groups(box_data.inputs)

        # Outputs
        box_model.add_outputs_groups(box_data.outputs)

        # Add default params value
        if hasattr(box_data, 'params') :
            for parameter, attributes in box_data.params.items() :
                # Copy parameter
                box_model._parameters[parameter] = copy.deepcopy(attributes)

        return box_model

    @staticmethod
    def fromDict(box_dict: dict):
        """Est la méthode appelée pour produire un modèle de box suivant un dictionnaire d'import."""

        # Get genral box informations
        library = box_dict['library']
        name = box_dict['name']

        #
        text = box_dict['text']

        # Get geometry
        position = QPointF(float(box_dict['geometry']['x']), float(box_dict['geometry']['y']))
        size = QSizeF(float(box_dict['geometry']['width']), float(box_dict['geometry']['height']))
        rotation = float(box_dict['geometry']['rotation'])

        # Build Box from BoxData
        box_data = BoxesLibrariesManager().get_box_data(library, name)
        
        # Handle Geometry value
        ## Size
        if size.width() < AbstractBoxModel.MinimunBoxWidth:
            size.setWidth(AbstractBoxModel.MinimunBoxWidth)
        if size.height() < AbstractBoxModel.MinimunBoxHeight:
            size.setHeight(AbstractBoxModel.MinimunBoxHeight)
        
        ## Rotation
        rotation = ((rotation // 90) % 4) * 90

        # Build Box Model
        box_model = BoxModel(
            library=box_data.box_library,
            name=box_data.box_name,
            position=position,
            size=size,
            rotation=rotation, can_be_loaded=True, text=text, icon=box_data.icon
        )
        
        box_model.box_type = box_data.box_type

        # Inputs
        box_model.add_inputs_groups(box_data.inputs, infinite_groups_reset=True)

        # Outputs
        box_model.add_outputs_groups(box_data.outputs, infinite_groups_reset=True)
        
        # Set Parameter values
        if hasattr(box_data, 'params') :
            for parameter, attributes in box_data.params.items() :
                # Copy parameter
                box_model._parameters[parameter] = copy.deepcopy(attributes)

                # Set with new value
                if parameter in box_dict["params"]:
                    box_model.set_parameter(parameter, box_dict["params"][parameter])


        return box_model