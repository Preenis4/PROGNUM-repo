import matplotlib.pyplot as plt
import scipy
import numpy as np

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A = float(input('A: '))
x0 = float(input('x0: '))
sig = float(input('sigma: '))
z0 = float(input('z0: '))
upper = float(input('Upper: '))
lower = float(input('Lower: '))


testx = np.linspace(-10, 10, 200)
testb = np.linspace(lower, upper, 200)

testy = gauss(testx, A, x0, sig, z0)
testyb = gauss(testb, A, x0, sig, z0)

intr, _ = scipy.integrate.quad(gauss, lower, upper, args=(A, x0, sig, z0))
print(f'The area is: {intr}')

plt.plot(testx, testy)

plt.fill_between(testb, testyb, z0, label = intr, color='g')
plt.legend()
plt.show()
