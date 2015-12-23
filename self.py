import SimpleHTTPServer
import SocketServer
import socket
list_server = []
# untuk di pasang pada server sebagai load balancer untuk yang tier ke dua....
for i in range(5):
	list_server.append(socket.gethostbyname(socket.gethostname()))
	list_server.append('%d'%(9010+i))

idx = 0
	
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		#print self.path
		global idx
		self.send_response(303)
		new_path = 'http://%s:%s' % (list_server[idx],list_server[idx+1])
		idx = idx+2
		
		if idx >= len(list_server):
			idx=0
		
		
		self.send_header('Location', new_path)
		self.end_headers()

PORT = 9009
SocketServer.TCPServer.allow_reuse_address = True
SocketServer.TCPServer.request_queue_size = 100000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port %d" % (PORT)
handler.serve_forever()