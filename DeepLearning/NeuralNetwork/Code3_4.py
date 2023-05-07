import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

def identify_function(x):
    return x

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X,W1) + B
# print(X.shape)
# print(W1.shape)
# print(B.shape)
# print(A1.shape)
print(A1)

Z1 = sigmoid(A1)
W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1,W2) + B2
print(Z1) 
print(A2)

Z2 = sigmoid(A2)
W3 = np.array([[0.1, 0.3],[0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2,W3) + B3
print(Z2)
print(A3)

y = identify_function(A3)
print("出力値= ",y)
