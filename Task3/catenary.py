import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
fig, ax = plt.subplots(figsize=(40,100)) 

x = np.arange(-5,6,0.1)
y = np.cosh(x)
plt.scatter(x, y)
plt.plot(x, y)
ax.set_title("Catenary plot")
ax.set_ylabel("Height(m)")
ax.set_xlabel("Wideness(m)")
red_patch = mpatches.Patch(color='blue', label="Catenary")
ax.legend(handles=[red_patch])
ax.grid()
plt.show()
