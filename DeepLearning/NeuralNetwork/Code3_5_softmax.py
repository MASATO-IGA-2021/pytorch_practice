import numpy as np

# def softmax(x):
#     exp_a = np.exp(x)
#     sum_exp_a = np.sum(exp_a)
#     # print(f"exp_a:{exp_a}")
#     # print(f"sum_exp_a:{sum_exp_a}")
#     return exp_a / sum_exp_a

def SoftMax(x):
    max_a = np.max(x)
    exp_a = np.exp(x-max_a)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

X = np.array([1, 2, 1.5])
print(SoftMax(X))