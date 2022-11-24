from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string = parse.parse_qwl(url_components.query)
        dic = dict(query_string)
        url = 'https://restcountries.com/v3.1/'
        message = "Error, this is API is not currently working, or you have entered an invalid endpoint."

        if "country" in dic:
            r = requests.get(url + "name/" + dic["country"])
            data = r.json()
            data_capital = data[0]["capital"]
            data_country = data[0]["name"]
            message = f'The capital of {data_country} is {data_capital}'

        if "capital" in dic:
            r = requests.get(url + "capital/" + dic["capital"])
            data = r.json()
            data_capital = data[0]["capital"]
            data_country = data[0]["name"]
            message = f' {data_capital} is the capital of {data_country}'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return


