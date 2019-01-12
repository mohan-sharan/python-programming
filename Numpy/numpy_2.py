#NUMPY STACK

import numpy as np
x = np.zeros((3,3))
print(x)

'''
OUTPUT:
[[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
'''

y = np.ones((3,3))
print(y)

'''
OUTPUT:
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
'''

z = np.random.random((2,2))
print(z)

'''
OUTPUT:
[[ 0.05330872  0.94978062]
 [ 0.33120876  0.82741279]]
'''

a = np.array([5,8])
print(a.dtype)

#OUTPUT: int64

b = np.array([5.0,8.0])
print(b.dtype)

#OUTPUT: float64

c = np.array([[0,1],[2,3]])
d = np.array([[4,5],[6,7]])

print(np.add(c,d))
#print(c+d) would also produce the same result

'''
OUTPUT:
[[ 4  6]
 [ 8 10]]
'''

print(np.multiply(c,d))
#print(c*d) - Elementwise product

'''
OUTPUT:
[[ 0  5]
 [12 21]]
'''

v = np.array((1,2,3,4))
w = np.array((5,6,7,8))
print(v+w)

#OUTPUT: [6 8 10 12] 
