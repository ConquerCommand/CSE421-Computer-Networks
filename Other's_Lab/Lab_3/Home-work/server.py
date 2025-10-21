import socket

HEADER = 16
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1828
DISCONNECT_MESSAGE = "End"
ADDRESS = (SERVER, PORT)

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
            hour = int(msg)
            salary = 0
            if hour <= 40:
                salary = hour * 200
                connection.send(str(salary).encode(FORMAT))
            elif hour > 40:
                extra = hour - 40
                salary = 8000 + extra * 300
                connection.send(str(salary).encode(FORMAT))

connection.close()
