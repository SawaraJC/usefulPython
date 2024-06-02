import socket
import threading
'''from operator import truediv
from site import check_enableusersite'''
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog


HOST = 'localhost'
PORT =1024 
self.text_area.config(state='normal')
                                
class Client:
    def_init_(self,host,port)
    self.sdck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.sock.connect((host,port))

    msg = tkinter.Tk()
    msg = withdraw()

    self.nickname = simpledialog.askstring("Nickname","Please choose a nickname",parent=msg)

    self.gui_done = False
    self.running = True
     
    gui_thread = threading.Thread(target=self.gui_loop)
    receive_thread = threading.Thread(target=self.receive)

    gui_thread.start()
    receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray") 

        self.chat_lable = tkinter.lable(self.win,text="chat:",bg="lightgray")
        self.chat_lable.config(font=("Arial",12))
        self.chat_lable.pack(padx=20,pady=5)

        self.text_area = tkinder.scrolledtext.scrolledtext(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disable')

        self.msg_lable = tkinter.lable(self.win,text="messsage:",bg=lightgray)
        self.msg_lable.config(font=("Arial",12))
        self.msg_lable.pack(padx=20,pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.button(self,win, text="send",command=self.write)
        self.send_button.config(font=("Arial",12))
        self.send_button.pack(padx=20,pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        self.win.mainloop()

        def write(self):
            message = f"{self.nickname}:{self.input_area.get('1.0','end')}"
            self.running.sock.send(message.encode('utf-8'))
            self.input_area.delete('1.0','end')

        def stop(self):
                self.runing = False
                self.win.destroy()
                self.sock.close()
                exit(0)

        def receive(self):
            while self.running:
                try:
                    message = self.sock.recv(1024) #change
                    if massage == 'NICK':
                        self.sock.send(self.nickname.encode('utf-8'))
                    else:
                            if self.gui_done:
                               self.text_area.config(state='normal')
                               self.text_area.insert('end',message)
                               self.text_area.yview('end')
                               self.text_area.config(state='disabled')
                            
                            except:
                                 (ConnectionAbortedError)

                            break
                except:
                    print("Error")
                    self,sock.close()
                    break
                    client = client(HOST,PORT)