import socket,sys
import winsound
import os

HeaderLength = 20

print(f'Howdy !!')
print(f'Make sure the sender and receiver are connected to same network...')

while True:

    choice = int(input('Enter 1 to receive the file\nEnter 2 to send the file\n'))
    if choice == 1:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        server.bind((IP_ADDRESS,808))
        print("ENTER THE FOLLOWING IP ADDRESS INTO THE SENDER'S CONSOLE:")
        print(IP_ADDRESS)
        while True:

            server.listen()
            s,arr = server.accept()
            header1 = s.recv(HeaderLength)
            if not len(header1):
                assert False
            mes_len = int(header1.decode("utf-8").strip())
            filename = s.recv(mes_len).decode("utf-8")
            f = open(filename,'wb+')

            header2 = s.recv(HeaderLength)
            if not len(header2):
                assert False
            mes_len = int(header2.decode("utf-8").strip())
            size = int(s.recv(mes_len).decode("utf-8"))
            # print('filename:',filename)
            print('size:',size,'bytes')
            k = 20

            while True:
                try:
                    x = s.recv(1024*k)
                    if x == '' or x == b'' or x == 'end':
                        break
                    f.write(x)
                    f.flush()
                    os.fsync(f.fileno())

                except:
                    f.close()
                    break

            winsound.MessageBeep()
            f.close()
            print('received file:',f.name)
            print()
    elif choice == 2:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP_ADDRESS = input("Enter the receiver's ip address displayed on the receiver's terminal:")
        s1.connect((IP_ADDRESS, 808))
        print('connected...')
        while True:
            filename = input(
                "Enter the file to be transferred along with the path (or simply drag the file here in the console):")
            if filename[0] == '"':
                filename = filename[1:-1]
            f1 = open(filename, 'rb')
            name = os.path.basename(f1.name)
            size = os.stat(f1.name).st_size
            header1 = f"{len(name):<{HeaderLength}}".encode('utf-8') + name.encode('utf-8')
            header2 = f"{len(str(size)):<{HeaderLength}}".encode('utf-8') + str(size).encode('utf-8')
            s1.send(header1)
            s1.send(header2)
            while True:
                try:
                    x = f1.read(1024 * 20)
                    if x == b'':
                        s1.send('end')
                    s1.send(x)
                except:
                    f1.close()
                    break
            s1.close()
            print('sent:',f1.name)

    else:
        winsound.MessageBeep()
        print('Enter valid choice idiot!!')
