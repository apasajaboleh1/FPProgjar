import SimpleHTTPServer
import SocketServer
import socket
list_server = []

'''
for i in range(2):
	list_server.append('10.151.34.120')
	list_server.append('9009')

for i in range(2):
	list_server.append('10.151.34.104')
	list_server.append('9009')
	
for i in range(6):
	list_server.append('10.151.34.147')
	list_server.append('9009')

for i in range(4):
	list_server.append('10.151.34.105')
	list_server.append('9009')
'''
for i in range(5):
	list_server.append(socket.gethostbyname(socket.gethostname()))
	#list_server.append('localhost')
	list_server.append('%d'%(9010+i))

idx = 0
	
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		#print self.path
		global idx
		self.send_response(303)
		print 'fuk yu', idx
		new_path = 'http://%s:%s' % (list_server[idx],list_server[idx+1])
		idx = idx+2
		
		if idx >= len(list_server):
			idx=0
		
		#print 'fuk yu',new_path
		self.send_header('Location', new_path)
		self.end_headers()

PORT = 9009
SocketServer.TCPServer.allow_reuse_address = True
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port %d" % (PORT)
handler.serve_forever()