# import numpy as np

# #活性化関数のステップ関数
# def step_function(x):
#     if x > 0:return 1
#     else:return 0

# #活性化関数のステップ関数(numpy 配列対応)
# def step_function(x):
#     y = x > 0
#     print(y)
#     return y.astype(np.int)

# print(step_function(np.array([0,-1,23])))

#ステップ関数のグラフ
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0 ,dtype = np.int)
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x,y)
plt.show()
#出力結果："C:\Users\masato\Pictures\Screenshots\ステップ関数_.png"

