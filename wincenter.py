#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()

#Set the geometry
win.geometry("400x250")

win.eval('tk::PlaceWindow . center')

win.mainloop()