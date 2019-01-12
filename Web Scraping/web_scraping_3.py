#PROGRAM TO EXTRACT POKEDEX DATA
#WEBSITE: https://pokemondb.net/

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url = requests.get("https://pokemondb.net/pokedex/all")
soup = BeautifulSoup(url.content, 'html.parser')

pokemon_names = []
pokemon_types = []
pokemon_no = []
pokemon_hp = []
pokemon_attack = []
pokemon_defense = []
pokemon_speed = []

names = soup.find_all('td', class_="cell-name")

for x in names:
    pokemon_names.append(x.get_text())

types = soup.find_all('td', class_="cell-icon")

for x in types:
    pokemon_types.append(x.get_text())

testDataFrame = pd.DataFrame({"NAME": pokemon_names, "TYPE": pokemon_types})
print(testDataFrame.head())
'''
                    NAME         TYPE
0              Bulbasaur  GrassPoison
1                Ivysaur  GrassPoison
2               Venusaur  GrassPoison
3  VenusaurMega Venusaur  GrassPoison
4             Charmander         Fire
'''
      
other_data = []
for x in soup.find_all(attrs={'class': 'cell-num'}):
    other_data.append(x.get_text())

print(other_data[0:7])
'''
[u'001', u'45', u'49', u'49', u'65', u'65', u'45']
'''
#FORMAT: [NUMBER, HP, ATTACK, DEFENSE, SP.ATTACK, SP.DEFENSE, SPEED]
#NOTE: For this script, except "SP.ATTACK" and "SP.DEFENSE", all the above other parameters are considered.

for i in range(0,len(other_data),7):
    pokemon_no.append(other_data[i])

print(pokemon_no[0:5]) #NUMBER
'''
[u'001', u'002', u'003', u'003', u'004']
'''

for i in range(1,len(other_data),7):
    pokemon_hp.append(other_data[i])
        
print(pokemon_hp[0:5]) #HP
'''
[u'45', u'60', u'80', u'80', u'39']
'''

for i in range(2,len(other_data),7):
    pokemon_attack.append(other_data[i])
 
print(pokemon_attack[0:5]) #ATTACK
'''
[u'49', u'62', u'82', u'100', u'52']
'''

for i in range(3,len(other_data),7):
    pokemon_defense.append(other_data[i])

print(pokemon_defense[0:5]) #DEFENSE
'''
[u'49', u'63', u'83', u'123', u'43']
'''

for i in range(6,len(other_data),7):
    pokemon_speed.append(other_data[i])
        
print(pokemon_speed[0:5]) #SPEED
'''
[u'45', u'60', u'80', u'80', u'65']
'''

pokemon_hp = [int(i) for i in pokemon_hp]
pokemon_defense = [int(i) for i in pokemon_defense]
pokemon_attack = [int(i) for i in pokemon_attack]
pokemon_speed = [int(i) for i in pokemon_speed]

final_data = {"#": pokemon_no, 
	      "NAME": pokemon_names, 
              "TYPE": pokemon_types, 
	      "HP": pokemon_hp, 
	      "ATTACK": pokemon_attack, 
	      "DEFENSE": pokemon_defense, 
	      "SPEED": pokemon_speed}

finalDataFrame = pd.DataFrame(final_data)

print(finalDataFrame.head(10))
''' 
     # ATTACK DEFENSE  HP                       NAME SPEED         TYPE
0  001     49      49  45                  Bulbasaur    45  GrassPoison
1  002     62      63  60                    Ivysaur    60  GrassPoison
2  003     82      83  80                   Venusaur    80  GrassPoison
3  003    100     123  80      VenusaurMega Venusaur    80  GrassPoison
4  004     52      43  39                 Charmander    65         Fire
5  005     64      58  58                 Charmeleon    80         Fire
6  006     84      78  78                  Charizard   100   FireFlying
7  006    130     111  78  CharizardMega Charizard X   100   FireDragon
8  006    104      78  78  CharizardMega Charizard Y   100   FireFlying
9  007     48      65  44                   Squirtle    43        Water
'''
print(finalDataFrame.tail(5))
'''
       # ATTACK DEFENSE   HP         NAME SPEED       TYPE
921  805    131     211   61    Stakataka    13  RockSteel
922  806    127      53   53  Blacephalon   107  FireGhost
923  807    112      75   88      Zeraora   143   Electric
924  808     65      65   46       Meltan    34      Steel
925  809    143     143  135     Melmetal    34      Steel
'''

def split_text(text):
    myList = []
    for i in text:
        myList.append(i)
    for index in range(1, len(myList)):    
        if myList[index].isupper():
            myList[index] = '/' + myList[index]
    myList = ''.join(myList)        
    return myList

text = 'FireFlying'
print(split_text(text))
#OUTPUT: Fire/Flying

finalDataFrame['TYPE'] = finalDataFrame['TYPE'].apply(split_text)
print(finalDataFrame.head(10))
'''
     # ATTACK DEFENSE  HP                       NAME SPEED          TYPE
0  001     49      49  45                  Bulbasaur    45  Grass/Poison
1  002     62      63  60                    Ivysaur    60  Grass/Poison
2  003     82      83  80                   Venusaur    80  Grass/Poison
3  003    100     123  80      VenusaurMega Venusaur    80  Grass/Poison
4  004     52      43  39                 Charmander    65          Fire
5  005     64      58  58                 Charmeleon    80          Fire
6  006     84      78  78                  Charizard   100   Fire/Flying
7  006    130     111  78  CharizardMega Charizard X   100   Fire/Dragon
8  006    104      78  78  CharizardMega Charizard Y   100   Fire/Flying
9  007     48      65  44                   Squirtle    43         Water
'''
print(finalDataFrame.describe())
'''
           ATTACK     DEFENSE          HP       SPEED
count  926.000000  926.000000  926.000000  926.000000
mean    80.066955   74.502160   69.535637   74.502160
std     32.508558   31.202313   26.073665   31.202313
min      5.000000    5.000000    1.000000    5.000000
25%     55.000000   50.000000   50.000000   50.000000
50%     75.000000   70.000000   66.500000   70.000000
75%    100.000000   90.000000   80.000000   90.000000
max    190.000000  230.000000  255.000000  230.000000
'''
#ANALYSIS
def poke_statistics(finalDataFrame, COLUMNS):
    for i in COLUMNS:
        min_values = finalDataFrame[i].min()
        min_names = finalDataFrame[finalDataFrame[i] == min_values]['NAME'].values[0]
        print(min_names + " --> (MIN) " + i + " = " + str(min_values))
        max_values = finalDataFrame[i].max()
        max_names = finalDataFrame[finalDataFrame[i] == max_values]['NAME'].values[0]
        print(max_names + " --> (MAX) " + i + " = " + str(max_values))

COLUMNS = ['ATTACK', 'HP', 'DEFENSE', 'SPEED']

print(poke_statistics(finalDataFrame, COLUMNS))
'''
Chansey --> (MIN) ATTACK = 5
MewtwoMega Mewtwo X --> (MAX) ATTACK = 190
Shedinja --> (MIN) HP = 1
Blissey --> (MAX) HP = 255
Chansey --> (MIN) DEFENSE = 5
SteelixMega Steelix --> (MAX) DEFENSE = 230
Chansey --> (MIN) SPEED = 5
SteelixMega Steelix --> (MAX) SPEED = 230
'''
