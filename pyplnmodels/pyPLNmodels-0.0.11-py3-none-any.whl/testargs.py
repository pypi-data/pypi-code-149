import pandas as pd 
import torch 
import numpy as np 

Y = pd.read_csv("../example_data/Y_test")
print(isinstance(Y, np.ndarray))
