from socket import *
serverPort = 9955 #server port number
clientSocket = socket(AF_INET,SOCK_STREAM)#create TCP socket with port 9955
clientSocket.connect(("localhost", serverPort)) #associate the socket with a local network by specifying the IP address and the port number
student_id = input("enter student id:") # ask the user to enter an ID
clientSocket.sendall(student_id.encode('utf-8')) #sends the student ID to the server through the clientSocket established

