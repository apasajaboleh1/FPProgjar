import SimpleHTTPServer
import SocketServer
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		print self.path
		self.send_response(303)
		new_path = 'http://localhost:8855'
		print new_path
		self.send_header('Location', new_path)
		self.end_headers()

PORT = 8009
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port %d" % (PORT)
handler.serve_forever()