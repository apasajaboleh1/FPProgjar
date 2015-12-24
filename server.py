import socket,time,datetime,sys	
import os
queue_data=50000;
addr=socket.gethostbyname(socket.gethostname())
#sys.stdout.write('Port : ')
#port = raw_input()
port = int(sys.argv[1])
server_addr = (addr,port)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_addr)
sock.listen(queue_data)
print 'serve at %s port %s'%server_addr

f = open("cloud.jpg","rb")
index = f.read()
f.close()

try:
	while True:
		client_con,client_addr=sock.accept()
		request = client_con.recv(1024)	
		request_data=request.split()
		
		if len(request_data) > 1:
			temp=request_data[1]
		else:
			temp="/"
			
		try :
			data_send="HTTP/1.1 200 OK \r\n\r\n%s"%index
			client_con.sendall(data_send)
		except :
			err="HTTP/1.1 404 Not Found\r\n\r\n <h1>NOT FOUND</h1>"
			client_con.sendall(err)
		client_con.close()
except KeyboardInterrupt:
	print 'Server Disconnect'
	exit(0)
		


