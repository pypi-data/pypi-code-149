#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from math import pow

#-----------------------------------
# Functions
#-----------------------------------

def _function_power_box (box, event_) -> List :
    
    v = pow(box.get_input(0).value, box['power'])
    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events