import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
#配列の次元数を取得
print(A.shape)
#配列の形状を取得
print(A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
#配列の次元数を取得
print(B.shape)
#配列の形状を取得
print(B.shape[0])

C = np.array([[1,2],[3,4]])
D  =np.array([[2,3],[4,5]])
print(np.dot(C,D))