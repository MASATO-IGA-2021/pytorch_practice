import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))
def identify_function(x):
    return x

def init_network():
    network = {}
    network["w1"] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["w2"] = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["w3"] = np.array([[0.1, 0.3],[0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2, W3 =  network["w1"],  network["w2"],  network["w3"]
    B1, B2, B3 =  network["b1"],  network["b2"],  network["b3"]
    
    A1 = np.dot(x, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    y = identify_function(A3)
    return y
network = init_network()
X = np.array([0.87, 1.21])
Y = forward(network, X)
print(Y)