# -----------------------------------
# Imports
# -----------------------------------

from typing import List
from scipy.integrate import solve_ivp
from scipy.signal import lsim, StateSpace
import ast
import numpy as np

# -----------------------------------
# Functions
# -----------------------------------

def get_coeff_vector(coeff_vector_string: str) -> List[float]:

    if coeff_vector_string is None:
        return [0]

    vector = []
    for sub in coeff_vector_string.split(' '):

        sub = sub.strip()
        if len(sub) == 0:
            continue

        try:
            vector.append(float(sub))
        except ValueError:
            ...

    return vector


def _init_transfer_function(box, simulation_params) -> None:
    
    box['A_list'] = box['A']
    box['B_list'] = box['B']
    box['C_list'] = box['C']
    box['D_list'] = box['D']

    box['system'] = StateSpace(box['A'], box['B'], box['C'], box['D']).to_tf()

    box['input_size'] = 1 #np.array(box['D_list']).shape[1]

    box['last_X'] = ast.literal_eval(box['initial_state'])
    
    box['last_timing'] = -1
    box['last_input'] = 0

def _function_transfer_function(box, event_) -> List :             

    if box['last_timing'] == event_.timing:    # if we are still on the current step, leave
        return []

    events: List = []

    step = event_.step_time

    t0 = event_.timing

    t = [t0, t0 + step]                 # time vector is only current and next step

    sol = lsim(box['system'], [box['last_input'], box.get_input(0).value], t, box['last_X'])
    box['last_input'] = box.get_input(0).value
    
    print(sol)
    out = sol[1][1]               # use the last values as the output of the step
    print(out)
    box['last_X'] = sol[2][-1]

    for output in box.outputs :
        events.append(box.construct_signal_event(output, out)) # only send the y(t) output, discard eventual derivatives for order >= 2

    box['last_timing'] = event_.timing

    return events
