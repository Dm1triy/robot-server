import socket
import time


class Client:
    def __init__(self, host='192.168.88.21', port=6543):
        self.host = host
        self.port = port
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))
        print("(Client)\n    Connected to the server!")

        self.interaction()

    def __del__(self):
        self.client_socket.sendall(b"Stop")
        self.client_socket.close()
        print("(Client)\n    Connection lost")

    def interaction(self):
        while True:
            self.client_socket.sendall(b"Give me acceleration")
            data = self.client_socket.recv(1024).decode()
            receiving_time = time.time()
            print(f"(Client)\n    Receiving Time: {receiving_time}")
            processed_data = list(map(float, data.split(", ")))
            print(f"    Processed data: X:{processed_data[0]}, Y:{processed_data[1]}, Z:{processed_data[2]}\n"
                  f"    Getting time: {processed_data[4]}, Delay: {receiving_time - processed_data[4]}")


if __name__ == "__main__":
    pk = Client()
