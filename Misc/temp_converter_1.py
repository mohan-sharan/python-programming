#temperature converter

print("A SIMPLE TEMPERATURE CONVERTER PROGRAM\n")

while True:
    print("Enter 1 to convert temperature from Celsius to Fahrenheit:")
    print("Enter 2 to convert temperature from Fahrenheit to Celsius:")
    print("Enter 3 to EXIT!")
    userChoice = int(input("\nEnter your choice: "))
    if userChoice is 1:
        tempC = float(input("Enter a number to find it's temperature equivalent in Fahrenheit: "))
        tempF = float(tempC * 1.8 + 32)
        print("\nThe temperature in Fahrenheit is:", round(tempF, 3))
    elif userChoice is 2:
        tempF = float(input("Enter a number to find it's temperature equivalent in Celsius: "))
        tempC = float((tempF - 32) * 5/9)
        print("\nThe temperature in Celsius is:", round(tempC, 3))
    elif userChoice is 3:
        quit()

'''
OUTPUT:
A SIMPLE TEMPERATURE CONVERTER PROGRAM

Enter 1 to convert temperature from Celsius to Fahrenheit:
Enter 2 to convert temperature from Fahrenheit to Celsius:
Enter 3 to EXIT!

Enter your choice: 1
Enter a number to find it's temperature equivalent in Fahrenheit: 34.5

The temperature in Fahrenheit is: 94.1
Enter 1 to convert temperature from Celsius to Fahrenheit:
Enter 2 to convert temperature from Fahrenheit to Celsius:
Enter 3 to EXIT!

Enter your choice: 2
Enter a number to find it's temperature equivalent in Celsius: 101

The temperature in Celsius is: 38.333
Enter 1 to convert temperature from Celsius to Fahrenheit:
Enter 2 to convert temperature from Fahrenheit to Celsius:
Enter 3 to EXIT!

Enter your choice: 3

Process finished with exit code 0
'''		
