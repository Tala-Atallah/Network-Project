from socket import *
serverPort = 9966 #server port number
serverSocket = socket(AF_INET,SOCK_STREAM)#create TCP socket with port 9966
serverSocket.bind(("",serverPort))
serverSocket.listen(1)#server begins listening for incoming TCP requests
print("The server is ready to receive")

while True:
    #server waits on accept() for incoming requests
    connectionSocket, addr = serverSocket.accept()
    #read bytes from socket
    sentence = connectionSocket.recv(1024).decode()

    print(addr)
    print(sentence)

    ip = addr[0]
    port = addr[1]
     #get the request fom the client
    if sentence.startswith("GET /") and (" HTTP/1.1" in sentence or " HTTP/1.0" in sentence):

        path = sentence.split(" ")[1]
        print(path)
    #check the type of request to send the file with Content type and http response
    if (path == '/' or path == '/index.html' or path == '/main_en.html' or path == '/en'):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("main_en.html", "rb")
         connectionSocket.send(file.read())

    elif (path == '/ar'):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("main_ar.html", "rb")
         connectionSocket.send(file.read())

    elif (path.endswith('.html')):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("page.html", "rb")
         connectionSocket.send(file.read())

    elif (path.endswith('.css')):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: text/css \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("main_en.css", "rb")
         connectionSocket.send(file.read())


    elif (path.endswith('.png')):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: image/png \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("img2.png", "rb")
         connectionSocket.send(file.read())

    elif (path.endswith('.jpg')):
         connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
         connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("img1.jpg", "rb")
         connectionSocket.send(file.read())

    elif(path == '/cr'):
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://www.cornell.edu \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif(path == '/so'):
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (path == '/rt'):
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://ritaj.birzeit.edu \r\n".encode())
        connectionSocket.send("\r\n".encode())

    else:
         connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         file = open("error.html", "rb")
         connectionSocket.send(file.read())
         connectionSocket.close()
    connectionSocket.close()#close connection to this client