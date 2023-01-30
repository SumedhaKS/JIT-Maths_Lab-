import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-10,10,0.001)
y1= np.sin(x)
plt.plot(x,y1)
plt.title("Sin Curve")
plt.xlabel("Values of X")
plt.ylabel("values of sin(x) ")
plt.grid()
plt.show()