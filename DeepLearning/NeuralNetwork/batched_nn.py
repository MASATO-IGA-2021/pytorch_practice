import numpy as np
from dataset.mnist import  load_mnist
import pickle
import os 

def get_data():
    (x_train, t_train),(x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_train, t_train,x_test, t_test

def init_network():
    with open('./sample_weight.pkl','rb') as f:
        network = pickle.load(f)
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)   # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

def predict(network,x):
    W1,W2,W3 = network['W1'], network['W2'], network['W3']
    b1,b2,b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

def Accuracy(network,x,t,batch_size):
    accurancy_cnt = 0  
    for i in range(0,len(x),batch_size):
        x_batch = x[i:i + batch_size]
        y_batch = predict(network,x_batch)
        p = np.argmax(y_batch,axis =1)
        accurancy_cnt += np.sum(p ==t[i: i + batch_size])
    return accurancy_cnt / len(x) 

network = init_network()
x_train, t_train,x_test, t_test = get_data()
print("Accuracy: ",Accuracy(network,x_test,t_test,100))