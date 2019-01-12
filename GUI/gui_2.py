#SIMPLE TEMPERATURE LOGGER (GUI)
#SUBMIT BUTTON - prints the values on to the terminal.
#EXIT BUTTON - terminates the application.

import tkinter

window = tkinter.Tk()
window.configure(background="MediumPurple1")
window.geometry("480x200")
window.title("Temperature Input")

def showTextField():
   print("\nCity: {}".format(e0.get()))
   print("Current Temperature (F): {}\n".format(e1.get()))
 
#Labels
l0 = tkinter.Label(window, text="TEMPERATURE LOGGER (GUI)", bg="DeepSkyBlue2", font=("Verdana", 14))
l1 = tkinter.Label(window, text="City", width=22, bg="orange", font=("Times", 14))
l2 = tkinter.Label(window, text="Current Temperature (F)", width=22, bg="orange", font=("Times", 14))

l0.grid(row=0, padx=5, pady=10)
l1.grid(row=1, pady=5)
l2.grid(row=2, pady=5)

#Text-Entry
e0 = tkinter.Entry(window)
e1 = tkinter.Entry(window)

e0.grid(row=1, column=1, pady=5)
e1.grid(row=2, column=1, pady=5)

#Buttons
b0 = tkinter.Button(window, text="SUBMIT", command=showTextField, bg="lime green", font=("Times", 18))
b1 = tkinter.Button(window, text="EXIT", command=window.quit, bg="firebrick2", font=("Times", 18))

b0.grid(row=4, column=1, pady=10)
b1.grid(row=4, column=0, pady=10)

#draw the application, and start the 'application'
window.mainloop()

#check out the file gui_2.PNG for output.
