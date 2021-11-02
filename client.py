import socket
import pickle

score = 15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1236))
while True:

    s.connect(("127.0.0.1", 1235))
    msg = pickle.dumps(score)
    s.sendto(msg, ("127.0.0.1", 1235))
