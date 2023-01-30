from sympy import plot_implicit, symbols,Eq
import matplotlib as plt

x, y= symbols('x y')
p4= plot_implicit(
    Eq((y**2)*(3-x),x**3),(x,-2,5), (y,-5,5))
plt.title=('Cissiod')
plt.show()