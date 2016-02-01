 
import socket
import sys
 

# create an INET, STREAMing socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
mysock.connect(("www.pythonlearn.com", 80))
 # create an INET, STREAMing socket
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')


while True:
    data = mysock.recv(512)
    if ( len(data) < 1):
    	break
    print data
mysock.close()