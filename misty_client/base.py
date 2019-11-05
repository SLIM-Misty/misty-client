import requests


class Client(object):

    def get(self, url, params={}, **kwargs):
        return requests.get(url, params=params)

    def post(self, url, payload={}, params={}, **kwargs):
        if payload:
            return requests.post(url, params=params, json=payload)
        return requests.post(url, params=params)

    def put(self, url, payload={}, params={}, **kwargs):
        if payload:
            return requests.put(url, params=params, json=payload)
        return requests.put(url, params=params)

    def delete(self, url, params={}, **kwargs):
        return requests.delete(url, params=params)


class Base(object):

    def __init__(self, ip):
        self.ip = ip
        self.url_base = "http://{}/api".format(self.ip)
        self.client = Client()
