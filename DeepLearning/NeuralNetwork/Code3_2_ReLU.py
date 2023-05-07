import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
    return np.maximum(0,x)

x = np.arange(-3.0, 3.0, 0.1)
y = ReLU(x)
plt.plot(x, y)
plt.show()
#output: "C:\Users\masato\Pictures\Screenshots\ReLU.png"