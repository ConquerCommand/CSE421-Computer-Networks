import socket
import threading

HEADER = 16
PORT = 1828
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def service(connection, address):
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
                vowels = ["A", "E", "I", "O", "U",
                          "a", "e", "i", "o", "u"]
                count = 0
                for i in msg:
                    if i in vowels:
                        count += 1
                if count == 0:
                    connection.send("Not enough vowels".encode(FORMAT))
                elif count > 2:
                    connection.send("Too many vowels".encode(FORMAT))
                else:
                    connection.send("Enough vowels I guess".encode(FORMAT))

    connection.close()


def start():
    server.listen()
    print(f"Server is listening...")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=service, args=(connection, address))
        thread.start()
        print(f"Total clients connected {threading.active_count()-1}")


start()
