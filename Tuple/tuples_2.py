myTuple1 = ("B", "U", "R", "R", "I", "T", "O")
print(type(myTuple1)) #type() is a built-in function that returns the type of an object.

#OUTPUT: <class 'tuple'>

myTuple2 = ("TACO", "Cost:$", 2.98, "How many?", 2)
for x in myTuple2:
    print(x, type(x))

'''
OUTPUT:
TACO <class 'str'>
Cost:$ <class 'str'>
2.98 <class 'float'>
How many? <class 'str'>
2 <class 'int'>
'''

#append doesn't work on a tuple. The output below shows what happens when append is called.
myTuple2.append("Jalapenos")

'''
OUTPUT:
Traceback (most recent call last):
  File "C:/Users/PycharmProjects/tutorial/basics.py", line 6, in <module>
    myTuple2.append("Jalapenos")
AttributeError: 'tuple' object has no attribute 'append'

Process finished with exit code 1
'''

myTuple3 = ('Tortilla', 'Chips')
c = myTuple3 * 2
print(c)

#OUTPUT: ('Tortilla', 'Chips', 'Tortilla', 'Chips')

myTuple4 = ('Hard-Shell ')
myTuple5 = ('Taco')
d = myTuple4 + myTuple5
print(d)

#OUTPUT: Hard-Shell Taco	
