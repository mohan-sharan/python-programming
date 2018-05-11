#FACTORIAL
#Denoted by n!
#where n = non-negative integer
#is the product of all positive integers less than or equal to n.
#For example: 4! = 4*3*2*1 = 24

n = int(input("Enter a number to find its factorial: "))

fact = 1

if (n == 0):
    print("The Factorial of 0 is 1.")

elif (n < 0):
    print("INVALID! Factorial doesn't exist for negative numbers.")

else:
    for i in range(1, n+1):
        fact = fact * i
    print("{}! is {}.".format(n, fact))

'''
OUTPUT 1:
Enter a number to find its factorial: -4
INVALID! Factorial doesn't exist for negative numbers.
'''

'''
OUTPUT 2:
Enter a number to find its factorial: 0
The Factorial of 0 is 1.
'''

'''
OUTPUT 3:
Enter a number to find its factorial: 6
6! is 720.
'''