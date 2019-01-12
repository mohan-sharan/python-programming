import numpy as np

import matplotlib.pyplot as plt

a = np.linspace(0,10,100)

b = np.cos(a)

plt.plot(a,b)

plt.xlabel("Time")
plt.ylabel("A function of time")
plt.title("Example Chart")

plt.show()
