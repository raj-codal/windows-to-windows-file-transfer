import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDRESS = input("Enter the reciever's ip address")
s.connect((IP_ADDRESS, 808))
filename = input("Enter the file to be transferred along with the path (or simply drag the file here in the console):")
f=open(filename,'rb')
while True:
    try:
        x = f.read(1024*20)
        if x==b'':
            s.send('end')
        s.send(x)
    except:
        f.close()
        break
s.close()
