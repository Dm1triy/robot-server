import socket

host = '192.168.88.24'

port = 6543  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")

