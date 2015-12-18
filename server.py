import socket,time,datetime,sys	
import os
queue_data=1001;

sys.stdout.write('Port : ')
port = raw_input()
port = int(port)
server_addr = ('localhost',port)
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
		#test="<!DOCTYPE HTML><html><h1>sukses gan</h1></html>"
		#data="HTTP/1.1 200 OK \n\n%s"%test
		request = client_con.recv(1024)	
		request_data=request.split()
		
		if len(request_data) > 1:
			temp=request_data[1]
		else:
			temp="/"
			
		temp1=temp[1:]
		datahandler = temp1.split("?")
		datarecognation=""
		if len(datahandler)>1 :
			datacapturing = datahandler[1]
			datarecognation = datacapturing.split("&");
		
		
		if temp=="/" :
			try :
				data_send="HTTP/1.1 200 OK \r\n\r\n%s"%index
				client_con.sendall(data_send)
			except :
				err="HTTP/1.1 404 Not Found\r\n\r\n <h1>NOT FOUND</h1>"
				client_con.sendall(err)
		else :
			try :
				f=open(datahandler[0],"r+")
				ambil_data=f.read()
				f.close()
				if ambil_data :
					datasimpan = ""
					for i in range(len(datarecognation)):
						datasimpan=datasimpan+datarecognation[i]+"\n"
					data_send="HTTP/1.1 200 OK \r\n\r\n%s"%datasimpan+ambil_data
					client_con.sendall(data_send)
			except :
				err="HTTP/1.1 404 Not Found\r\n\r\n <h1>NOT FOUND</h1>"
				client_con.sendall(err)
		"""try :
			#print len(datarecognation)
			f=open(datahandler[0]+".jpeg","r+")
			ambil_data=f.read()
			f.close()
			if ambil_data :
				data_send="HTTP/1.1 200 OK \r\n\r\n%s"%ambil_data
				client_con.sendall(data_send)
			
		except :
				err="HTTP/1.1 404 Not Found\r\n\r\n <h1>404<br>NOT FOUND</h1>"
					client_con.sendall(err)"""
		client_con.close()
except KeyboardInterrupt:
	print 'Server Disconnect'
	exit(0)
		


