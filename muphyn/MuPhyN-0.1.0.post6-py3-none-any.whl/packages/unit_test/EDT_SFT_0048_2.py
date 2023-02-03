import numpy as np
from typing import List

def print_eq_laplace (num_vect : List[float], denum_vect : List[float]) -> None : 
    eq = 'Y * ('
    order_denum = len(denum_vect) - 1
    order_num = len(num_vect) - 1

    for i, current_coeff in enumerate(denum_vect) :
        
        current_order = order_denum - i

        if current_coeff == 0 :
            continue

        if not(i == 0) :
            
            if current_coeff < 0 :
                eq = eq + ' - '
            else :
                eq = eq + ' + '

        else :
            if current_coeff < 0 :
                eq = eq + ' - '

        if current_order > 1 :
            eq = eq + str(np.abs(current_coeff)) + ' s**' + str(current_order)

        elif current_order == 1 :
            eq = eq + str(np.abs(current_coeff)) + ' s'

        elif current_order == 0 : 
            eq = eq + str(np.abs(current_coeff))

    eq = eq + ') / ('

    for i, current_coeff in enumerate(num_vect) :
        
        current_order = order_num - i
        
        if current_coeff == 0 :
            continue
        
        if not(i == 0) :
            
            if current_coeff < 0 :
                eq = eq + ' - '
            else :
                eq = eq + ' + '

        else :
            if current_coeff < 0 :
                eq = eq + ' - '

        if current_order > 1 :
            eq = eq + str(np.abs(current_coeff)) + ' s**' + str(current_order)

        elif current_order == 1 :
            eq = eq + str(np.abs(current_coeff)) + ' s'

        elif current_order == 0 : 
            eq = eq + str(np.abs(current_coeff))

    return eq + ') = U'