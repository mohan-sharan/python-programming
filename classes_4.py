#MULTILEVEL INHERITANCE

class Engine:
    numberCylinders = 16


class Material(Engine):
    materialType = "Carbon fiber"


class Bugatti(Material):
    def __init__(self):
        self.topSpeed = "254 mph"
        print("The Bugatti Veyron has a top speed of {}. It is"
        " made of {} and has a {} cylinder engine!" .format(self.topSpeed, self.materialType, self.numberCylinders))

object = Bugatti()

#OUTPUT
#The Bugatti Veyron has a top speed of 254 mph. It is made of Carbon fiber and has a 16 cylinder engine!
