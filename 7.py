import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-1,1,0.001)
y1= np.sin(x)
y2= np.cos(x)

plt.plot(x,y1/y2)
plt.title("Tan Curve")
plt.xlabel("Values of X")
plt.ylabel("values of sin(x) by cos(x)")
plt.grid()
plt.show()