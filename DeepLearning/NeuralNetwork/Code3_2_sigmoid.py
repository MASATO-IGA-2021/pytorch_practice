import numpy as np
import matplotlib.pyplot as plt
class Code3_2_sigmoid:
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    x = np.arange(-10.0, 10.0, 0.1)
    y = sigmoid(x)
    plt.plot(x,y)
    plt.show()
    #output: "C:\Users\masato\Pictures\Screenshots\sigmoid.png"
