myList = []
for i in range(4):
  myList.append("S" * 4)

def printMyList(myList_in):
  for x in myList:
    print(" ".join(x))

printMyList(myList)

'''
OUTPUT:
S S S S
S S S S
S S S S
S S S S
'''
