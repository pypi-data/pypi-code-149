#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _init_integrator_box (box, simulation_params) -> None :
    box['last_output'] = 0
    box['last_input'] = 0
    box['last_timing'] = 0


def _function_integrator_box (box, event_) -> List:
        
    input = box.get_input(0).value

    if event_.timing == 0 :
        return []

    if box['last_timing'] == event_.timing :
        return []

    box['last_timing'] = event_.timing

    v = (event_.step_time * (input + box['last_input']) / 2) + box['last_output']

    box['last_output'] = v
    box['last_input'] = input

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events