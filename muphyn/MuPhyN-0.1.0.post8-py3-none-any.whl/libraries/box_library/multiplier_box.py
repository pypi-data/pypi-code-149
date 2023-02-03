#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _function_multiplier_box (box, event_) -> List:
    v = 1

    for input in box.inputs:
        v *= input.value

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events