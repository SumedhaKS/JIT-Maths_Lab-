import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-10,10,0.001)
y1= np.sin(x)
y2= np.cos(x)
plt.plot(x,y1,x,y2)
plt.title("Sin and Cos Curve")
plt.xlabel("Values of X")
plt.ylabel("values of sin(x) and cos(x) ")
plt.grid()
plt.show()