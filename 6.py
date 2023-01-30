import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-1,1,0.001)
y1= np.tan(x)
plt.plot(x,y1)
plt.title("Tan Curve")
plt.xlabel("Values of X")
plt.ylabel("values of tan(x) ")
plt.grid()
plt.show()