class Base(object):

    def __init__(self, ip):
        self.url_base = "http://{}/api".format(ip)
