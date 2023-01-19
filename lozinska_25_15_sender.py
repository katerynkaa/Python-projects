import socket

HOST = 'localhost'
PORT = 1401


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
inp = s.makefile('rb', 0)
out = s.makefile('wb', 0)

while True:
    data = inp.readline()
    if not data: break
    print(str(data, encoding='utf-8'))

    to_send = input('answer: ')
    out.write(bytes(to_send, encoding='utf-8') + b'\n')


