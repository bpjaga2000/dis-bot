import http.server as server
from json import loads

PORT = 3000
URL = "127.0.0.1"
i=0

class handler(server.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode("utf-8")
        print(loads(body))
        print("post"+str(++i))

httpd = server.HTTPServer((URL,PORT),handler)
httpd.serve_forever()
httpd.server_close()