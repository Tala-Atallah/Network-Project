from socket import *
import time
import ctypes
serverPort = 9955 #server port number
serverSocket = socket(AF_INET,SOCK_STREAM)#create TCP socket with port 9955
serverSocket.bind(("localhost",serverPort)) #associate the socket with a local network by specifying the IP address and the port number
serverSocket.listen(1)
print("The server is listening on port 9955")
connectionSocket, addr = serverSocket.accept() # waits until a client connects and start sending request
message = connectionSocket.recv(1024).decode() #recieves data up to 1024 bytes and converts bytes to string
print("the message ->",message)
if message == "1200219" or message == "1202575":  #checks if the message is equal to our group members ID
    print("The OS will lock the screen after 10 seconds")
    connectionSocket.sendall(b"Server will lock screen after 10 seconds") #send the message to the client side through the connectionSocket established
    time.sleep(10)
    ctypes.windll.user32.LockWorkStation() # call the function that is responsible to lock the screen on windows
    print("Locking the screen now")
else :
    print("Invalid student ID")
    connectionSocket.sendall(b"Error, the student ID is invalid") #send the message to the client side



