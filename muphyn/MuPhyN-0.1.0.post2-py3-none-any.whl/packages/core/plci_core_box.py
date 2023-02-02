#-----------------------------------
# Imports
#-----------------------------------

import sys
from typing import Callable, Iterator, List, Any, Dict
from muphyn.packages.core.plci_core_data import Data

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.plci_core_signal_event import SignalEvent
from muphyn.packages.core.plci_core_scheduler_event import SchedulerEvent
from muphyn.packages.core.plci_core_signal import Signal

#-----------------------------------
# Class
#-----------------------------------

class Box :
    """Est la classe décrivant les boxes."""
    # -------------
    # Constructors
    # -------------

    def __init__ (  self, 
                    index_ : int, 
                    name_ : str,
                    library_ : str,
                    init_method_ : Callable[[Any], None] = None, 
                    function_ : Callable[[Any, SchedulerEvent], List[SignalEvent]] = None, 
                    end_method_ : Callable[[Any], None] = None, 
                    wait_for_events_ : bool = True,
                    wait_for_all_signal_events_ : bool = True, 
                    params_ : Dict[str, Any] = None) :
        
        self._index : int = index_
        self._name : str = name_
        self._library : str = library_
        
        if params_ is None :
            self._params : Dict[str, Any] = {}
        else :
            self._params : Dict[str, Any] = params_

        self._inputs : Dict[Signal, float] = {}
        self._outputs : List[Signal] = []

        self._wait_for_events : bool = wait_for_events_
        self._wait_for_all_signal_events : bool = wait_for_all_signal_events_

        self._current_timing : float = 0.0

        if (init_method_ == None) : 
            self._init_method : Callable[[Box], None] = lambda box, scheduler_params : ...
        else :
            self._init_method : Callable[[Box], None] = init_method_

        if (function_ == None) :
            self._function : Callable[[Box, SchedulerEvent], List[SignalEvent]] = lambda box, timing : []
        else :
            self._function : Callable[[Box, SchedulerEvent], List[SignalEvent]] = function_

        if (end_method_ == None) :
            self._end_method : Callable[[Box], None] = lambda box : ...
        else :
            self._end_method : Callable[[Box], None] = end_method_
        
    # -------------
    # Properties
    # -------------

    @property 
    def index (self) -> int :
        """Permet de récuperer l'index de la box."""
        return self._index

    @property
    def name (self) -> str :
        """Permet de récuperer le nom de la box."""
        return self._name

    @property
    def library (self) -> str :
        """Permet de récuperer la bibliothèque dans laquelle se trouve la box."""
        return self._library
    
    @property
    def inputs (self) -> List[Signal] :
        """Permet de récuperer les entrées de la box."""
        return self._inputs.keys()

    @property
    def outputs (self) -> List[Signal] :
        """Permet de récuperer les sorties de la box."""
        return self._outputs

    @property
    def params (self) -> Dict[str, Any] :
        """Permet de récuperer les paramètres de le box."""
        return self._params

    @property
    def wait_for_events (self) -> bool :
        """Permet de savoir si la box ne peut être utilisée que lors d'un événement."""
        return self._wait_for_events

    @property
    def wait_for_all_signal_events (self) -> bool :
        """Permet de savoir si la box ne peut être appelée que lorsque toutes ses entrées ont reçues un événement au timing actuel."""
        return self._wait_for_all_signal_events

    @property 
    def events_on_all_inputs (self) -> bool :
        """Permet de savoir si toutes les entrées ont bien reçues un événement au timing actuel."""
        for signal in self._inputs.keys() :
            if self._inputs[signal] < self.current_timing : 
                return False
        return True

    @property 
    def current_timing (self) -> float :
        """Permet de récuperer le timing de la box."""
        return self._current_timing


    # -------------
    # Methods
    # -------------

    def init (self, scheduler_params: SchedulerParams) -> None :
        """Permet de lancer la méthode d'initialisation de la box."""
        self._init_method(self, scheduler_params)

    def function (self, event_ : SchedulerEvent) -> List[SignalEvent] :
        """Permet de réaliser le traitement de la box et de modifier les éventuels sorties."""

        self._current_timing = event_.timing
        
        # Si on attend que des événements et que ce n'est pas un événement. On s'arrête
        if self.wait_for_events :
            if event_.signal is None :
                return []
            
        # Si c'est bien un événement, on modifie le timing de l'entrée concernée.
        if not event_.signal is None :
            self._inputs[event_.signal] = event_.timing
        
        # Si on attends tous les événement et qu'un événement n'est pas encore arrivé. On s'arrête.
        if self.wait_for_all_signal_events :
            if not self.events_on_all_inputs :
                return []

        # Activation de la box.
        return_data = self._function(self, event_)

        # Si l'activation n'a rien retourné, on produit quand même un tableau vide.
        if return_data is None :
            return_data : List[SchedulerEvent] = []

        # Retour du tableau d'activation.
        return return_data

    def end (self) -> None :
        """Permet d'appeler la méthode de fin de la box une fois que le planificateur a terminé."""
        self._end_method(self)

    def append_outputs (self, *outputs : Signal) -> None :
        """Permet d'ajouter autant de sorties que voulue à la box."""
        for output in outputs :
            self._outputs.append(output)

    def append_inputs (self, *inputs : Signal) -> None : 
        """Permet d'ajouter autant d'entrée que voulue à la box."""
        for input in inputs :
            self._inputs[input] = -1

    def get_input (self, input_index : int) -> Signal :
        """Permet de récuperer un index suivant son index dans la liste de la boite actuelle."""
        for input in self._inputs :
            if input_index == 0 :
                return input
            
            input_index -= 1

        return None

    def get_parameter(self, name: str):
        if name in self._params:
            return self._params[name]
        else:
            raise(Exception(f"No {name} parameter in Box parameters -> {[param for param in self._params]}"))

    def construct_signal_event (self, output : Signal, value : Any) -> SignalEvent :
        """Permet de générer des events signal."""
        

        if isinstance(value, float) :
            if output.signal_type == DataType.FLOAT :
                data = Data(DataType.FLOAT, value)

            elif output.signal_type == DataType.INT :
                data = Data(DataType.INT, int(value))

        elif isinstance(value, str) :
            data = Data(DataType.STRING, value)
        
        elif isinstance(value, int) :
            if output.signal_type == DataType.FLOAT :
                data = Data(DataType.FLOAT, float(value))

            elif output.signal_type == DataType.INT :
                data = Data(DataType.INT, value)

        elif isinstance(value, object) :
            data = Data(DataType.OBJECT, value)

        else :
            data = Data(DataType.UNDIFINED, value)
        
        return SignalEvent(output, self, data)

    def __str__ (self) :
        """Permet de retourner la box sous la forme d'un string."""
        self._params.__setitem__
        return "Box [" + self._library + " " + self._name + " | " + str(self._index) + "]"

    def __getitem__ (self, name : str) -> Any :
        """Permet de récuperer un objet des paramètres en utilisant les crochets."""

        if name in self._params :
            return self._params.__getitem__(name)

        else :
            return None

    def __setitem__ (self, name : str, obj : Any) -> None :
        """Permet de modifier un paramètre en utilisant les crochets."""
        self._params.__setitem__(name, obj) 
        self._params.__iter__()

    def __delitem__ (self, name : str) -> None :
        """Permet de supprimer un paramètre en utilisant son nom."""
        self._params.__delitem__(name)

    def __iter__ (self) -> Iterator[str] :
        """Permet d'itérer dans les paramètres."""
        return self._params.__iter__()

    if sys.version_info >= (3, 8):
        def __reversed__ (self) -> Iterator[str] :
            """Permet de récuperer la version inversée de la liste des paramètres."""
            return self._params.__reversed__()

    def __contains__ (self, obj : str) -> bool : 
        """Permet de savoir si l'a box cotient l'élément passé en in."""
        return self._params.__contains__(obj)
