import socket



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#host = 'ip ardes'
host = socket.gethostname()
port = 444
serversocket.bind((host, port)) # bind port and host to the server
serversocket.listen(3) # listen for connections

print ('Server is listening for connections')
while True:
    clientsocket, address = serversocket.accept()
    print ('Got a connection from %s' % str(address))         #print('Received connection from ' + str(address))       
    message = 'Thank you for connecting' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
    
    # data = clientsocket.recv(1024)
    # print ("Received data:", data)
    # clientsocket.send(data)
    # clientsocket.close()