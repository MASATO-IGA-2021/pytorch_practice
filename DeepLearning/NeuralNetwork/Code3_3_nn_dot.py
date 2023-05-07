#簡易的なニューラルネットワークの形成

import numpy as np
x = np.array([1, 2, 3])
print(x.shape)
w = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(w.shape)
print(np.dot(x,w))