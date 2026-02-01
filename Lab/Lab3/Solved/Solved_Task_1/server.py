import socket

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

while True:
    conn,addr = server.accept()
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
                print(msg)
                conn.send("message received".encode(format))
    conn.close()