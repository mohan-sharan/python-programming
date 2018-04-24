class Tesla:
    carType = "Electric" #Public => memberName
    _horsepower = 518 #Protected => _memberName
    __doorType = "Falcon Wing" #Private => __memberName

class ModelX(Tesla):
    def __init__(self):
        print("horsepower (Protected):", self._horsepower)

tesla = Tesla()
print("carType (Public Attribute):", tesla.carType)

modelx = ModelX()
print("doorType (Private Attribute):", tesla._Tesla__doorType)

'''
OUTPUT:
carType (Public Attribute): Electric
horsepower (Protected): 518
doorType (Private Attribute): Falcon Wing
'''
