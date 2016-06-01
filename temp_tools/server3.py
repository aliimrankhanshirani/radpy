import BaseHTTPServer
import CGIHTTPServer
from CGIHTTPServer import _url_collapse_path

class MyCGIHTTPServer(CGIHTTPServer.CGIHTTPRequestHandler):  
  def is_cgi(self):
    collapsed_path = _url_collapse_path(self.path)
    for path in self.cgi_directories:
        if path in collapsed_path:
            dir_sep_index = collapsed_path.rfind(path) + len(path)
            head, tail = collapsed_path[:dir_sep_index], collapsed_path[dir_sep_index + 1:]
            self.cgi_info = head, tail
            return True
    return False

server = BaseHTTPServer.HTTPServer
handler = MyCGIHTTPServer

server_address = ("", 8000)
handler.cgi_directories = [""]

httpd = server(server_address, handler)
httpd.serve_forever()
