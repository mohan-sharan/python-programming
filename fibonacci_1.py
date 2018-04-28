#Fibonacci Sequence: 
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def f(n):
    if(n <= 1):
        return n
    else:
        return (f(n-1) + f(n-2))

num = int(input("Enter the number of terms you want in the sequence:"))
print("The Fibonacci Sequence:")
for i in range(num):
    print(f(i), end=" ")

'''
OUTPUT 1:
Enter the number of terms you want in the sequence: 7
The Fibonacci Sequence:
0 1 1 2 3 5 8 	

OUTPUT 2:
Enter the number of terms you want in the sequence:17
The Fibonacci Sequence:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
'''
