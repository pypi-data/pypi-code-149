
import matplotlib.pylab as plt
import numpy as np

C = [
        [1/2,   1/4,    1/8,    1/16,   1/32,   1/64],
        [4,     4/3,    4/6,    4/9,    4/12,   4/15],
        [1,     1/5,    1/10,   1/15,   1/20,   1/25]  
    ]


X = []
Values = []
Values.append([])
Values.append([])
Values.append([])

v = 0
while v < 0.05:
    X.append(v)
    v += 0.001

for i, x_ in enumerate(X):
    v = 0
    
    if x_ < 0.035 :
        Values[1].insert(0, 1)
    else :
        Values[1].insert(0, 0)

    if x_ < 0.003:
        Values[2].insert(0, 0)
    elif x_ < 0.014:
        Values[2].insert(0, 1)
    elif x_ < 0.028:
        Values[2].insert(0, 0)
    else:
        Values[2].insert(0, 1)

    if len(C) > 0:
        if len(C[0]) > 0 :
            v = C[0][0]
    
    for j in range(min(len(C[0])-1, len(Values[0]))):
        v += C[0][j + 1] * Values[0][j]

    input_count = len(Values) - 1
    coeff_count = len(C) - 1
    input_index_count = min(input_count, coeff_count)

    if x_ >= 0.013 and x_ <= 0.014 :
        print("oui")

    for input_index in range(min(coeff_count, input_count)) :

        input_value_index_count = len(C[input_index + 1])
        last_values_index_count = len(Values[input_index + 1])
        values_index_count = min(input_value_index_count, last_values_index_count)

        for value_index in range(values_index_count) :
            coeff = C[input_index + 1][value_index]
            val = Values[input_index + 1][value_index]
            v += coeff * val 
    
    Values[0].insert(0, v)

Y = []
I1 = []
I2 = []
for i, x_ in enumerate(X):
    Y.append(Values[0][len(X) - 1 - i])
    I1.append(Values[1][len(X) - 1 - i])
    I2.append(Values[2][len(X) - 1 - i])

fig = plt.figure('i1 & i2') 
plt.grid(True)
plt.title('i1 & i2')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.plot(X, Values[1], X, Values[2])


fig2 = plt.figure('y')
plt.grid(True)
plt.title('y')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.plot(X, Y)


plt.show()
