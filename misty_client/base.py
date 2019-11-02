import requests


class Client(object):

    def get(self, url, params={}, **kwargs):
        return requests.get(url, params=params)

    def post(self, url, payload, params={}, **kwargs):
        return requests.post(url, params=params, json=payload)

    def put(self, url, payload, params={}, **kwargs):
        return requests.put(url, params=params, json=payload)

    def delete(self, url, params={}, **kwargs):
        return requests.delete(url, params=params)


class Base(object):

    def __init__(self, ip):
        self.url_base = "http://{}/api".format(ip)
        self.client = Client()
