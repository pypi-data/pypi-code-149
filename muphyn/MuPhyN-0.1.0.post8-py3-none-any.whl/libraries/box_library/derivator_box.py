#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _init_derivator_box (box, simulation_params) -> None :
    box['last_output'] = 0
    box['last_input'] = 0
    box['points_evaluated'] = 0

def _function_derivator_box (box, event_) -> List :

    v = 0
    input = box.get_input(0).value

    if (not event_.step_time == 0) and (not event_.timing == 0) : 
        v = (input - box['last_input']) / event_.step_time
        
    else : 
        return []

    box['last_output'] = v
    box['last_input'] = input
    box['points_evaluated'] = box['points_evaluated'] + 1

    if box['points_evaluated'] < 2 :
        return []

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events