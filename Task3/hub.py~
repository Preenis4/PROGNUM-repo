import numpy as np
import matplotlib.pyplot as plt

def chi_2(x, y):
    npx = np.array(x)
    npy = np.array(y)
    b = (np.sum(npx*npy))/(np.sum(npx**2))
    print(b)
    return np.sum((npy - (b*npx))**2)

def bee(x, y):
    npx = np.array(x)
    npy = np.array(y)
    return (np.sum(npx*npy))/(np.sum(npx**2))

data = [ (18.49, 2094.75),
 (35.48, 2320.87),
 (35.48, 1224.9),
 (11.34, 872.13),
 (7.12,  432.2),
 (9.82,  751),
 (23.66, 1410),
 (44,    2700),
 (66.7,  5292),
 (52.4,  2550),
 (55,    5253),
 (25.6,  2419),
 (26.19, 2158)]
distance, velocity = zip(*data)

myhub = bee(distance, velocity)

distance, velocity = zip(*data)
npdis = np.array(distance)
calcd = list(npdis * myhub)
litted = list(npdis * 67.66)
plt.rcParams['text.usetex'] = True
plt.scatter(distance, velocity, marker = "*", color = "red", label= "stars")
plt.plot(distance, litted, label = "literature")
plt.plot(distance, calcd, label = "calculated")

plt.xlabel(r"Distance(Mpc)")
plt.ylabel(r"Velocity($\frac{km}{s}$)")
plt.title("Hubble constant")
plt.legend()
plt.show()