from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from entries import get_all_entries, get_single_entry, save_entry, delete_entry
from entriesTags import get_all_entriesTags
from tags import get_all_tags
from instructors import get_all_instructors
from moods import get_all_moods

HANDLERS = {
    "entries": {
        "get_all": get_all_entries,
        "get_single": get_single_entry,
        "delete": delete_entry,
        "create": save_entry
    },
    "entriesTags": {
        "get_all": get_all_entriesTags,
        # "get_single": get_single_entryTag
    },
    "tags": {
        "get_all": get_all_tags,
        # "get_single": get_single_tag
    },
    "instructors": {
        "get_all": get_all_instructors,
        # "get_single": get_single_instructor
    },
    "moods": {
        "get_all": get_all_moods,
        # "get_single": get_single_mood
    }
    
}

class JournalRequestHandler(BaseHTTPRequestHandler):
    def parse_url(self, path):
        params = path.split("/")
        resourceString = params[1]
        if "?" in resourceString:
            resource, param = resourceString.split("?")
            key, value = param.split("=")
            value = urllib.parse.unquote(value)
            return (resource, key, value)

        else:
            id = None
            try:
                id = int(params[2])
            except IndexError:
                pass
            except ValueError:
                pass
            return (resourceString, id)

    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()

    def do_GET(self):
        response = {}
        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            (resourceName, id) = parsed
            handlerDict = HANDLERS[resourceName]
            if id is not None:
                response = f"{handlerDict['get_single'](id)}"
                if response == 'Item not found':
                    self._set_headers(404)
                else:
                    self._set_headers(200)
            else:
                response = f"{handlerDict['get_all']()}"
        elif len(parsed) == 3:
            pass

        self.wfile.write(response.encode())

    def do_DELETE(self):
        (resource, id) = self.parse_url(self.path)
        success = HANDLERS[resource]["delete"](id)
        if success:
            self._set_headers(204)
        else: 
            self._set_headers(404)
        self.wfile.write("".encode())

    def do_POST(self):
        self._set_headers(201)
        length =  int(self.headers.get('content-length', 0))
        content = self.rfile.read(length)
        content = json.loads(content)
        (resource, id) = self.parse_url(self.path)
        resource_creation_handler = HANDLERS[resource]["create"]
        new_resource = resource_creation_handler(content)
        self.wfile.write(f"{new_resource}".encode())  

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), JournalRequestHandler).serve_forever()
if __name__ == "__main__":
    main()    
