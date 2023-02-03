#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

#-----------------------------------
# Functions
#-----------------------------------
def _update_box_value(box_model: BoxModel):
    box_model.setValue(box_model.get_parameter("gain")["value"])

def _function_amplifier_box (box, event_) -> List :
    
    v = box['gain'] * box.get_input(0).value
    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events