import requests
import json

from misty_client import base
from misty_client.navigation.slam import slam_stream


class Picture(base.Base):
    """Contains various functions to take pictures with each camera type."""

    def __init__(self, ip):
        """Initializes the picture class with the IP of Misty.

        Args:
          ip (str): IP address of the Misty robot.
        """
        super(Picture, self).__init__(ip)

    def take(self, filename, width=300, height=200, onscreen=True, overwrite=True):
        """Takes a picture with the RGB camera.

        Args:
          filename (str): Name of the file where the image will be saved.
          width (int): Width of image in pixels.
          height (int): Height of image in pixels.
          onscreen (boolean): If true and filename is provided then show on misty.
          overwrite (boolean): Whether to overwrite a file with the same name.

        Returns:
          object: An object containing image data and meta information.
        """

        url = "{}/cameras/rgb".format(self.url_base) 
        params = {
            "Base64": "true", 
            "FileName": filename,
            "Width": width,
            "Height": height,
            "DisplayOnScreen": onscreen,
            "OverwriteExisting": overwrite
        }

        return self.client.get(url, params=params)

    @slam_stream
    def take_depth(self, *args, **kwargs):
        """Takes a picture with the depth camera.

        Note that the width and height cannot be set. It seems to be hardcoded
        on the backend to be 240 height and 320 width. As Misty moves fruther
        away from a scene being viewed, each pixel value will represent a larger
        surface area. The reverse is true when moving closer.

        For example, being 2 meters away from a flat wall will result in most of the
        values being around 2000.

        Returns:
          object: An object containing depth information about the image matrix.
            This includes height, width, and an array of size height*width.
            Each value is the distance in millimeters from the sensor for each
            pixel in the captured image.
        """

        url = "{}/cameras/depth".format(self.url_base)
        return self.client.get(url)

    @slam_stream
    def take_fisheye(self, *args, **kwargs):
        """Takes a picture with the fisheye camera.

        Returns:
          object: An object containing image data and meta information.
        """

        params = {
            "Base64": "true", 
        }
 
        url = "{}/cameras/fisheye".format(self.url_base)
        return self.client.get(url, params=params)


class Video(object):
    pass


class FaceDetection(base.Base):
    pass


class ObjectDetection(object):
    pass
