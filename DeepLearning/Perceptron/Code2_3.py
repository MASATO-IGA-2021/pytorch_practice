
import numpy as np

def AND(x1, x2) :
    x = np.array([x1,x2])
    w1,w2,b = 0.5, 0.5, -0.8
    perceptron = x[0]*w1 + x[1]*w2 + b
    if  perceptron > 0 :return 1
    else:return 0 
# print(AND(0,0))
# print(AND(1,0))
# print(AND(0,1))
# print(AND(1,1))

def NAND(x1, x2) :
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    perceptron = sum(x*w) + b
    if perceptron > 0:return 1
    else:return 0
# print(NAND(0,0))
# print(NAND(1,0))
# print(NAND(0,1))
# print(NAND(1,1))


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.7
    perceptron = sum(x*w) + b
    if perceptron > 0:return 1
    else:return 0  
# print(OR(0,0))  
# print(OR(1,0))  
# print(OR(0,1))  
# print(OR(1,1))  
 
def NOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1, x2)
    return (AND(s1, s2))
print(NOR(0,0))
print(NOR(1,0))
print(NOR(0,1))
print(NOR(1,1))