# make a simple webserver
import http.server
import socketserver

#make a handler class which returns every file/folder in the current directory except for this file
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

# make a server
PORT = 80
Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
