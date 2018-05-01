#Solving a Linear System
#A.x = b
#x = A^(-1).b

import numpy as np

A = np.array([[4,5],[6,7]])

print(A)

'''
OUTPUT:
[[4 5]
 [6 7]]
'''

b = np.array([1,2])

print(b)

'''
OUTPUT:
[1, 2]
'''

x = np.linalg.inv(A).dot(b)

print(x)

'''
OUTPUT:
[ 1.5, -1. ]
'''

x = np.linalg.solve(A, b)

print(x)

'''
OUTPUT:
[ 1.5, -1. ]
''' 
