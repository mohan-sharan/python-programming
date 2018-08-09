#String Methods (common examples)
#Returns Boolean Values

myString = "MOBILE SUIT GUNDAM"
print(myString.isupper()) #prints "True" if all the characters are uppercase
#OUTPUT: True

myString1 = "mobile suit gundam"
print(myString1.islower()) #prints "True" if all the characters are lowercase
#OUTPUT: True

myString2 = "RX-0 Unicorn Gundam"
print(myString2.isalpha()) #prints "False" if the string contains one or more non-alphabets
#OUTPUT: False

myString3 = "Gundam00"
print(myString3.isalnum()) #prints "True" if the string contains alphanumeric characters and no spaces
#OUTPUT: True

#String swapcase() method

myString4 = "MecHa ANime"
print(myString4.swapcase()) #swaps the case of each character in the string
#OUTPUT: mEChA anIME

myString5 = "the psychoframe"
print(myString5.swapcase())
#OUTPUT: THE PSYCHOFRAME
