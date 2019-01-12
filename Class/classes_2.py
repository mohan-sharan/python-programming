#single inheritance

#Inheritance is a powerful feature in object oriented programming. It refers to defining a new class with little or no modification to an existing class. 
#The new class is called derived (example: GT) class and the one from which it inherits is called the base (example: Ford) class.

class Ford:
    manufacturer = "Ford Motor Company"
    contactWebsite = "www.ford.com/contact"

    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)

class GT(Ford):
    def __init__(self):
        self.yearOfManufacture = 2015

    def manufacturerDetails(self):
        print("This GT was manufactured in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))

ford = GT()
ford.manufacturerDetails()
ford.contactDetails()
        
#OUTPUT:
#This GT was manufactured in the year 2015 by Ford Motor Company
#To contact us, log on to  www.ford.com/contact
