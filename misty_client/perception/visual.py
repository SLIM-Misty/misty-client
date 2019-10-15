import requests
import json

from misty_client import base
from mist_client.perception.slam import slam_stream

class Picture(base.Base):

    def __init__(self, ip):
        super(Picture, self).__init__(ip)

    def take(self, filename, width=300, height=200, base64=True, onscreen=True, overwrite=True):
        url = "{}/cameras/rgb".format(self.url_base) 
        payload = {
            "Base64": base64, 
            "FileName": filename,
            "Width": width,
            "Height": height,
            "DisplayOnScreen": onscreen,
            "OverwriteExisting": overwrite
        }
        request.post(url, json=payload)

    @slam_stream
    def take_depth(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        url = "{}/cameras/depth".format(self.url_base)
        return request.get(url)

    @slam_stream
    def take_fisheye(self, *args, **kwargs):
        url = "{}/cameras/fisheye".format(self.url_base)
        return request.get(url)

class Video(object):
    pass


class FaceDetection(object):
    pass


class ObjectDetection(object):
    pass
