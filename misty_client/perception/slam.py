from misty_client import base

class SLAM(base.Base):

    def __init__(self, ip):
        super(SLAM, self).__init__(ip)

    def start(self):
        url = "{}/slam/streaming/start".format(self.url_base)
        result = request.post(url)
        return result

    def stop(self):
        url = "{}/slam/streaming/stop".format(self.url_base)
        result = request.post(url)
        return result
