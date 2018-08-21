#Split
#Breaks a large string and returns a list of smaller strings.

#EXAMPLE: 1
pokemonType = "Electric/Fire/Water/Ground/Grass/Psychic"
split_1 = pokemonType.split("/")
print(split_1)

#OUTPUT: ['Electric', 'Fire', 'Water', 'Ground', 'Grass', 'Psychic']

for s in split_1:
    print(s)

'''
OUTPUT:
Electric
Fire
Water
Ground
Grass
Psychic
'''

split_1 = pokemonType.split("/", 3) #Maximum number of splits = 3
for s in split_1:
    print(s)

'''
OUTPUT:
Electric
Fire
Water
Ground/Grass/Psychic
'''

#EXAMPLE: 2
myFile = open("Example File")
for lines in myFile:
    print(lines)

'''
Pokemon Generation 1

Evolution: Starter Pokemon

Type: Grass

Bulbasaur - Ivysaur - Venusaur

Type: Fire

Charmander - Charmeleon - Charizard

Type: Water

Squirtle - Wartortle - Blastoise
'''

for lines in myFile.read().split(": "):
    print(lines)

'''
Pokemon Generation 1
Evolution
Starter Pokemon
Type
Grass
Bulbasaur - Ivysaur - Venusaur
Type
Fire
Charmander - Charmeleon - Charizard
Type
Water
Squirtle - Wartortle - Blastoise
'''

for lines in myFile.read().split(" - "):
    print(lines)

'''
Pokemon Generation 1
Evolution: Starter Pokemon
Type: Grass
Bulbasaur
Ivysaur
Venusaur
Type: Fire
Charmander
Charmeleon
Charizard
Type: Water
Squirtle
Wartortle
Blastoise
'''