
#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, List, Any, Dict

from muphyn.utils.paths import ROOT_DIR

from ..plci_core_box import Box
from ..plci_core_data import Data
from ..plci_core_data_type import DataType, get_data_type
from ..plci_core_diagram import Diagram
from ..plci_core_signal import Signal
from ..plci_core_signal_event import SignalEvent
from ..plci_core_scheduler_event import SchedulerEvent

#-----------------------------------
# Methods
#-----------------------------------

def construct_diagram (signals : Dict, boxes : Dict, inputs : Dict, outputs : Dict, box_params : Dict[str, Any], boxes_library : Any) -> Diagram :
   
    diagram = Diagram()
    
    for signal_data in signals :
        
        data_type : DataType = get_data_type(signal_data['type'])
        signal : Signal = Signal(signal_data['index'], data_type, signal_data['value']) 
        diagram.append(signal)

    for box_data in boxes :

        params = box_data['params']
        if params == 'None' :
            box = boxes_library.construct_box(box_data['library'], box_data['name'])
        else :
            box = boxes_library.construct_box(box_data['library'], box_data['name'], **params)
        
        if isinstance(box, Diagram) :
            diagram.append(box)

            if not box_data['inputs'] == 'None' :

                for signal_index, input in enumerate(box_data['inputs']) :
                    signal = diagram.signals[input['signal_index']]
                    
                    input_signal = box.signals[box.inputs[signal_index]]
                    diagram.add_linked_signals(signal, input_signal)

            if not box_data['outputs'] == 'None' :

                for signal_index, output in enumerate(box_data['outputs']) :
                    signal = diagram.signals[output['signal_index']]
                    
                    output_signal = box.signals[box.outputs[signal_index]]
                    diagram.add_linked_signals(output_signal, signal)

        elif isinstance(box, Box) :
            diagram.append(box)

            if not box_data['inputs'] == 'None' :

                for box_input_data in box_data['inputs'] :
                    diagram.add_box_inputs(box, diagram.signals[box_input_data['signal_index']])

            if not box_data['outputs'] == 'None' :
                
                for box_output_data in box_data['outputs'] :
                    diagram.add_box_outputs(box, diagram.signals[box_output_data['signal_index']])

    for input in inputs :
        diagram.inputs.append(input['signal_index'])

    for output in outputs :
        diagram.outputs.append(output['signal_index'])

    return diagram


#-----------------------------------
# Classes
#-----------------------------------

class AbstractBoxData : 
    """Est la classe commune des classes de données de bibliothèque."""

    # -------------
    # Constructors
    # -------------

    def __init__ (
            self, 
            box_name: str, 
            box_library: str, 
            box_type: str,
            creator: str,
            date_created: Any,
            version: float,
            inputs,
            outputs,
            icon: str = None
        ) :
        self._box_name = box_name
        self._box_library = box_library
        self._box_type = box_type
        self._creator : str = creator
        self._date_created : Any = date_created
        self._version : float = version
        self._inputs: dict[str, dict] = inputs
        self._outputs: dict[str, dict] = outputs
        self._full_box_path = self._box_library + '.' + self._box_name
        if icon is not None:
            self._icon = ROOT_DIR + "/" + icon
        else:
            self._icon = None

    # -------------
    # Properties
    # -------------

    @property 
    def box_name (self) -> str :
        """Permet de récuperer le nom de la box."""
        return self._box_name

    @property
    def box_library (self) -> str :
        """Permet de récuperer la bibliothèque dans laquel se trouve la box."""
        return self._box_library

    @property
    def box_type (self) -> str :
        """Permet de récuperer la bibliothèque dans laquel se trouve la box."""
        return self._box_type

    @property
    def creator (self) -> str :
        """Permet de récuperer le nom de la personne qui a créé la box."""
        return self._creator

    @property
    def date_created (self) -> Any :
        """Permet de récuperer la date à laquelle la box a été créée."""
        return self._date_created

    @property
    def version (self) -> float :
        """Permet de récuperer la version de la box."""
        return self._version

    @property
    def inputs (self) :
        """Permet de récuperer la liste des signaux considérés comme entrées."""
        return self._inputs

    @property
    def outputs (self) :
        """Permet de récuperer la liste des signaux considérés comme sorties."""
        return self._outputs

    @property
    def full_box_path (self) -> str :
        """Permet de récuperer le nom complet de la boite (bibliothèque + nom)."""
        return self._full_box_path

    @property
    def icon(self) -> str:
        return self._icon

    # -------------
    # Methods
    # -------------

    def __lt__ (self, other) :
        return self._full_box_path.__lt__(other._full_box_path) 


    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Any :
        """Permet de générer la box."""
        raise Exception('AbstractBoxData construct_box is an abstract method and must be overriden !')

