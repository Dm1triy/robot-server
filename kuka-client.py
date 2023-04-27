import socket
import time


class Client:
    def __init__(self, host='192.168.88.24', port=6543):
        self.host = host
        self.port = port
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))
        print("(Client)\n    Connected to the server!")

        self.interaction()

    def __del__(self):
        self.client_socket.close()
        print("(Client)\n    Connection lost")

    def interaction(self):
        while True:
            self.client_socket.sendall(b"Give me acceleration")
            data = self.client_socket.recv(1024).decode()
            print(f"(Client)\n    Time{time.time()}. Received {data!r}")


if __name__ == "__main__":
    pk = Client()