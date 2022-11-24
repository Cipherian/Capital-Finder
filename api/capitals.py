from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_string = parse.urlsplit(s)
        query_list = parse.parse_qsl(url_string.query)
        dict_list = dict(query_list)
        message = None

        url = 'https://restcountries.com/v2/'

        if "country" in dict_list:
            r = requests.get(url + "name/" + dict_list["country"])
            data = r.json()
            data_country = data[0]["name"]
            data_capital = data[0]["capital"]
            message = f' The capital of {data_country} is {data_capital}.'

        if "capital" in dict_list:
            r = requests.get(url + "name/" + dict_list["capital"])
            data = r.json()
            data_country = data[0]["name"]
            data_capital = data[0]["capital"]
            message = f'  {data_capital} is the capital of {data_country}.'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(bytes(message.encode()))

        return



