from numpy import sin, cos, exp, pi
import numpy as np
import scipy

myfn = input('Enter Function: ')
x = 1
try:
    temp = eval(myfn)
except NameError:
    print('limit function to basic math with x as the variable')
except:
    print('incorrect expression')
del x
low = float(input('low: '))
hi = float(input('high: '))
def fn(x):
    return eval(myfn)
try:
    intr, _ = scipy.integrate.quad(fn, low, hi)
    print(intr)
except:
    print('function not eligible for integration')

rang = np.random.uniform(low, hi, 2000)
mony = (hi - low)*np.mean(fn(rang))
print('monty:')
print(mony)