class CompositeBoxData (AbstractBoxData) :
    """Est la classe qui permet de contenir les données des boxes composites."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (
            self, 
            box_name : str, 
            box_library : str, 
            creator : str,
            date_created : Any,
            version : float,
            signals, 
            boxes, 
            inputs, 
            outputs,
            icon: str = None
        ) :
        AbstractBoxData.__init__(self, box_name, box_library, creator, date_created, version, inputs, outputs, icon)
        self._signals = signals
        self._boxes = boxes
    
    # -------------
    # Properties
    # -------------
    
    def signals (self) :
        """Permet de récuperer le dictionnaire contenant la composition des signaux de la box composite."""
        return self._signals

    def boxes (self) :
        """Permet de récuperer le dictionnaire contenant la composition des boxes de la box composite."""
        return self._boxes

    # -------------
    # Methods
    # -------------

    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Diagram :
        """Permet de générer la box."""
        
        return construct_diagram(self._signals, self._boxes, self._inputs, self._outputs, box_params, boxes_library)

class CodeBoxData (AbstractBoxData) :
    """Est la classe qui permet de contenir les données des boxes importées par un bibliothèque."""

    # -------------
    # Constructors
    # -------------
    def __init__ (
            self, 
            box_name : str, 
            box_library : str, 
            box_type: str,
            wait_for_event : bool, 
            wait_for_all_signal_events : bool,
            params : Dict[str, Data], 
            box_init_method_ : Callable[[Box], None], 
            box_function_ : Callable[[Box, SchedulerEvent], List[SignalEvent]], 
            box_end_method_ : Callable[[Box], None],
            creator : str,
            date_created : Any,
            version : float, 
            inputs,
            outputs,
            icon: str = None
        ) :

        AbstractBoxData.__init__(self, box_name, box_library, box_type, creator, date_created, version, inputs, outputs, icon)
        self._init_method : Callable[[Box], None] = box_init_method_
        self._box_function : Callable[[Box, SchedulerEvent], List[SignalEvent]] = box_function_
        self._end_mehtod : Callable[[Box], None] = box_end_method_
        self._params : Dict[str, Data] = params
        self._wait_for_event = wait_for_event
        self._wait_for_all_signal_events = wait_for_all_signal_events

    # -------------
    # Properties
    # -------------

    @property
    def init_method (self) -> Callable[[Box], None] :
        """Permet de récuperer la méthode d'initialisation de la box."""
        return self._init_method
    
    @property
    def box_function (self) -> Callable[[Box, SchedulerEvent], List[SignalEvent]] :
        """Permet de récuperer la fonction de la box."""
        return self._box_function

    @property
    def end_method (self) -> Callable[[Box], None] :
        """Permet de récuperer la méthode de fin de la box."""
        return self._end_mehtod

    @property
    def params (self) -> Dict[str, Data] : 
        """Permet de récuperer tous les paramètres requis pour la génération de ce type de box."""
        return self._params

    @property 
    def wait_for_event (self) -> bool :
        """Permet de récuperer le fait qu'il faille attendre un événement pour que la box puisse s'activer."""
        return self._wait_for_event

    @property
    def wait_for_all_signal_events (self) -> bool :
        """Permet de récuperer le fait qu'il faille que toutes les entrées de la box aie eu des événements au timing actuel pour qu'elle s'active."""
        return self._wait_for_all_signal_events

    # -------------
    # Methods
    # -------------
    
    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Box :
        """Permet de générer la box."""
        return Box(
                    index_ = index,
                    name_ = self.box_name,
                    library_ = self.box_library,
                    init_method_ = self.init_method,
                    function_ = self.box_function,
                    end_method_ = self.end_method,
                    wait_for_events_ = self.wait_for_event,
                    wait_for_all_signal_events_ = self.wait_for_all_signal_events,
                    params_ = box_params
                )

class MultiPhysicsSimulationBoxData(CodeBoxData):
    def __init__(self, box_name: str, box_library: str, box_type: str, wait_for_event: bool, wait_for_all_signal_events: bool, params: Dict[str, Data], box_init_method_: Callable[[Box], None], box_function_: Callable[[Box, SchedulerEvent], List[SignalEvent]], box_end_method_: Callable[[Box], None], creator: str, date_created: Any, version: float, inputs, outputs, icon: str = None):
        super().__init__(box_name, box_library, box_type, wait_for_event, wait_for_all_signal_events, params, box_init_method_, box_function_, box_end_method_, creator, date_created, version, inputs, outputs, icon)

    @staticmethod
    def fromCodeBoxData(code_box_data: CodeBoxData):

        return MultiPhysicsSimulationBoxData(
            code_box_data.box_name,
            code_box_data.box_library,
            code_box_data.box_type,
            code_box_data.wait_for_event,
            code_box_data.wait_for_all_signal_events,
            code_box_data.params,
            None if not hasattr(code_box_data, "box_init_method_") else code_box_data.box_init_method_, 
            None if not hasattr(code_box_data, "box_function_") else code_box_data.box_function_, 
            None if not hasattr(code_box_data, "box_end_method_") else code_box_data.box_end_method_,
            code_box_data.creator,
            code_box_data.date_created,
            code_box_data.version,
            code_box_data.inputs,
            code_box_data.outputs,
            code_box_data.icon
        )