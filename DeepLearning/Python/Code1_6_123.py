import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,6,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()
#  "C:\Users\masato\Pictures\Screenshots\Figure_1.png"

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(np.cos(10*x))

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--",label="cos")
plt.plot(x, y3, linestyle = "-",label = "sin(cos(x))")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

