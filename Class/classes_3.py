class Car:
    def carDetails(self):
        self.name = input("Enter the name of a car:")
        self.type = input("Enter the car's type:")

    def printCarDetails(self):
        print("\nThe car's name:", self.name)
        print("\nThe car's type:", self.type)

car = Car()
car.carDetails()
car.printCarDetails()

'''
OUTPUT:
Enter the name of a car: Honda
Enter the car's type: Sedan

The car's name:  Honda

The car's type:  Sedan
'''
