#The Python join() method
#EXAMPLE: 1
myList = ["Cyndaquil", "Quilava", "Typhlosion"]
join_myList = "->".join(myList)
print(join_myList)

#OUTPUT: Cyndaquil->Quilava->Typhlosion

#EXAMPLE: 2
myString = "POKEMON"
join_myString = ".".join(myString)
print(join_myString)

#OUTPUT: P.O.K.E.M.O.N

#EXAMPLE: 3
import pandas as pd

df1 = pd.DataFrame(
{"Pokemon Gen 1": ["Sandshrew", "Charmander", "Pikachu", "Bulbasaur"],
"Type": ["Ground", "Fire", "Electric", "Grass"]}
)

print(df1)

'''
  Pokemon Gen 1      Type
0     Sandshrew    Ground
1    Charmander      Fire
2       Pikachu  Electric
3     Bulbasaur     Grass
'''

df2 = pd.DataFrame(
{"Pokemon Gen 2": ["Totodile", "Cyndaquil", "Chikorita", "Phanpy"],
"Type": ["Water", "Fire", "Grass", "Ground"]}
)

print(df2)

'''
  Pokemon Gen 2    Type
0      Totodile   Water
1     Cyndaquil    Fire
2     Chikorita   Grass
3        Phanpy  Ground

'''

join_df = df1.join(df2, lsuffix=" Gen 1", rsuffix=" Gen 2")
print(join_df)

'''
  Pokemon Gen 1 Type Gen 1 Pokemon Gen 2 Type Gen 2
0     Sandshrew     Ground      Totodile      Water
1    Charmander       Fire     Cyndaquil       Fire
2       Pikachu   Electric     Chikorita      Grass
3     Bulbasaur      Grass        Phanpy     Ground
'''
