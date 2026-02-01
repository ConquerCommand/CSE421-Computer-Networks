import socket
import threading

header = 64
format = 'utf-8'
disconnect_msg = 'End'

SERVER = socket.gethostbyname(socket.gethostname())
PORT=6666
ADDR=(SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
print('server is starting....... ')
server.listen()
print('server is listening on ',SERVER)

def handel_client(conn,addr):
    print('connected to ', addr)
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == disconnect_msg:
                connected = False
                conn.send(f"terminating the connection with {addr}".encode(format))
            else:
                vowels = "AEIOUaeiou"
                count=0
                for i in msg:
                    if i in vowels :
                        count+=1
                if count == 0:
                    conn.send("Not enough vowels".encode(format))
                elif count <= 2:
                    conn.send("Enough vowels I guess".encode(format))
                else:
                    conn.send("Too many vowels".encode(format))
    conn.close()

while True:
    conn,addr = server.accept()
    thread=threading.Thread(target=handel_client, args=(conn,addr))
    thread.start()