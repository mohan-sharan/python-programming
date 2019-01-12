#INTRODUCTION: PANDAS
#PANDAS is a python data-centric package that makes analyzing and importing data much easier.

import pandas as pd

file = pd.read_excel("microprocessor.xlsx")

#To read an excel file.

file.head()

#prints the first 5 rows of a data frame. (default: 5)

'''
Out[1]: 
             Processor  Transistor count  Date of introduction  \
0             TMS 1000              8000                  1974   
1           Intel 4004              2300                  1971   
2           Intel 8008              3500                  1972   
3  MOS Technology 6502              3510                  1975   
4        Motorola 6800              4100                  1974   

            Designer    Process    Area  
0  Texas Instruments   8,000 nm  11 mm²  
1              Intel  10,000 nm  12 mm²  
2              Intel  10,000 nm  14 mm²  
3     MOS Technology   8,000 nm  21 mm²  
4           Motorola   6,000 nm  16 mm²  
'''

file.tail()

#prints the last 5 rows of a data frame. (default: 5)

'''
Out[2]: 
                      Processor  Transistor count  Date of introduction  \
112                      POWER9        8000000000                  2017   
113  IBM z14 Storage Controller        9700000000                  2017   
114            32-core SPARC M7       10000000000                  2015   
115                Centriq 2400       18000000000                  2017   
116            32-core AMD Epyc       19200000000                  2017   

     Designer Process     Area  
112       IBM   14 nm  695 mm²  
113       IBM   14 nm  696 mm²  
114    Oracle   20 nm      NaN  
115  Qualcomm   10 nm  398 mm2  
116       AMD   14 nm  768 mm2  
'''

file.shape

#returns the total number of rows and columns of the excel file.
 
#Out[3]: (117, 6)

file.loc[:7, "Designer"]

#the column label(for example: "Designer") and rows upto 7.

'''
Out[3]: 
0    Texas Instruments
1                Intel
2                Intel
3       MOS Technology
4             Motorola
5                Intel
6                  RCA
7                Intel
Name: Designer, dtype: object
'''

file.loc[4,:]

#the 5th row, and all the columns for the row.

'''
Out[4]: 
Processor               Motorola 6800
Transistor count                 4100
Date of introduction             1974
Designer                     Motorola
Process                      6,000 nm
Area                           16 mm²
Name: 4, dtype: object
'''
