import sys,os
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle 
import glob
# path = glob.glob('sample_weight.pkl')
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
def get_data():
    (x_train, t_train),(x_test, t_test) = load_mnist(flatten = True,normalize = True)
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

def predict(network, x):
    W1,W2,W3 = network['W1'], network['W2'], network['W3']
    b1,b2,b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y 
    
sys.path.append(os.pardir)
network = init_network()
x_train, t_train,x_test, t_test = get_data()

accuracy_cnt = 0
for i in range(len(x_test)):
    y = predict(network, x_test[i])
    p = np.argmax(y)
    if p == t_test[i] :accuracy_cnt +=1
print('Accuracy : ',float(accuracy_cnt/ len(x_test)))



# img = img.reshape(28,28)
#1次元から2次元へ(reshape関数)
#1次元配列[1,2,3,4,5,6,7,8]→2次元配列[[1,2,3,4],[5,6,7,8]]
# img_show(img)
