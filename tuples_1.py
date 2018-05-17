#Tuples

myTuple1 = ("07-06-1969", "01-23-1996")
print(myTuple1[0])
print(myTuple1[1])

'''
OUTPUT:
07-06-1969
01-23-1996
'''

#del doesn't work on a tuple. The output below shows what happens when del is called.
del(myTuple1[0])

'''
OUTPUT:
  File "C:/Users/PycharmProjects/tutorial/basics.py", line 5, in <module>
    del(myTuple1[0])
TypeError: 'tuple' object doesn't support item deletion

Process finished with exit code 1
'''


myTuple2 = ("Smashing Pumpkins", "Foo Fighters", "Fleetwood Mac", "Matchbox Twenty", "Silversun Pickups")
print("The length of the tuple is:", len(myTuple2))
for x in myTuple2:
    print(x, end="  ")

'''
OUTPUT:
The length of the tuple is: 5
Smashing Pumpkins  Foo Fighters  Fleetwood Mac  Matchbox Twenty  Silversun Pickups 
'''		