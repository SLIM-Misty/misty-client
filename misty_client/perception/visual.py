import requests
import json

from misty_client import base


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

    def take_depth(self):
        # Need to import slam sensor and start it
        url = "{}/cameras/depth".format(self.url_base)
        request.get(url)

    def take_fisheye(self):
        # Need to import slam sensor and start it
        url = "{}/cameras/fisheye".format(self.url_base)


class Video(object):
    pass


class FaceDetection(object):
    pass


class ObjectDetection(object):
    pass
