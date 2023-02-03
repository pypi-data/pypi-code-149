#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _init_ramp_box (box, simulation_params) -> None :

    if not 'start_time' in box :
        box['start_time'] = 0.0

    if not 'initial_value' in box :
        box['initial_value'] = 0.0

    if not 'slope' in box :
        box['slope'] = 1.0

def _function_ramp_box (box, event_) -> List : 
    if event_.timing < box['start_time']:
        v = box['initial_value']
    else:
        v = box['initial_value'] + ((event_.timing - box['start_time']) * box['slope'])

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events