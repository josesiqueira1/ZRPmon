from http.server import SimpleHTTPRequestHandler
from re import search

from requests import get


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        param = search('/pokemon/[a-zA-Z]+', self.path)
        if not param:
            return self.handle_error(b'Parametros invalidos \nUtilizacao: /pokemon/{nome}', 500)

        result = get('https://pokeapi.co/api/v2' + param.group(0))

        if result.status_code == 404:
            return self.handle_error(b'Pokemon nao encontrado', result.status_code)
        elif result.status_code != 200:
            return self.handle_error(b'Erro ao buscar dados do pokemon', result.status_code)

        abilities_details = result.json()['abilities']
        abilities_names = [i['ability']['name'] for i in abilities_details]

        ordered_abilities = sorted(abilities_names)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(str(ordered_abilities).encode())

        return

    def handle_error(self, mensagem: bytes, status: int):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(mensagem)
