#-----------------------------------
# Imports
#-----------------------------------

import math
from typing import Callable, List, Any
from muphyn.packages.core.plci_core_data import Data

from muphyn.packages.core.plci_core_scheduler_exception import SchedulerException

from .plci_core_scheduler_params import SchedulerParams
from .plci_core_scheduler_event import SchedulerEvent
from .plci_core_signal_event import SignalEvent
from .plci_core_signal import Signal
from .plci_core_box import Box
from .plci_core_diagram import Diagram


def round_step_size(quantity, step_size) -> float:
    """Rounds a given quantity to a specific step size
    :param quantity: required
    :param step_size: required
    :return: decimal
    """
    precision: int = int(round(-math.log(step_size, 10), 0))
    return float(round(quantity, precision))

#-----------------------------------
# Class
#-----------------------------------

class Scheduler :
    """Est la classe qui permet de résoudre les simulation basé sur des diagrammes de boxes."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, scheduler_name_ : str, function_ : Callable[[Any], SchedulerException]) :
        
        if function_ is None :
            self._function : Callable[[Any], SchedulerException] = lambda scheduler : ...

        else : 
            self._function = function_

        self._scheduler_name = scheduler_name_
        self._current_time : float = 0
        self._events : List[SignalEvent] = []
        self._diagram : Diagram = Diagram()
        self._scheduler_params : SchedulerParams = SchedulerParams


    # -------------
    # Properties
    # -------------

    @property
    def diagram (self) -> Diagram :
        """Permet de récuperer le diragramme à résoudre."""
        return self._diagram

    @diagram.setter
    def diagram (self, diagram_ : Diagram) -> None :
        """Permet de modifier le diagramme de simulation."""
        self._diagram = diagram_

    @property
    def params (self) -> SchedulerParams :
        """Permet de récuperer les paramètres de la simulation."""
        return self._scheduler_params

    @params.setter
    def params (self, scheduler_params_ : SchedulerParams) -> None :
        """Permet de modifier les paramètres de simulation."""
        self._scheduler_params = scheduler_params_

    @property
    def step_time (self) -> float :
        """Permet de récuperer le temps de step de la simulation."""
        return self._scheduler_params.step_time

    @property
    def stop_time (self) -> float :
        """Permet de récuperer le temps maximal de la simulation."""
        return self._scheduler_params.stop_time

    @property 
    def current_time (self) -> float :
        """Permet de récuperer le temps de simulation acutel."""
        return self._current_time

    @property
    def scheduler_name (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return self._scheduler_name

    @property 
    def events_count (self) -> int :
        """Permet de récuperer le nombre d'événements dans la liste."""
        return len(self._events)

    @property
    def are_events_left (self) -> bool :
        """Permet de savoir si il reste des événements à réaliser."""
        return len(self._events) > 0

    @property 
    def should_simulation_continue (self) -> bool :
        """Permet de savoir si le temps de simulation n'a pas dépassé encore le temps final de simulation."""
        return self.current_time <= self._scheduler_params.stop_time
    
    # -------------
    # Methods
    # -------------

    def schedule (self, diagram : Diagram = None, params : SchedulerParams = None) -> SchedulerException :
        """Permet de résoudre le diagramme."""

        exc = self._scheduler_call_init()
        if not exc is None :
            return exc
        
        exc = self._function(self)
        if not exc is None :
            return exc
        
        exc = self._scheduler_call_end()
        if not exc is None :
            return exc

        return None

    
    def _scheduler_call_init (self, diagram : Diagram = None) -> SchedulerException :
        """Permet d'appeler la méthode init des boxes contenues dans le diagramme."""
        try :
            for box in self.diagram.boxes :
                box.init(self._scheduler_params)

        except Exception as err :
            return SchedulerException(box, None, None, None, self.diagram, 0, err)

        return None

    def _scheduler_call_end (self) -> SchedulerException :
        """Permet d'appeler la méthode end des boxes contenues dans le diagramme."""
        
        try :
            for box in self.diagram.boxes :
                box.end()

        except Exception as err :
            return SchedulerException(box, None, None, None, self.diagram, self.current_time, err)

        return None

    def stepping_time (self) -> None :
        """Permet d'avancer d'un pas de temps."""
        self._current_time += self._scheduler_params.step_time
        self._current_time = round_step_size(self._current_time, self._scheduler_params.step_time)

    def insert_event (self, position_ : int, signal_event_ : SignalEvent) -> None :
        """Permet d'insérer un évenements dans la liste à un index donné."""
        self._events.insert(position_, signal_event_)

    def append_event (self, signal_event_ : SignalEvent) -> None :
        """Permet d'ajouter un événement à la fin de la liste des événements."""
        self._events.append(signal_event_)

    def remove_event (self, signal_event : SignalEvent) -> None :
        """Permet de supprimer un événement de la liste."""
        self._events.remove(signal_event)
        del signal_event

    def get_event (self, position_ : int) -> SignalEvent :
        """Permet de récuperer un événement suivant son index dans la liste des événements."""
        return self._events[position_]

    def construct_event (self, signal_event_ : SignalEvent = None) -> SchedulerEvent :
        """Permet de créer un schedulerEvent sur base d'un signal event."""
        if signal_event_ == None :
            return SchedulerEvent(None, None, None, self.current_time, self)
        else :
            return SchedulerEvent(signal_event_.signal, signal_event_.box, signal_event_.new_signal_data, self.current_time, self)

    def construct_exception (self, current_box_ : Box, current_box_bis_ : Box, current_event_ : SignalEvent, exception_ : Exception) -> SchedulerException :
        """Permet de créer une exception."""
        return SchedulerException(current_box_, current_box_bis_, self._events, current_event_, self.diagram, self.current_time, exception_)

    def construct_signal_event (self, signal : Signal, box : Box, data : Data) -> SignalEvent :
        """Permet de créer des evenements de signaux."""
        return SignalEvent(signal, box, data)

    def is_scheduler_exception (self, obj : Any) -> bool :
        """Permet de savoir si l'objet passé en paramètre est une exception."""
        return isinstance(obj, SchedulerException)