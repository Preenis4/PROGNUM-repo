import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
fig, ax = plt.subplots()

x = np.arange(-5,6)
y = np.cosh(x)
plt.scatter(x, y)
plt.plot(x, y)
ax.set_title("Catenary plot")
ax.set_ylabel("Height")
ax.set_xlabel("Wideness")
red_patch = mpatches.Patch(color='blue', label="Catenary")
ax.legend(handles=[red_patch])
ax.grid()
plt.show()
