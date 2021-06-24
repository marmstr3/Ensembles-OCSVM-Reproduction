import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 3, 400)
ax.plot(x, x)
print("I RAN!")
