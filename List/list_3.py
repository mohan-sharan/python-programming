#NESTED LISTS
x = [["Lead", "Copper", "Aluminum"], ["Pb", "Cu", "Al"]]
print(x)
print(x[0])
print(x[1])
print("The length of x is:", len(x))

print(x[0] * 3) #prints the value at index[0] 3 times

del x[0]
print("After deleting value at index 0, x is:", x)

'''
OUTPUT:
[['Lead', 'Copper', 'Aluminum'], ['Pb', 'Cu', 'Al']]
['Lead', 'Copper', 'Aluminum']
['Pb', 'Cu', 'Al']
The length of x is: 2
['Lead', 'Copper', 'Aluminum', 'Lead', 'Copper', 'Aluminum', 'Lead', 'Copper', 'Aluminum']
After deleting value at index 0, x is: [['Pb', 'Cu', 'Al']]
'''
