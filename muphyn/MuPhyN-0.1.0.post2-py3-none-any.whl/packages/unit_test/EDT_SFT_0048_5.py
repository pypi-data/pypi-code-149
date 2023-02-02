from os import system
import time

import numpy as np
import matplotlib.pyplot as plt

from typing import List

from box_library.transfert_function_box import get_coeff_vector, euler
from muphyn.packages.unit_test.EDT_SFT_0048_2 import print_eq_laplace

# =========== Differential equation ===========

_ = system('cls')

wc = 20

num = '1'
denom = '1 1 1'

num_vect = get_coeff_vector(num)
denom_vect = get_coeff_vector(denom)

denom_order = len(denom_vect) - 1
num_order = len(num_vect) - 1
order = denom_order

# =========== Simulation ===========

fs = 100
dt = 1/fs
sim_time = 15
samples_number = int(fs * sim_time) + 2

print('=============================================================')
print('||                                                         ||')
print('||                      Simulation                         ||')
print('||                                                         ||')
print('|| - num order :', num_order, '                                        ||')
print('|| - denom order :', denom_order, '                                      ||')
print('|| - eq order :', order, '                                         ||')
print('||                                                         ||')
print('|| - simulation time :', sim_time, '                                 ||')
print('|| - sample frequency :', fs, '                              ||')
print('|| - dt :', dt, '                                           ||')
print('|| - samples number :', samples_number, '                               ||')
print('||                                                         ||')
print('|| - input : STEP                                          ||')
print('|| - eq : ', print_eq_laplace(num_vect, denom_vect))
print('||                                                         ||')
print('=============================================================')
print('')
print('')

num_vect.reverse()
denom_vect.reverse()

# time
t = [n * dt for n in range(samples_number)]

# input - STEP
u = [1 if t_ > 1 else 0 for t_ in t]

# output
last_u_derivatives : List[float] = [0 for num in num_vect]
last_y_derivatives : List[float] = [0 for denom in denom_vect]
last_y = 0
y = []


for i, t_ in enumerate(t) :
#for i in range(12) :

    current_y = 0
    current_u_derivatives = []
    current_y_derivatives = []

    # u's
    for j, coeff_u in enumerate(num_vect) :
        
        if j == 0 :
            current_y += coeff_u * u[i]
            current_u_derivatives.append(u[i])

        else:
            derivative = (current_u_derivatives[j - 1] - last_u_derivatives[j - 1]) / dt

            current_y += coeff_u * derivative
            current_u_derivatives.append(derivative)

    # y's 
    if order > 0 :
        
        for j in range(order) : 

            coeff_y = denom_vect[j]
            
            if j == 0 :
                current_y -= coeff_y * last_y
                current_y_derivatives.append(last_y)

            else :
                derivative = (current_y_derivatives[j - 1] - last_y_derivatives[j - 1]) / dt

                current_y -= coeff_y * derivative
                current_y_derivatives.append(derivative)
        
        current_y /= denom_vect[order]

        for j in range(order).__reversed__() :
            print('time :', t_, ' - order :', j, ' - derivative :', current_y_derivatives[j])
            current_y *= dt
            current_y += current_y_derivatives[j]
            

    else :
        current_y = current_y / denom_vect[order]

    """
    if i >= 2 :
        #current_y -= denom_vect[0] * y[i - 1]
        #current_y -= denom_vect[1] * (current_y_derivatives[0] - last_y_derivatives[0]) / dt
        #current_y /= denom_vect[2]
        current_y *= dt
        current_y += (y[i - 1] - y[i - 2]) / dt
        current_y *= dt 
        current_y += y[i - 1]
        
    elif i == 1 :
        #current_y -= denom_vect[0] * y[i - 1]
        #current_y -= denom_vect[1] * (current_y_derivatives[0]) / dt
        #current_y /= denom_vect[2]
        current_y *= dt
        current_y += ((y[i - 1]) / dt)
        current_y *= dt 
        current_y += y[i - 1]

    else :
        #current_y /= denom_vect[2]
        current_y *= dt
        current_y *= dt
    """

    last_u_derivatives = current_u_derivatives
    last_y_derivatives = current_y_derivatives
    last_y = current_y
    
    y.append(current_y)

print('at', (len(y) - 1) / fs, 's :', y[len(y) - 1])

# =========== Personnal notes ===========

print('')
print(' =====> Résultats <=====')
print('')
print('date : 22/02/2022')
print('')
print('Les modifications apportées et trouvées permettent ')

# =========== Plot results ===========

t_renderable = t[0 : len(y)]
u_renderable = u[0 : len(y)]

plt.figure()
num_vect.reverse()
denom_vect.reverse()
plt.title(print_eq_laplace(num_vect, denom_vect))
#plt.plot(t_renderable, u_renderable, label="u(t)")
plt.plot(t_renderable, y, label="y(t)")
plt.legend()
plt.grid()
plt.xlabel('Time')
plt.show()