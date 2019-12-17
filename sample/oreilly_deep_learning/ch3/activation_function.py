import numpy as np
import matplotlib.pylab as plt

# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# def step_function(x):
#     y = x > 0
#     return y.astype(np.int)

def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def identify_function(x):
    return x

def __check():
    x = np.arange(-5.0, 5.0, 0.1)
    # y = step_function(x)
    y = sigmoid(x)
    plt.plot(x,y)
    plt.ylim(-0.1, 1.1)
    plt.show()