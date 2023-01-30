import matplotlib.pyplot as plt
from sympy import plot_implicit, symbols,Eq
x, y= symbols('x y')
p5= plot_implicit(
    Eq(4*(y**2) , (x**2)*(4-x**2)) , (x , -5 , 5) , (y , -5 , 5)
)