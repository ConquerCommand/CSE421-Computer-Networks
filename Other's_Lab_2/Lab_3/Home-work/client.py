import socket

HEADER = 16
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1828
DISCONNECT_MESSAGE = "End"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    msg = input("Total Working Hours: ")
    if msg == DISCONNECT_MESSAGE:
        send(msg)
        break
    else:
        send(msg)
