import numpy as np

np.random.seed(10)
n_ = 1000
t = np.linspace(0, 50 * np.pi, n_)
# pattern + trend + noise
x1 = (
    sum([20 * np.sin(i * t + np.pi) for i in range(5)])
    + 0.01 * (t ** 2)
    + np.random.normal(0, 6, n_)
)
x2 = (
    sum([15 * np.sin(2 * i * t + np.pi) for i in range(5)])
    + 0.5 * t
    + np.random.normal(0, 6, n_)
)

ts_2dim = np.column_stack([x1, x2])
