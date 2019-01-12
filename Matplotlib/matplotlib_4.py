#PLOT SHOWING THE TALLEST BUILDINGS IN THE WORLD

import matplotlib.pyplot as plt
plt.style.use('ggplot') #A style of plot presentation
import numpy as np

buildings = ["Shun Hing Square (China)",
"CITIC Plaza (China)",
"23 Marina (UAE)",
"Two International Finance Centre (China)",
"Al Hamra Tower (Kuwait)",
"Princess Tower (UAE)",
"Jin Mao Tower (China)",
"Trump International Hotel & Tower (USA)",
"432 Park Avenue (USA)",
"Guangzhou International Finance Center (China)",
"KK100 (China)",
"Willis Tower (USA)",
"Jiangxi Nanchang Greenland Zifeng Tower (China)",
"Petronas Towers (Malaysia)",
"International Commerce Centre (China)",
"Shanghai World Financial Center (China)",
"TAIPEI 101 (Taiwan)",
"Guangzhou CTF Finance Center (China)",
"One World Trade Center (USA)",
"Lotte World Tower (South Korea)",
"Ping An Finance Center (China)",
"Makkah Royal Clock Tower (Saudi Arabia)",
"Shanghai Tower (China)",
"Burj Khalifa (UAE)"] 

xAxis = np.arange(len(buildings))

height = [384, 390.2, 392.4, 412, 412.6, 413.4, 420.5, 423.2, 425.5, 438.6, 441.8, 442.1,
	450, 451.9, 484, 492, 508, 530, 541.3, 554.5, 599, 601, 632, 828]

plt.bar(xAxis, height, align='center', color='orange')

plt.xticks(xAxis, buildings)
plt.xticks(rotation=90)

plt.xlabel("Buildings")
plt.ylabel("Height (in meters)")
plt.title("The Tallest Buildings in the World!")

plt.show()
