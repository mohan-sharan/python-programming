#a simple program to demonstrate the handling of exceptions.
#try-except block.

a = int(input("Enter a number:\n"))
b = int(input("Enter another number:\n"))

c = a/b
print("\na/b = ", c)

'''
OUTPUT 1:
Enter a number:
5
Enter another number:
2

a/b =  2.5

Process finished with exit code 0

OUTPUT 2:
Enter a number:
5
Enter another number:
0
Traceback (most recent call last):
  File "C:/Users/PycharmProjects/tutorial/basics.py", line 4, in <module>
    c = a/b
ZeroDivisionError: division by zero

Process finished with exit code 1
'''

a = int(input("Enter a number:\n"))
b = int(input("Enter another number:\n"))

try:
    c = a/b
    print("\na/b = ", c)
except ZeroDivisionError:
    print("Divide By Zero Error!")

'''
OUTPUT:
Enter a number:
5
Enter another number:
0
Divide By Zero Error!

Process finished with exit code 0
'''