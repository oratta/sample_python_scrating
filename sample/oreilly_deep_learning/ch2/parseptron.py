import numpy as np

def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    return parseptron(x1,x2,w1,w2,b)

def OR(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.2
    return parseptron(x1,x2,w1,w2,b)

def NAND(x1, x2):
    w1, w2, b = -0.5, -0.5, 0.7
    return parseptron(x1,x2,w1,w2,b)

def parseptron(x1, x2, w1, w2, b):
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

