#SMART WATCH ANALYSIS
#1. Fitness Focused Watch (Ex: Garmin - fenix 5 Plus)
#2. Galaxy Watch
#3. Apple Watch
#Parameters - Water Rating, Battery Life, Build Quality, Price

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
watchData_1 = [["Garmin - fenix 5 Plus", 10, 100], ["Galaxy Watch", 5, 50], ["Apple Watch Series 4", 5, 50]]
wd1 = pd.DataFrame(watchData_1, index=[1,2,3], columns = ["Watch", "Water Rating (ATM)", "Water Rating (meters)"])
#Conversion: 1 ATM = 10.33 m
print(wd1)
'''
                   Watch  Water Rating (ATM)  Water Rating (meters)
1  Garmin - fenix 5 Plus                  10                    100
2           Galaxy Watch                   5                     50
3   Apple Watch Series 4                   5                     50
'''
watchData_2 = [["Garmin - fenix 5 Plus", 12], ["Galaxy Watch", 4], ["Apple Watch Series 4", 1]]
wd2 = pd.DataFrame(watchData_2, index=[1,2,3], columns = ["Watch", "Battery Life (Days)"])
print(wd2)
'''
                   Watch  Battery Life (Days)
1  Garmin - fenix 5 Plus                   12
2           Galaxy Watch                    4
3   Apple Watch Series 4                    1
'''
watchData_3 = [["Garmin - fenix 5 Plus", 9.5], ["Galaxy Watch", 6], ["Apple Watch Series 4", 7]]
wd3 = pd.DataFrame(watchData_3, index=[1,2,3], columns = ["Watch", "Build Quality (1-10)"])
print(wd3)
'''
                   Watch  Build Quality (1-10)
1  Garmin - fenix 5 Plus                   9.5
2           Galaxy Watch                   6.0
3   Apple Watch Series 4                   7.0
'''
watchData_4 = [["Garmin - fenix 5 Plus", "Sapphire, Titanium with Solar Flare Orange Band", 849.99],
              ["Galaxy Watch", "Silver, 4G LTE", 399.99],
              ["Apple Watch Series 4", "Space Gray aluminum case, GPS + Cellular", 529]]
wd4 = pd.DataFrame(watchData_4, index=[1,2,3], columns = ["Watch", "Type", "Cost ($)"])
print(wd4)
'''
                   Watch                                             Type  \
1  Garmin - fenix 5 Plus  Sapphire, Titanium with Solar Flare Orange Band
2           Galaxy Watch                                   Silver, 4G LTE
3   Apple Watch Series 4         Space Gray aluminum case, GPS + Cellular

   Cost ($)
1    849.99
2    399.99
3    529.00
'''
X = range(len(wd1))
X_WATCH = wd1["Watch"]
Y_WATER_RATING = wd1["Water Rating (meters)"]
Y_BATTERY_LIFE = wd2["Battery Life (Days)"]
Y_BUILD_QUALITY = wd3["Build Quality (1-10)"]
Y_COST = wd4["Cost ($)"]

plt.subplot(2,2,1)
plt.xticks(X, X_WATCH, rotation=90)
plt.bar(X, Y_WATER_RATING, align="center", color="blue")
plt.ylabel("Water Rating (meters)")
plt.title("WATER RATING")
plt.ylim(0, 120)

plt.subplot(2,2,2)
plt.xticks(X, X_WATCH, rotation=90)
plt.bar(X, Y_BATTERY_LIFE, align="center", color="green")
plt.ylabel("Battery Life (in days) - Normal Use")
plt.title("BATTERY")
plt.ylim(0, 14)

plt.subplot(2,2,3)
plt.xticks(X, X_WATCH, rotation=90)
plt.bar(X, Y_BUILD_QUALITY, align="center", color="gray")
plt.ylabel("Build Quality")
plt.title("ROBUSTNESS")
plt.ylim(0, 10)

plt.subplot(2,2,4)
plt.xticks(X, X_WATCH, rotation=90)
plt.bar(X, Y_COST, align="center", color="orange")
plt.ylabel("Price ($)")
plt.title("COST")
plt.ylim(0, 1000)

plt.show()

'''
References
Garmin - fenix 5 Plus: https://buy.garmin.com/en-US/US/p/603267/pn/010-01988-04#specs
Galaxy Watch: https://www.samsung.com/global/galaxy/galaxy-watch/
Apple Watch Series 4: https://www.apple.com/apple-watch-series-4/?afid=p238%7Cs0FYFsN2K-dc_mtid_20925qtb42335_pcrid_295216235241&cid=wwa-us-kwgo-watch-slid--
'''
