import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-10,10,0.001)
y2= np.cos(x)
plt.plot(x,y2)
plt.title("Cos Curve")
plt.xlabel("Values of X")
plt.ylabel("values of cos(x)")
plt.grid()
plt.show()