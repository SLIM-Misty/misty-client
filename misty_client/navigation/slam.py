from misty_client import base


class SLAM(base.Base):

    def __init__(self, ip):
        super(SLAM, self).__init__(ip)

    def start(self):
        url = "{}/slam/streaming/start".format(self.url_base)
        return self.client.post(url)

    def stop(self):
        url = "{}/slam/streaming/stop".format(self.url_base)
        return self.client.post(url)


def slam_stream(func):
    def stream(*args, **kwargs):
        # Assumption is made that only classes pertaining
        # to the REST API are being decorated
        slam = SLAM(args[0].ip)
        slam.start()
        func(*args, **kwargs)
        slam.stop()
    return stream
