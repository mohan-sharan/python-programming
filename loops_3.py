#What is a continue statement?
#It is used to skip a particular iteration of the loop.

x = 1
while x <= 7:
	if x == 5:
		x += 1
		continue
	print("x =", x)
	x += 1
	
#When x = 5, "continue" stops further execution of that iteration and moves on to the next iteration.
'''
OUTPUT:
x = 1
x = 2
x = 3
x = 4
x = 6
x = 7
'''
