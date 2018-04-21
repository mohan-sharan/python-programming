#init - is the constructor method for a class. It is called called whenever an object of the class is constructed.

class Animal:
    def __init__(self, name):
        self.name = name

    def animalName(self):
        print(self.name)

object1 = Animal("Elephant")
object2 = Animal("Fox")
object1.animalName()
object2.animalName()