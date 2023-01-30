from sympy import plot_implicit, symbols,Eq
x, y= symbols('x y')
p3= plot_implicit(
    Eq((y**2)*(2-x),(x**2)*(2+x)), (x,-5,5), (y,-5,5))
title= 'Strophoid: $y^2 (a-x)= x^2 (a+x),a>0$'

