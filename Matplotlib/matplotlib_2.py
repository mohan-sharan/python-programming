import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

myImage = imread("goku.jpg")

x = np.arange(0, 3*np.pi, 0.1)
y_cos = np.cos(x)
y_sin = np.sin(x)

#Image
plt.subplot(1,3,1)
plt.imshow(myImage)
plt.title("Goku SSJ3")
#Cosine
plt.subplot(1,3,2)
plt.plot(x, y_cos)
plt.title("Cosine")
#Sine
plt.subplot(1,3,3)
plt.plot(x, y_sin)
plt.title("Sine")

plt.show()
