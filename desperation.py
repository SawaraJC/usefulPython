
import socket
import threading 
import tkinter 
from tkinter import simpledialog
from tkinter import* 
import tkinter.scrolledtext
from tkinter import ttk 

host='127.0.0.1'
port='9090'

class client:
     def __init__(self, host, port):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))

        root=tkinter.Tk()
        root.title=("SERVER BASED CHAT BOX")

        window_height=500
        window_width=300

def firstwin():
    global screen_height, screen_width, x_cordinate, y_cordinate 

    screen_height=root.winfo_screenheight()
    screen_width=root.winfo_screenwidth()
    x_cordinate=int((screen_width/2)-(window_width/2))
    y_cordinate=int((screen_height/2)-(window_height/2))

    root.geometry('{}+{}+{}+{}'.format(window_width,window_width,x_cordinate,y_cordinate))



firstwin()
root.mainloop()

