import socket
import os
s=socket.socket()
print('SOCKET CREATED')
s.bind(('',9999))
s.listen(1)
print('WAITING FOR CONNECTIONS')
c,address=s.accept()
print("Connected with address : ",address)
while True:
    a=c.recv(1024).decode().strip()
    if(a.startswith('create')):
        loc=a[7:].strip()
        try:
            f=open(loc,"x")
            display='File Created'
        except:
            display='File Not Created'
        f.write("Iam ")
        f.close()
    elif(a.startswith('cat')):
        loc=a[4:].strip()
        try:
            f=open(loc,"r")
            display=f.read()
        except:
            display='File does not exist'
        f.close()
    elif(a.startswith('edit')):
        loc=a[5:].strip()
        try:
            f=open(loc,"a")
            msg=c.recv(1024).decode()
            f.write(msg)
            display='File is modified with :'+msg
        except:
            display='File does not exist'
        f.close()
    elif(a.startswith('delete')):
        loc=a[7:].strip()
        if os.path.exists(loc):
            os.remove(loc)
            display='File is deleted'
        else:
            display='File does not exist'
    elif(a.startswith('exit')):
        c.close()
        s.close()
        quit()
    else:
        display='PLEASE ENTER A VALID OPERATION'
    c.send(bytes(display,"utf-8"))
    print(display)
