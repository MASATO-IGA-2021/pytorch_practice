import numpy as np

x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

print(type(x))
print(x + y)
print(x - y)
print(x * y)
print(x / y)

A = np.array([[1.0,2.0],[3.0,4.0]])
print(A)
print(A.shape)
print(A.dtype)
B = np.array([[3,0],[0,6]])
print(A + B)
print(A * B)
print(A * 10)

X = np.array([[51,55],[14,19],[0,4]])
print(X)
X = X.flatten()
print(X)
Y = X[np.array([0,2,4])]
print(Y)