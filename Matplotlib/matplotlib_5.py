#Visualization - Pie Chart
#DART (Dallas Area Rapid Transit ) 
#Summary of Operating Expenses (2013-2017)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

labels = ["Salary, Wages, Benefits", "Materials and Supplies", "Purchased Transportation", "Other Operating Expenses"]
slice_colors = ["orange", "yellowgreen", "lightskyblue", "red"]
values_2013 = [298624115, 53017289, 37347278, 70941046]
values_2014 = [349304690, 44250972, 41572484, 30418733]
values_2015 = [352294008, 38574651, 42705615, 30615583]
values_2016 = [326096263, 43307151, 47175978, 73147290]
values_2017 = [342666956, 42810386, 47871991, 70034979]

plt.subplot(2,3,1)
plt.title("Summary (OE) - 2013")
plt.pie(values_2013, colors=slice_colors, shadow=True, autopct="%1.1f%%", startangle=90)
plt.axis("equal")

plt.subplot(2,3,2)
plt.title("Summary (OE) - 2014")
plt.pie(values_2014, colors=slice_colors, shadow=True, autopct="%1.1f%%", startangle=90)
plt.axis("equal")

plt.subplot(2,3,3)
plt.title("Summary (OE) - 2015")
plt.pie(values_2015, colors=slice_colors, shadow=True, autopct="%1.1f%%", startangle=90)
plt.axis("equal")

plt.subplot(2,3,4)
plt.title("Summary (OE) - 2016")
plt.pie(values_2016, colors=slice_colors, shadow=True, autopct="%1.1f%%", startangle=90)
plt.axis("equal")

plt.subplot(2,3,5)
plt.title("Summary (OE) - 2017")
plt.pie(values_2017, colors=slice_colors, shadow=True, autopct="%1.1f%%", startangle=90)
plt.legend(labels, loc="best")
plt.axis("equal")

plt.subplot(2,3,6)
year = ["Y2013", "Y2014", "Y2015", "Y2016", "Y2017"]
xaxis = np.arange(len(year))
yaxis = [459, 465, 464, 489, 503]
#yaxis = [459929728,  465546879, 464189857, 489726682, 503384312]
plt.bar(xaxis, yaxis, align="center", color="green")
plt.xticks(xaxis, year)
plt.xticks(rotation=90)
plt.title("Year vs Total (OE)")
plt.xlabel("Year -> 2013 to 2017")
plt.ylabel("Total OE (Million $)")
 
plt.show()

#References:
#https://www.transit.dot.gov/
#https://www.dart.org/about/dartfacts.asp