import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(10)

clients = set()
clients_lock = threading.Lock()

def receive_send(client_socket, address):
    print(f"Message From {address}")
    while True:
        with clients_lock:
            clients.add(client_socket)
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                else:
                    with clients_lock:
                        for c in clients:
                            c.sendall(str(address[0]).encode('utf-8') + "---".encode('utf-8') + data)
        finally:
            with clients_lock:
                clients.remove(client_socket)
                client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    print(client_socket)
    print("END")
    print(address)

    threading.Thread(target=receive_send, args=(client_socket, address)).start()
