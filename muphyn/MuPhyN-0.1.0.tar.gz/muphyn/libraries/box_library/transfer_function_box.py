# -----------------------------------
# Imports
# -----------------------------------

from typing import List
from scipy.integrate import solve_ivp

from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.utils.tools.math_expression_painter import mathTex_to_QPixmap

# -----------------------------------
# Functions
# -----------------------------------
def _update_icon(box_model: BoxModel):
    num = get_coeff_vector(box_model.get_parameter('numerator')["value"])
    num_str = ""
    for index in range(len(num)):
        degree = len(num) - index - 1
        coef = num [index]
        num_str += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            num_str += f" * s^{degree}"
        elif degree == 1:
            num_str += " * s"

    denom = get_coeff_vector(box_model.get_parameter('denominator')["value"])
    denom_str = ""
    for index in range(len(denom)):
        degree = len(denom) - index - 1
        coef = denom [index]
        denom_str += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            denom_str += f" * s^{degree}"
        elif degree == 1:
            denom_str += " * s"

    print("\\frac{" + num_str + "}{" + denom_str + "}")
    pixmap = mathTex_to_QPixmap("\\frac{" + num_str + "}{" + denom_str + "}")
    box_model.setIcon(pixmap)

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
    
    box['num_vect'] = get_coeff_vector(box['numerator'])
    box['num_vect'].reverse()
    box['num_order'] = len(box['num_vect']) - 1

    box['denom_vect'] = get_coeff_vector(box['denominator'])
    box['denom_vect'].reverse()
    box['denom_order'] = len(box['denom_vect']) - 1

    box['last_y'] = [box['initial_value']] + [0] * (box['denom_order'] -1) 
    
    box['last_timing'] = -1

def f(t, y, box): 
    out = 0
    for j, coeff_y  in enumerate(box['denom_vect'][:-1]):
        out -= coeff_y * y[j]
    
    for j, coeff_y in enumerate(box['num_vect']):
        if j == 0:
            out += coeff_y * box.get_input(0).value
        else:
            out += coeff_y * y[j]
    
    out_vector = [y[box['denom_order'] - 1 - x] for x in range(box['denom_order'])]
    out_vector[-1] = out/box['denom_vect'][-1]

    return out_vector

def _function_transfer_function(box, event_) -> List :             

    if box['last_timing'] == event_.timing:    # if we are still on the current step, leave
        return []

    events: List = []

    
    step = event_.step_time

    t0 = event_.timing

    t = [t0, t0 + step]                 # time vector is only current and next step
    sol = solve_ivp(f, t, box['last_y'], args=(box,), method='RK45', rtol=box['rtol'], atol=box['atol'])
    
    out = list(sol.y[:,-1])               # use the last values as the output of the step

    box['last_y'] = out

    for output in box.outputs :
        events.append(box.construct_signal_event(output, out[0])) # only send the y(t) output, discard eventual derivatives for order >= 2

    box['last_timing'] = event_.timing

    return events
