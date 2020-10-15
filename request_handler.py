from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from entries import get_all_entries 
from entriesTags import get_all_entriesTags
from tags import get_all_tags
from instructors import get_all_instructors
from moods import get_all_moods

HANDLERS = {
    "entries": {
        "get_all": get_all_entries,
        # "get_single": get_single_entry
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

    def do_GET(self):
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            (resourceName, id) = parsed
            handlerDict = HANDLERS[resourceName]
            if id is not None:
                response = f"{handlerDict['get_single']}"
            else:
                response = f"{handlerDict['get_all']()}"
        elif len(parsed) == 3:
            pass

        self.wfile.write(response.encode())        

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), JournalRequestHandler).serve_forever()
if __name__ == "__main__":
    main()    
