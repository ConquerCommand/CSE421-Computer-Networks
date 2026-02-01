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
                try:
                    hours = float(msg)
                    if hours <= 40:
                        salary = hours*200
                    else:
                        salary = 8000+(hours-40)*300
                    conn.send(f"Salary: Tk {salary:.2f}".encode(format))
                except ValueError:
                    conn.send(b"ERROR: invalid input")
    conn.close()

while True:
    conn,addr = server.accept()
    thread=threading.Thread(target=handel_client, args=(conn,addr))
    thread.start()