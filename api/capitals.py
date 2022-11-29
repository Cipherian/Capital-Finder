from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string = parse.parse_qsl(url_components.query)
        dic = dict(query_string)

        message = None

        try:
            if "country" in dic:
                url = 'https://restcountries.com/v3/name/"'
                r = requests.get(url + dic["country"])
                data = r.json()
                data_capital = data[0]["capital"]
                data_country = data[0]["name"]
                message = f'The capital of {data_country} is {data_capital}'

            if "capital" in dic:
                url = 'https://restcountries.com/v3/name/"'
                r = requests.get(url + "capital/" + dic["capital"])
                data = r.json()
                data_capital = data[0]["capital"]
                data_country = data[0]["name"]
                message = f' {data_capital} is the capital of {data_country}'

        except:
            message = "Error, this is API is not currently working, or you have entered an invalid endpoint."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return


