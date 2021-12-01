from http.server import SimpleHTTPRequestHandler

from requests import get


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        result = get('https://pokeapi.co/api/v2/pokemon/blastoise')
        if result.status_code != 200:
            raise Exception(result.text)

        abilities_details = result.json()['abilities']
        abilities_names = [i['ability']['name'] for i in abilities_details]

        ordered_abilities = sorted(abilities_names)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(str(ordered_abilities).encode())

        return
