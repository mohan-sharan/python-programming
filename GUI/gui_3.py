#POKEDEX v.0.1 - GUI
#WEBSITE: https://pokemondb.net/pokedex/all
'''
1. Enter a number between 0 and 925.
2. Click the "WHO'S THAT POKEMON?" button to get the required pokemon's stats [NAME, HP, ATTACK, DEFENSE, SPEED, TYPE].
3. Click the "CLEAR" button to erase the current stats and repeat step 1 & 2.
4. Click the "QUIT" button to exit from the GUI. 
'''

from Tkinter import *
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk

url = requests.get("https://pokemondb.net/pokedex/all")
soup = BeautifulSoup(url.content, 'html.parser')

#Data
pokemon_names = []
pokemon_hp = []
pokemon_attack = []
pokemon_defense = []
pokemon_speed = []
pokemon_types = []

names = soup.find_all('td', class_="cell-name")
for x in names:
    pokemon_names.append(x.get_text())

pokemon_name = [x.encode('utf-8') for x in pokemon_names]

types = soup.find_all('td', class_="cell-icon")
for x in types:
    pokemon_types.append(x.get_text())

other_data = []
for x in soup.find_all(attrs={'class': 'cell-num'}):
    other_data.append(x.get_text())

for i in range(1,len(other_data),7):
    pokemon_hp.append(other_data[i])

for i in range(2,len(other_data),7):
    pokemon_attack.append(other_data[i])

for i in range(3,len(other_data),7):
    pokemon_defense.append(other_data[i])

for i in range(6,len(other_data),7):
    pokemon_speed.append(other_data[i])

pokemon_hp = [int(i) for i in pokemon_hp]
pokemon_defense = [int(i) for i in pokemon_defense]
pokemon_attack = [int(i) for i in pokemon_attack]
pokemon_speed = [int(i) for i in pokemon_speed]

window = Tk()
window.configure(background="firebrick2")
window.geometry("525x700")
window.title("POKEDEX v.0.1")

#Labels
l1 = Label(window, text="ENTER A NUMBER: 0-925", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l2 = Label(window, text="NAME", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l3 = Label(window, text="HP", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l4 = Label(window, text="ATTACK", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l5 = Label(window, text="DEFENSE", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l6 = Label(window, text="SPEED", width=25, bg="gray25", fg="ghost white", font=("Times", 14))
l7 = Label(window, text="TYPE", width=25, bg="gray25", fg="ghost white", font=("Times", 14))

l1.grid(row=1, column=0, pady=15)
l2.grid(row=2, column=0, pady=5)
l3.grid(row=3, column=0, pady=5)
l4.grid(row=4, column=0, pady=5)
l5.grid(row=5, column=0, pady=5)
l6.grid(row=6, column=0, pady=5)
l7.grid(row=7, column=0, pady=5)

#Image
imagePath = "/home/user/Desktop/POKEBALL.PNG"
i = Image.open(imagePath)
pokemon_image = ImageTk.PhotoImage(i)
i1 = Label(window, image=pokemon_image)
i1.grid(row=0, column=0, padx=10, pady=10)

#Text-Entries
e1 = Entry(window)
e2 = Text(window, width=25, height=1)
e3 = Text(window, width=25, height=1)
e4 = Text(window, width=25, height=1)
e5 = Text(window, width=25, height=1)
e6 = Text(window, width=25, height=1)
e7 = Text(window, width=25, height=1)

e1.grid(row=1, column=1, pady=5)
e2.grid(row=2, column=1, pady=5)
e3.grid(row=3, column=1, pady=5)
e4.grid(row=4, column=1, pady=5)
e5.grid(row=5, column=1, pady=5)
e6.grid(row=6, column=1, pady=5)
e7.grid(row=7, column=1, pady=5)

def insert_data():
    try:
        temp = e1.get()
        data = int(temp)
        e2.insert(END, pokemon_name[data])
        e3.insert(END, pokemon_hp[data])
        e4.insert(END, pokemon_attack[data])
        e5.insert(END, pokemon_defense[data])
        e6.insert(END, pokemon_speed[data])
        e7.insert(END, pokemon_types[data])
    except IndexError:
        print("Number should be between: 0-925")
    except ValueError:
        print("Input should be a number")
        
def clear():
    e2.delete('1.0', END)
    e3.delete('1.0', END)
    e4.delete('1.0', END)
    e5.delete('1.0', END)
    e6.delete('1.0', END)
    e7.delete('1.0', END)

#Buttons
b1 = Button(window, text="WHO'S THAT POKEMON?", command=insert_data, bg="forest green", fg="gray7", font=("Times", 16))

b2 = Button(window, text="QUIT", command=window.quit, bg="royal blue", fg="ghost white", font=("Times", 18))

b3 = Button(window, text="CLEAR", command=clear, bg="gold", fg="gray7", font=("Times", 16))

b1.grid(row=8, column=0, padx=5, pady=10)
b2.grid(row=8, column=1, padx=5, pady=10)
b3.grid(row=9, column=0, padx=5, pady=10)

#Start the Application
window.mainloop()
