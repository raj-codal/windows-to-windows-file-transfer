import socket,sys
import winsound

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
server.bind((IP_ADDRESS,808))

print("ENTER THE FOLLOWING IP ADDRESS INTO THE SENDER'S CONSOLE:")
print(IP_ADDRESS)

server.listen()

s,arr = server.accept()

f = open(input('Enter file name along with the path:'),'wb+')

k = 20

while True:
    try:
        x = s.recv(1024*k)
        if x == '' or x == b'' or x == 'end':
            break
        f.write(x)
    except:
        f.close()
        break

winsound.Beep(2000,500)
winsound.Beep(2000,500)
winsound.Beep(2000,500)
f.close()
sys.exit()
