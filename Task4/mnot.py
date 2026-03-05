#4.6
from sympy import symbols, integrate, sympify


integrand = input('enter function: ')
variable = input('enter variable: ')
lower = input('input lower: ')
upper = input('input upper: ')

x = symbols(variable)
expr = sympify(integrand)
integral = integrate(expr, (x, lower, upper))

print(integral)
