#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from random import seed
from random import random

#-----------------------------------
# Functions
#-----------------------------------

def _init_noise_box (box, simulation_params) -> List : 
    
    if box['apply_seed'] :
        seed(box['seed'])

    box['min'] = box['mean_value'] - (box['amplitude'] / 2)

def _function_noise_box (box, event_) -> List :

    v = box['amplitude'] * random() + box['min']
    
    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events