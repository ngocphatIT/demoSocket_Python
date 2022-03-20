import socket
BUFFER_SIZE=30
HOST='127.0.0.1'
PORT=8080
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST,PORT))
a=int(input("Nhập hệ số a: "))
b=int(input("Nhập hệ số b: "))
c=int(input("Nhập hệ số c: "))
conn.sendall(f'{a} {b} {c}'.encode())
while True:
    data=conn.recv(BUFFER_SIZE).decode()
    print(data)
    
    
    
