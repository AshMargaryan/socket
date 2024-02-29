import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5100

# Connecting
name = input("Please enter your name:  \n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

start_message = f"\n{name} Connected\n".encode()
sock.send(start_message)


def receive_data():
    while True:
        data = sock.recv(5012)

        if len(data) < 1:
            break

        print(data.decode('utf-8'))


threading.Thread(target=receive_data).start()

while True:
    message = input("Enter The Message\n")
    sock.send(message.encode('utf-8'))
    if message == "quit":
        sock.close()
        break


