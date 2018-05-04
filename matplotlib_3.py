#BAR CHART SHOWING TOP SPEEDS OF CERTAIN SUPER CARS

import numpy as np
import matplotlib.pyplot as plt

cars = ("Veyron", "Agera RS", "Aventador", "Ford GT", "R8","La Ferrari")

carsAxis = np.arange(len(cars))

topSpeed = [254, 271, 217, 216, 199, 217]

plt.bar(carsAxis, topSpeed, align='center', alpha=0.5)

plt.xticks(carsAxis, cars)

plt.xlabel("Cars")
plt.ylabel("Top Speed (mph)")

plt.title("The Top Speed Chart")

plt.show()

