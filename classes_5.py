#METHODS
#A function within a class that performs a specific action is called a method belonging to that class.
#Methods are of two types: static method and instance method

'''
STATIC METHOD
A method that does not have access to any of the instance
attributes of a class is called a static method.

Static method uses a decorator @staticmethod to indicate
this method will not be taking the default self parameter.
'''

class Pokemon:
    numberOfPokemon = 0
    myPokemonCollection = []

    def __init__(self, name):
        self.name = name

        #Let's increment the number of Pokemon
        Pokemon.numberOfPokemon += 1

        #Append the Pokemon to the list if total number of Pokemons are less than 5
        if Pokemon.numberOfPokemon <= 5:
            Pokemon.myPokemonCollection.append(self)
        else:
        #If more than 5 Pokemons are present, delete the 1st one and store a new Pokemon
            del Pokemon.myPokemonCollection[0]
            Pokemon.myPokemonCollection.append(self)

    @staticmethod
    def displayPokemon():
        for pokemon in Pokemon.myPokemonCollection:
            print(pokemon.name, end='')
            print("")

pokemonOne = Pokemon("Blastoise")
pokemonTwo = Pokemon("Typhlosion")
pokemonThree = Pokemon("Blaziken")
pokemonFour = Pokemon("Swampert")
pokemonFive = Pokemon("Lugia")
pokemonFive.displayPokemon()

'''
OUTPUT:
Blastoise
Typhlosion
Blaziken
Swampert
Lugia
'''

#To print all the Pokemon after deleting the first Pokemon
#pokemonSix = Pokemon("Mew")
#pokemonSix.displayPokemon()

'''
OUTPUT:
Typhlosion
Blaziken
Swampert
Lugia
Mew
'''
