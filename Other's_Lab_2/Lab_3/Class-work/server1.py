import socket

HEADER = 16
PORT = 1828
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print(f"Server is listening... ")
connection, address = server.accept()
connected = True

while connected:
    msg_length = connection.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = connection.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            connection.send("Terminated".encode(FORMAT))
        else:
            connection.send("Message received".encode(FORMAT))
            print(msg)

connection.close()


