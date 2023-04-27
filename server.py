import socket
from accel_listener import Accel
import threading as thr


class Server:
    def __init__(self, host='192.168.88.24', port=6543):
        self.accel_stream = Accel()
        self.host = host
        self.port = port
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print('Port opened')

        self.server_is_running = True

        conn, address = self.server_socket.accept()
        self.conn = conn
        self.conn_addres = address
        print("Connection from: " + str(address))

    def __del__(self):
        self.conn.close()

    def interaction(self):
        while self.server_is_running:
            data = self.conn.recv(1024).decode()
            if data == "Give me acceleration":
                self.send_data()
                continue
            if data == "Kill":
                self.server_is_running = False

    def send_data(self):
        data = self.accel_stream.get_data()
        while not data:
            data = self.accel_stream.get_data()
        self.conn.sendall(data)



# with socket.socket() as s:
#     s.bind((host, port))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)

