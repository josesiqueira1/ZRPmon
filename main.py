from socketserver import TCPServer

from handler import Handler


def start_server():
    with TCPServer(("", 80), Handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    start_server()
