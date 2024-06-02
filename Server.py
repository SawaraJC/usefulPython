'''import threading 
import socket
import time
host='127.0.0.1'
port=9090

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients=[]
usernames=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message=clients.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            user=usernames[index]


            broadcast(f'{user} left the chat'.encode('ascii'))
            usernames.remove(user)
           
            #broadcast(user, "left the chat".encode('utf-8'))
            break

def receive():
    while True:
        client,address=server.accept()
        print(f'Connected with {str(address)}')
        print("Connected with" ,address)

        client.send('USER1'.encode('ascii'))
        user=client.recv(1024).decode('ascii')
        usernames.append(user)
        clients.append(client)
        print(f'\nUsername of client is {user}')
        client.send("\nConnected to server !".encode('ascii'))
        broadcast(f'\n{user}has joined the chat !'.encode('ascii'))
        #print(f'\nUsername of client is {user}')
         # broadcast(user, "has joined the chat !".encode('utf-8'))
        
        
        #client.send("Connected to server !".encode('utf-8'))

        thread=threading.Thread(target=handle, args=(client,))
        thread.start()
print("Server is running !")

receive()'''