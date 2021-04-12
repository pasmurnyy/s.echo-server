import socket

sock = socket.socket()
sock.connect(('Local host', 5050))
sock.send('hi, i`m Tom!')

data = sock.recv(1060)
sock.close()

print(data)
