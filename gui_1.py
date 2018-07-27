#A simple GUI program layout that contains 1 button, 3 labels and 2 text-entry widgets.

#Tkinter is the most commonly used GUI (Graphical User Interface) toolkit for Python.
#import the "tkinter" module
import tkinter

#create a new window
window = tkinter.Tk()

#set the window background color
window.configure(background="DodgerBlue2")

#set the window size
window.geometry("480x320")

#set the window title
window.title("Intro to GUI Programming - Python")

#create label + text entry widgets
label0 = tkinter.Label(window, text="Enter your Favorite Anime Series + Character", bg="gold", font=("Helvetica", 16))

label1 = tkinter.Label(window, text="SERIES", bg="yellowgreen", font=("Times", 14))
txtent1 = tkinter.Entry(window)

label2 = tkinter.Label(window, text="CHARACTER", bg="yellowgreen", font=("Times", 14))
txtent2 = tkinter.Entry(window)

#create a button widget
btn = tkinter.Button(window, text="SUBMIT", bg="firebrick2", font=("Times", 20))

#pack (add) the widgets into the window
label0.pack(padx=0, pady=30)

label1.pack()
txtent1.pack(padx=0, pady=10)

label2.pack()
txtent2.pack(padx=0, pady=10)

btn.pack(padx=0, pady=20)

#draw the application, and start the 'application'
window.mainloop()

#check out the file gui_1.PNG for output