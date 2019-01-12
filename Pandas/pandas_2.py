#INTRODUCTION: PANDAS

import pandas as pd

#Creating a DataFrame - Type 1
carData = [["Agera RS", 271],["Veyron", 254],["Aventador", 217],["R8", 217]]
cdf_1 = pd.DataFrame(carData, columns = ["Car", "Top Speed (mph)"])
print(cdf_1)

print('\nThe number of elements in the DataFrame:')
print(cdf_1.size)

'''
OUTPUT:
         Car  Top Speed (mph)
0   Agera RS              271
1     Veyron              254
2  Aventador              217
3         R8              217

The number of elements in the DataFrame:
8
'''

#Creating a DataFrame - Type 2
carData = {"Car":["Agera RS", "Veyron", "Aventador", "R8"], "Top Speed (mph)":[271,254,217,217]}
cdf_2 = pd.DataFrame(carData)
print(cdf_2.T) #prints the transpose of the DataFrame

print('\nThe number of elements in the DataFrame:')
print(cdf_2.size)

'''
OUTPUT:
                        0       1          2    3
Car              Agera RS  Veyron  Aventador   R8
Top Speed (mph)       271     254        217  217

The number of elements in the DataFrame:
8
'''
