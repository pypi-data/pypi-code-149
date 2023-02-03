from os import system

import matplotlib.pyplot as plt

# =========== Simulation ===========

fs = 1000
dt = 1/fs
sim_time = 20
samples_number = int(fs * sim_time) + 1

_ = system('cls')
print('=============================================================')
print('||                                                         ||')
print('||                      Simulation                         ||')
print('||                                                         ||')
print('|| X = Y * 1 / (P² + P + 1)                                ||')
print('||                                                         ||')
print('|| - simulation time :', sim_time, '                                 ||')
print('|| - sample frequency :', fs, '                              ||')
print('|| - dt :', dt, '                                           ||')
print('|| - samples number :', samples_number, '                               ||')
print('||                                                         ||')
print('=============================================================')
print('')

# time
t = [n * dt for n in range(samples_number)]

# input
u = [1 for t_ in t]

# output
y = []

A = 2
B = 0
G = 0
K = 1

def test (u, a, b) :
    """
    # Sans coefficeitns (sous entendus, tous à 1)
    current_y = u
    current_y -= a
    current_y -= (a - b) / dt
    current_y *= dt
    current_y += (a - b) / dt
    current_y *= dt 
    current_y += a
    
    # Suite d'instructions.
    return current_y

    # Déjà distribué à la main.
    return ((u - a) * (dt ** 2)) - ((a - b) * dt) + 2 * a - b
    """
    # Avec coefficients.
    return ((K * (dt ** 2)) * u / A) - (G * (dt ** 2) * a / A) - ( B * (a - b) * dt / A) + (a - b) + a



for i, t_ in enumerate(t) :
#for i in range(10) :

    c_u = u[i - 1]
    c_a = 0
    c_b = 0

    if i >= 1 :
        c_a = y[i - 1]
    
    if i >= 2 :
        c_b = y[i - 2]

    temp_y = test(c_u, c_a, c_b)

    if (i == 0) :
        print(temp_y)

    y.append(temp_y)

print('at', (len(y) - 1) / fs, 's :', y[len(y) - 1])

# =========== Personnal notes ===========

print('')
print(' =====> Résultats <=====')
print('')
print('date : 18/02/2022')
print('')
print('Décomposition à la main pas encore complète.')
print('')
print('')
print('date : 21/02/2022')
print('')
print('Fin de la décomposition à la main.')
print('La courbe perçue est exactement la même que celle de xcos !!!!')
print('')
print('Ajout de coefficient devant les termes.')
print('Cela semble fonctionne de la même manière.')
print('')
print('Démarrage sur ces base d\'un nouveau test : EDT_SFT_0048_5')

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