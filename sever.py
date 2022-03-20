import socket
def solve(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            if c==0:
                return 0
            else:
                return f"x= {-c/b}"
    else:
        delta=b**2-4*a*c
        if delta<0:
            return "Phương trình vô nghiệm"
        elif delta==0:
            return f"x={-b/(2*a)}"
        else:
            return f"x1= {(-b+delta**0.5)/(2*a)}, x2= {(-b-delta**0.5)/(2*a)}"
HOST="127.0.0.1"
PORT=8080
BUFFER_SIZE=30
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
try:
    while True:
        data=conn.recv(BUFFER_SIZE).decode()
        a,b,c=data.split()
        a,b,c=int(a),int(b),int(c)
        conn.sendall(solve(a,b,c).encode())
except:
    pass


