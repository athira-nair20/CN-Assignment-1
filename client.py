import socket
c=socket.socket()
address=input("Enter IP Address : ")
c.connect((address,9999))
print("\n Select the operation - ")
print("\n 1.create a file using suffix create \n 2.Read the file using suffix cat \n 3.Modify the file using suffix edit \n 4.Delete the file using suffix delete\n 5.exit \n")
while True:
	ch=input("Enter the required operation: ")
	c.send(bytes(ch,"utf-8"))
	if(ch.startswith("edit")):
		msg=input("Enter the string to be added: ")
		c.send(bytes(msg,"utf-8"))
	elif(ch=='exit'):
		quit()
		c.close()
	output=c.recv(1024).decode()
	print(output)
