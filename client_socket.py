import socket

HEADER             = 64
PORT               = 3074
SERVER             = '158.251.91.68'
ADDR               = (SERVER, PORT)
FORMAT             = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
#MAC_EXAMPLE = '1A:2B:3C:4D:5E:6D'	
MAC_EXAMPLE = '00:1B:44:11:3A:B7'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(MAC_EXAMPLE)
send('grupo 2')
send('el servidor funciona correctamente')
send(DISCONNECT_MESSAGE)

