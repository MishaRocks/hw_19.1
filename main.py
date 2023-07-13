import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_page(self):
        with open('templates/contacts.html', 'r', encoding='UTF-8') as file:
            content = file.read()
        return content

    def do_GET(self):
        content = self.__get_page()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")