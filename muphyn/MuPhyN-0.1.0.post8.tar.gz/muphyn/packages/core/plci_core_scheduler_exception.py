#-----------------------------------
# Imports
#-----------------------------------

import traceback
from types import TracebackType
from typing import List

from muphyn.packages.core.utils.log_manager import LogManager
from .plci_core_diagram import Diagram
from .plci_core_box import Box
from .plci_core_signal_event import SignalEvent

#-----------------------------------
# Class
#-----------------------------------

class SchedulerException :
    """Est la classe qui permet de créer un retour lors d'une exception dans un planificateur."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_ : Box, box_bis_ : Box, events_ : List[SignalEvent], event_ : SignalEvent, diagram_ : Diagram, timing_ : float, exception_ : Exception) :
        self._box = box_
        self._box_bis = box_bis_
        self._events = events_
        self._event = event_
        self._diagram = diagram_
        self._exception = exception_
        self._timing = timing_

    
    # -------------
    # Methods
    # -------------

    def print (self) :
        to_print_rows = []
        to_print_rows.append("SCHEDULER EXCEPTION : ")

        to_print_rows.append(f"\tException at : {self._timing: .3f}s")

        if self._box is None :
            to_print_rows.append("\tBox : No current box")
        else :
            to_print_rows.append(f"\tBox : {self._box.library} {self._box.name} | index : {self._box.index}")

        if self._box_bis is None :
            to_print_rows.append("\tBis box : No current bis box")
        else :
            to_print_rows.append(f"\tBix Box : {self._box.library} {self._box.name} | index : {self._box_bis.index}")

        if self._event is None :
            to_print_rows.append("\tCurrent event : No current event")
        else :
            to_print_rows.append(f"\tCurrent event : box index : {self._event.box.index} | signal index : {self._event.signal.index}")

            if not self._event.signal in self._diagram.box_inputs :
                to_print_rows.append("\tThe signal does not have any box to tickle !!!")

        if self._events is None :
            to_print_rows.append("\tEvents list : No events list")
        else :
            to_print_rows.append(f"\tEvents list : {len(self._events)} events in the queue")

        to_print_rows.append(f"\t{''.join(traceback.format_exception(self._exception))}")

        LogManager().error('\n'.join(to_print_rows))