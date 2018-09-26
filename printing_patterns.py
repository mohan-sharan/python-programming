print("\n...Program that prints different patterns...\n")
while True:
    print("\nTo Print a Pattern Type: Enter (1-6)")
    print("To Exit Program: Enter any other number\n")
    userChoice = int(input("Enter a number: "))
    if userChoice is 1:
        rows = int(input("Enter the number of rows: "))
        z = 2*rows - 2
        for x in range(0, rows):
            for y in range(0, z):
                print(end=" ")
            z = z - 1
            for y in range(0, x+1):
                print("* ", end="")
            print()
    elif userChoice is 2:
        rows = int(input("Enter the number of rows: "))
        for x in range(0, rows):
            for y in range(0, x+1):
                print("* ", end="")
            print()
    elif userChoice is 3:
        rows = int(input("Enter the number of rows: "))
        z = 2*rows - 2
        for x in range(0, rows):
            for y in range(0, z):
                print(end=" ")
            z = z - 2
            for y in range(0, x+1):
                print("* ", end="")
            print()
    elif userChoice is 4:
        rows = int(input("Enter the number of rows: "))
        n = 1
        for x in range(0, rows):
            for y in range(0, x+1):
                print(n, end=" ")
                n = n + 1
            print()
    elif userChoice is 5:
        rows = int(input("Enter the number of rows: "))
        n = 1
        for x in range(0, rows):
            for y in range(rows, x, -1):
                print(n, end=" ")
                n = n + 1
            print()
            n = 1
    elif userChoice is 6:
        rows = int(input("Enter the number of rows: "))
        value = 65
        for x in range(0, rows):
            for y in range(0, x+1):
                ch = chr(value)
                print(ch, end=" ")
            value = value + 1
            print()
    else:
        quit()

'''
OUTPUT:

...Program that prints different patterns...


To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 1
Enter the number of rows: 5
        *
       * *
      * * *
     * * * *
    * * * * *

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 2
Enter the number of rows: 5
*
* *
* * *
* * * *
* * * * *

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 3
Enter the number of rows: 6
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 4
Enter the number of rows: 6
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 5
Enter the number of rows: 6
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 6
Enter the number of rows: 7
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G

To Print a Pattern Type: Enter (1-6)
To Exit Program: Enter any other number

Enter a number: 7
sharan-mohan@SharanMohan-VirtualBox:~/Desktop$
'''
