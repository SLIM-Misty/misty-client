import requests

class Client(object):

    def __init__(self, ip):
        self.api_base = "http://{}/api/".format(ip)

    def get(self, url, params={}, **kwargs):
        url = "{}{}".format(self.api_base, url)
        return request.get(url, params=params)

    def post(self, url, payload, params={}, **kwargs):
        url = "{}{}".format(self.api_base, url)
        return request.post(url, params=params, data=payload)

    def put(self, url, payload, params={}, **kwargs):
        url = "{}{}".format(self.api_base, url)
        return request.put(url, params=params, data=payload)

    def delete(self, url, params={}, **kwargs):
        url = "{}{}".format(self.api_base, url)
        return request.delete(url, params=params)

class Base(object):

    def __init__(self, ip):
        self.client = Client(ip)
