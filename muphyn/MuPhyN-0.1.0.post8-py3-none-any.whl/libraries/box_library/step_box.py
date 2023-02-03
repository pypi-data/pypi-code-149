#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _init_step_box (box, simulation_params) -> None :

    if not 'step_time' in box :
        box['step_time'] = 1.0

    if not 'start_value' in box :
        box['start_value'] = 0.0

    if not 'stop_value' in box :
        box['stop_value'] = 1.0

def _function_step_box (box, event_) -> List : 
    if event_.timing < box['step_time']:
        v = box['start_value']
    else:
        v = box['stop_value']

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events