#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _init_constant_box (box, simulation_params) -> None :
    
    if not 'Constant Value' in box :
        box['Constant Value'] = 1

def _function_constant_box (box, event_) -> List :
    
    v = box['Constant Value']
    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events