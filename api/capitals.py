from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        try:

            if "country" in dic:
                url = "https://restcountries.com/v3/name/"
                r = requests.get(url + dic["country"])
                data = r.json()
                capital = str(data[0]['capital'])[1:-1]
                message = f'The capital of {dic["country"]} is {capital}.'

            if "capital" in dic:
                url = "https://restcountries.com/v3/capital/"
                r = requests.get(url + dic["capital"])
                data = r.json()
                country = data[0]['name']['common']
                message = f'{dic["capital"]} is the capital of {country}.'

        except:
            message = "The capital or country you entered in is invalid"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return