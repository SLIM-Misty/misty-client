from misty_client import base


class SLAM(base.Base):

    def __init__(self, ip):
        super(SLAM, self).__init__(ip)

    def start(self):
        url = "{}/slam/streaming/start".format(self.url_base)
        return request.post(url)

    def stop(self):
        url = "{}/slam/streaming/stop".format(self.url_base)
        return request.post(url)


def slam_stream(func):
    def stream(*args, **kwargs):
        slam = SLAM(kwargs["ip"])
        slam.start()
        if kwargs:
            func(*args, **kwargs)
        else:
            func(*args)
        slam.stop()
    return stream
