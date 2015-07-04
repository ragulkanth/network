import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))

while True:
    msg = raw_input("Message to server: ")
    s.send(msg)
    if msg.lower() == "bye":
        break
    msg_received = s.recv(1024)
    print "Server: ", msg_received
    if msg_received.lower() == "bye":
	      break

s.close()
