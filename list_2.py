#CREATE A LIST TO STORE ANY 5 EVEN NUMBERS
evenNumbers = [2, 4, 6, 8, 10]
print(evenNumbers)

#UPDATE THE ELEMENT AT THE 4TH POSITION TO 18
evenNumbers[3] = 18
print(evenNumbers)

#CREATE A LIST TO STORE ANY 5 ODD NUMBERS
oddNumbers = [1, 3, 5, 7, 9]
print(oddNumbers)

#CONCATENATE BOTH THE EVEN AND ODD LISTS
concatenatedList = oddNumbers + evenNumbers
print(concatenatedList)

'''
OUTPUT
[2, 4, 6, 8, 10]
[2, 4, 6, 18, 10]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 2, 4, 6, 18, 10]
'''
