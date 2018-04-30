#SIMPLE PROGRAM TO SORT A CAR BY ITS TOP SPEED

import operator

#Read the names and their top speeds(mph) of atleast 3 cars

def readCarDetails():
    print("Enter the number of cars: ")
    numberOfCars = int(input())
    carRecord = {}
    for car in range(0, numberOfCars):
        print("Enter the name of a car: ")
        name = input()
        print("Enter the top speed of the car (mph): ")
        topSpeed = float(input())
        carRecord[name] = topSpeed
    return carRecord

def rankCars(carRecord):
    try:
        sortedCarRecord = sorted(carRecord.items(), key=operator.itemgetter(1), reverse=True)
        print(sortedCarRecord)
        print("{} has a top speed of {} mph and is the fastest in the lot.".format(sortedCarRecord[0][0], sortedCarRecord[0][1]))
        print("{} has a top speed of {} mph and is the second fastest in the lot.".format(sortedCarRecord[1][0], sortedCarRecord[1][1]))
        print("{} has a top speed of {} mph and is the slowest in the lot.".format(sortedCarRecord[2][0], sortedCarRecord[2][1]))
        return sortedCarRecord
    except IndexError:
        print("Enter a minimum of 3 cars!")
        quit()


carRecord = readCarDetails()
sortedCarRecord = rankCars(carRecord)

'''
OUTPUT 1:
Enter the number of cars: 
3
Enter the name of a car: 
Veyron
Enter the top speed of the car (mph): 
254.04
Enter the name of a car: 
Aventador
Enter the top speed of the car (mph): 
217
Enter the name of a car: 
Agera RS
Enter the top speed of the car (mph): 
284
[('Agera RS', 284.0), ('Veyron', 254.04), ('Aventador', 217.0)]
Agera RS has a top speed of 284.0 mph and is the fastest in the lot.
Veyron has a top speed of 254.04 mph and is the second fastest in the lot.
Aventador has a top speed of 217.0 mph and is the slowest in the lot.

OUTPUT 2:
Enter the number of cars: 
1
Enter the name of a car: 
Veyron
Enter the top speed of the car (mph): 
254.04
[('Veyron', 254.04)]
Veyron has a top speed of 254.04 mph and is the fastest in the lot.
Enter a minimum of 3 cars!
'''