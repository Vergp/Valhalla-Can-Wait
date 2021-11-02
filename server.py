import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1235)) #IP e PORTA
s.listen(5)

while True:
    s.connect(("127.0.0.1", 1236))
    print(f"Conexão com foi estabelecida!")
    msg = s.recv(16)
    d = pickle.loads(msg)
    print(d)

