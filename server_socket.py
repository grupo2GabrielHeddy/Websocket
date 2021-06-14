import socket
import threading

HEADER = 64
PORT   = 3074
SERVER = '127.0.0.1'
ADDR   = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
MAC_EXAMPLE        = '00:1B:44:11:3A:B7'
CHECK_MAC = True
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            allowed = handshake(conn,msg)
            if (msg == DISCONNECT_MESSAGE):
                connected = False
                conn.send("[SERVER] Disconnected".encode(FORMAT))
                print('[SERVER] User Disconnected')
            elif allowed:
                connected = False
                conn.send('[SERVER] MAC is not registered in our servers'.encode(FORMAT))
                print('[SERVER] User Disconnected')
                conn.send("Disconnected".encode(FORMAT))
                print('[SERVER] User Disconnected')
            if connected
                print(f"[{addr}] {msg}")
                conn.send("Message received".encode(FORMAT))

    conn.close()

def handshake(conn,message):
	global CHECK_MAC
	if CHECK_MAC:
		print("[SERVER] CHECKING MAC "+ message)
		if message == MAC_EXAMPLE:
			conn.send("Access Permitted: Welcome [{addr}]".encode(FORMAT))
			print('[ACCESS PERMITTED]')
			CHECK_MAC=False
			return False
		else:
			conn.send("Access Denied: You are not allowed to connect. Get out of here".encode(FORMAT))
			print('[ACCESS DENIED]')
			return True

def start():
    server.listen()
    print(f"[LISTEN] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is running.....")
start()

