import socket

header = 64
format = 'utf-8'
disconnect_msg = 'End'

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 6666
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(format)
  msg_length = len(msg)
  send_length = str(msg_length).encode(format)
  send_length +=b" "*(header-len(send_length))
  client.send(send_length)
  client.send(message)
  print(client.recv(2048).decode(format))

msg = f"The hostname of client is {socket.gethostname()} and the IP is {SERVER}"


while True:
  prompt = input("Hours the person worked: ")
  send(prompt)
  if prompt == disconnect_msg:
    break