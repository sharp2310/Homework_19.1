from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        name, email = query_components.get('name'), query_components.get('email')
        print(name, email)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")