import socket
sock = socket.socket()
sock.bind(('', 5050))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1060)
    if not data:
        break
    conn.send(data.upper())

conn.close()
