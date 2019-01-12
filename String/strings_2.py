myString1 = "iT's A BeauTifuL DaY!"
print(myString1.upper()) #prints all the characters in upper case
#OUTPUT: IT'S A BEAUTIFUL DAY!

print(myString1.lower()) #prints all the characters in lower case
#OUTPUT: it's a beautiful day!

myString2 = "Mclaren"
print(myString2)
#OUTPUT: Mclaren

print(myString2[::-1]) #prints the string in reverse order
#OUTPUT: neralcM

#To check if a string is a Palindrome
myString = input("Enter a string: ")
if (myString == myString[::-1]):
    print("The string {} is a palindrome.".format(myString))
else:
    print("The string {} is not a palindrome.".format(myString))

#OUTPUT 1:
#Enter a string: ABBA
#The string ABBA is a palindrome.

#OUTPUT 2:
#Enter a string: AUDI
#The string AUDI is not a palindrome.
