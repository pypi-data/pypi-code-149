# -----------------------------------
# Imports
# -----------------------------------

from typing import List


# -----------------------------------
# Functions
# -----------------------------------

def euler(t_1, t_0, dt):
    """Permet de retourner la differentiel entre deux points."""
    return (t_1 - t_0) / dt

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


def _init_transfert_function(box, simulation_params) -> None:
    
    box['num_vect'] = get_coeff_vector(box['numerator'])
    box['num_vect'].reverse()
    box['num_order'] = len(box['num_vect']) - 1
    box['last_u_derivatives'] = [0 for _ in box['num_vect']]

    box['denom_vect'] = get_coeff_vector(box['denominator'])
    box['denom_vect'].reverse()
    box['denom_order'] = len(box['denom_vect']) - 1
    box['last_y_derivatives'] = [0 for _ in box['denom_vect']]

    box['order'] = box['denom_order']
    box['order_coeff'] = box['denom_vect'][box['order']]

    box['last_y'] = box['initial_value']
    box['last_timing'] = -1

def _function_transfert_function(box, event_) -> List : 

    v = 0
    current_u_derivatives = []
    current_y_derivatives = []
    input_value = box.get_input(0).value

    if box['last_timing'] == event_.timing :
        return []
    box['last_timing'] = event_.timing

    for j, coeff_u in enumerate(box['num_vect']) : 

        if j == 0 : 
            v += coeff_u * input_value
            current_u_derivatives.append(input_value)
        
        else :
            derivative = (current_u_derivatives[j - 1] - box['last_u_derivatives'][j - 1]) / event_.step_time
            v += coeff_u * derivative
            current_u_derivatives.append(derivative)

    if box['order'] > 0 :

        for j in range(box['order']) :

            coeff_y = box['denom_vect'][j]

            if j == 0 :
                v -= coeff_y * box['last_y']
                current_y_derivatives.append(box['last_y'])

            else :
                derivative = (current_y_derivatives[j - 1] - box['last_y_derivatives'][j - 1]) / event_.step_time
                v -= coeff_y * derivative
                current_y_derivatives.append(derivative)

        v /= box['order_coeff']

        for j in range(box['order']).__reversed__() :
            # LogManager().debug(f'time : {event_.timing} - order : {j} - derivative : {current_y_derivatives[j]}')
            v *= event_.step_time
            v += current_y_derivatives[j]

    else :
        v /= box['order_coeff']

    box['last_u_derivatives'] = current_u_derivatives
    box['last_y_derivatives'] = current_y_derivatives
    box['last_y'] = v

    """
    while (len(box['last_y_s']) > box['denom_order']) :
        del box['last_y_s'][0]
    """


    events: List = []

    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events
