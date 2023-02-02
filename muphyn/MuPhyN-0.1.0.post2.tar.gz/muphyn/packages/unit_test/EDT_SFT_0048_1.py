from os import system
import matplotlib.pyplot as plt

from typing import List

from box_library.transfert_function_box import get_coeff_vector, euler, trapeze

_ = system('cls')

# =========== Differential methods ===========


def differentiate(order: int, last_index: int, vector: List[float], last_derivatives: List[float], dt: float) -> List[float]:

    returning_tuple = []

    if last_index > 0:
        d_1 = vector[last_index]
        d_2 = vector[last_index - 1]
        returning_tuple.append(euler(d_1, d_2, dt))

        for current_order in range(max(min(order, last_index - 1), 0)):
            d_1 = returning_tuple[current_order]
            d_0 = last_derivatives[last_index - 1][current_order]
            current_derivative = euler(d_1, d_0, dt)

            returning_tuple.append(current_derivative)

            if current_derivative == 0:
                break

    while len(returning_tuple) < order:
        returning_tuple.append(0)

    return returning_tuple

# =========== Differential equation ===========

num = '1 1 0'

num_vect = get_coeff_vector(num)
num_vect.reverse()

num_order = len(num_vect) - 1

# =========== Simulation ===========

fs = 1000
dt = 1/fs
sim_time = 20
samples_number = int(fs * sim_time) + 1

print('=============================================================')
print('||                                                         ||')
print('||                      Simulation                         ||')
print('||                                                         ||')
print('|| X = Y * (P² + P)                                        ||')
print('||                                                         ||')
print('|| - num order :', num_order, '                                        ||')
print('||                                                         ||')
print('|| - simulation time :', sim_time, '                                 ||')
print('|| - sample frequency :', fs, '                              ||')
print('|| - dt :', dt, '                                           ||')
print('|| - samples number :', samples_number, '                               ||')
print('||                                                         ||')
print('=============================================================')
print('')
print('')

# time
t = [n * dt for n in range(samples_number)]

# input
u = [(12.5*t_)**2 for t_ in t]

# output
u_derivatives : List[List[float]] = []
y = []


for i, t_ in enumerate(t) :
#for i in range(10) :

    current_y = 0

    current_u_derivative = differentiate(num_order, i, u, u_derivatives, dt)

    for j, current_coeff in enumerate(num_vect):

        if j == 0:
            current_y += (current_coeff * u[i])

        else:
            current_y += (current_coeff * current_u_derivative[j - 1])

    u_derivatives.append(current_u_derivative)

    y.append(current_y)


print('at', (len(y) - 1) / fs, 's :', y[len(y) - 1])

# =========== Personnal notes ===========

print('')
print(' =====> Résultats <=====')
print('')
print('date : 16/02/2022')
print('')
print('On se rend bien compte que ma méthode fonctionne pour dériver des u.')
print('Cependant, ma méthode d\'approche pour les y semble très mauvaise !')
print('')
print('')
print('date : 17/02/2022')
print('')
print('Essai d\'intégration des U au lieu de dériver les Y ... TRES MAUVAISES REPONSES !!!')
print('')
print('')
print('date : 18/02/2022')
print('')
print('Reprise depuis le début du travail, voir EDT_SFT_0048_3 pour voir la suite.')

# =========== Plot results ===========

t_renderable = t[0 : len(y)]
u_renderable = u[0 : len(y)]

plt.figure()
plt.plot(t_renderable, u_renderable, label="u(t)")
plt.plot(t_renderable, y, label="y(t)")
plt.legend()
plt.grid()
plt.xlabel('Time')
plt.show()
