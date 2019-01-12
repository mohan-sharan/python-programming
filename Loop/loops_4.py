#What is a break statement?
#It stops the execution of the statement in the current/innermost loop and 
#starts executing the next line of code after the block.

x = 20
while x > 10:
    print("x =", x)
    x -= 1
    if x == 15:
        break

print("BREAK")

'''
OUTPUT:
x = 20
x = 19
x = 18
x = 17
x = 16
BREAK
'''
