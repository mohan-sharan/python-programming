myList = ['T', 'O', 'P', '', 'G', 'E', 'A', 'R']
i = 0
while i < len(myList):
    print(myList[i], end=" ")
    i += 1

#OUTPUT: T O P  G E A R 	
	
#append() method
myList.append("R")
print("\nUpdated List: ", myList)

#OUTPUT: Updated List:  ['T', 'O', 'P', '', 'G', 'E', 'A', 'R', 'R']

#pop() method
print(myList.pop()) #removes the last element from the list

#OUTPUT: R

#remove() method
myList.remove('T')
print("Updated List: ", myList)

#OUTPUT: Updated List:  ['O', 'P', '', 'G', 'E', 'A', 'R']
