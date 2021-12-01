from handler import Handler
from socketserver import TCPServer

with TCPServer(("", 80), Handler) as httpd:
    httpd.serve_forever()
