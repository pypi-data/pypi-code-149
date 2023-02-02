#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from numpy import sin

#-----------------------------------
# Functions
#-----------------------------------

def _init_sine_box (box, simulation_params) -> None :

    if not 'amplitude' in box :
        box['amplitude'] = 1.0

    if not 'pulsation' in box :
        box['pulsation'] = 1.0
    
    if not 'phase' in box :
        box['phase'] = 0.0

def _function_sine_box (box, event_) -> List : 
    
    v = box['amplitude'] * sin((event_.timing * box['pulsation']) + box['phase'] )
    
    events : List = []

    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events