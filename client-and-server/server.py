import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)


while True:

    try:
    	print "Waiting for connections..."
    	c, addr = s.accept()
    	print "Connected: ", addr


    	while True:
    	    msg_received = c.recv(1024)
    	    print "Client: ", msg_received
    	    if msg_received.lower() == 'bye':
	        print "%r got disconnected" % addr[0]
                break
    	    else:
                msg = raw_input("Message to client: ")
                c.send(msg)
                if msg.lower() == "bye":
	            break
        c.close()
    except KeyboardInterrupt:
	print "Qutting..."
	exit()
