from typing import List
import numpy as np
import matplotlib.pyplot as plt



def derivate (n_minus_1 : float, n_0 : float, dT : float) -> float :
    return (n_0 - n_minus_1) / dT

def double_precision_derivate (n_minus_2 : float, n_minus_1 : float, n_0 : float, dT : float) -> float :
    ...

def derivate_second (n_minus_2 : float, n_minus_1 : float, n_0 : float, dT : float) -> float :
    return (n_0 - 2*n_minus_1 + n_minus_2) / (dT*dT)

def derivation_first (data : List[float], step : float, start_value : float = 0) -> List[float] :
    
    data_n_minus_1 = start_value
    vector = []

    for data_n_0 in data : 

        if len(vector) < 1 :
            vector.append(0)
            data_n_minus_1 = data_n_0
            continue
        
        y = derivate(data_n_minus_1, data_n_0, step)
        vector.append(y)

        data_n_minus_1 = data_n_0

    return vector

def derivation_second (data : List[float], step : float, start_values : List[float]) -> List[float] :
    
    data_n_minus_1 = start_values[0]
    data_n_minus_2 = start_values[1]

    vector = []

    for data_n_0 in data : 
    
        if len(vector) < 2 :
            vector.append(0)
            data_n_minus_2 = data_n_minus_1    
            data_n_minus_1 = data_n_0
            continue

        y = derivate_second(data_n_minus_2, data_n_minus_1, data_n_0, step)
        vector.append(y)

        data_n_minus_2 = data_n_minus_1    
        data_n_minus_1 = data_n_0

    return vector

order = 1
fs = 100.0       
cutoff = 30 

print('low pass filter')
print('order :', order)
print('fs :', fs)
print('cutoff :', cutoff)

# Creating the data for filteration
T = 1.0         # value taken in seconds
n = int(T * fs) # indicates total samples
t_a = np.linspace(0, T, n, endpoint=False)

data = []
for t in t_a :
    data.append(t * t * 5)

y_1 = derivation_first(data, 1/fs, (-1/fs)*(-1/fs)*5)
y_2 = derivation_second(data, 1/fs, [(-2/fs)*(-2/fs)*5, (-1/fs)*(-1/fs)*5])
y_3 = []
for i, y_1_ in enumerate(y_1) : 
    y_3.append(data[i] - y_1_ - y_2[i])

plt.figure(0)
plt.plot(t_a[2:], data[2:], 'r-', label='data')
plt.plot(t_a[2:], y_1[2:], 'g-', label='y1')
plt.plot(t_a[2:], y_2[2:], 'b-', label='y2')
plt.plot(t_a[2:], y_3[2:], 'c-', label='y3')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.show()