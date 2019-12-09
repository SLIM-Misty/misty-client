from misty_client import base


class SLAM(base.Base):
    """Collection of functions used to interact with SLAM endpoints"""

    def __init__(self, ip):
        """Initializes the SLAM class with the IP of Misty.

        Args:
          ip (str): IP address of the Misty robot.
        """
        super(SLAM, self).__init__(ip)

    def start(self):
        """Starts the SLAM stream.

        Opens the data stream from the Occipital Structure Core depth
        sensor to obtain image and depth data.

        Must be done before using depth camera. 

        Returns:
          bool: Returns true if there are no errors related to this command.
        """
        url = "{}/slam/streaming/start".format(self.url_base)
        return self.client.post(url)

    def stop(self):
        """Stops the SLAM stream.

        This command turns off the laser in the depth sensor and lowers
        Misty's power consumption.

        Must always be called after using start.

        Returns:
          bool: Returns true if there are no errors related to this command.
        """
        url = "{}/slam/streaming/stop".format(self.url_base)
        return self.client.post(url)

    def start_mapping(self):
        url = "{}/slam/map/start".format(self.url_base)
        return self.client.post(url)

    def stop_mapping(self):
        url = "{}/slam/map/stop".format(self.url_base)
        return self.client.post(url)

    def get_map(self):
        url = "{}/slam/map".format(self.url_base)
        return self.client.get(url)

    def get_slampath(self, x, y):
        url = "{}/slam/path".format(self.url_base)
        payload = {
            "X": x,
            "Y": y,
        }
        return self.client.get(url, params=payload)

    def start_tracking(self):
        url = "{}/slam/track/start".format(self.url_base)
        return self.client.post(url)

    def stop_tracking(self):
        url = "{}/slam/track/stop".format(self.url_base)
        return self.client.post(url)

    def drive_to_location(self, x, y):
        self.start_tracking()
        url = "{}/drive/coordinates".format(self.url_base)
        payload = {
            "Destination": "{0}:{1}".format(x, y)
        }
        resp = self.client.post(url, payload)
        self.stop_tracking()
        return resp

    def follow_path(self, path):
        self.start_tracking()
        url = "{}/drive/path".format(self.url_base)
        payload = {
            "Path": path,
        }
        resp = self.client.post(url, payload)
        self.stop_tracking()
        return resp

def slam_stream(func):
    """Decorator used to handle opening and closing of SLAM stream.

    Args:
      func (function): Function being decorated.

    Returns:
      function: stream inner function
    """
    def stream(*args, **kwargs):
        """Opens and closes stream after function call.

        Args:
          *args: Variable length argument list.  
          **kwargs: Arbitrary keyword arguments.
        """
        # Assumption is made that only classes pertaining
        # to the REST API are being decorated. Arg 0 = self.
        slam = SLAM(args[0].ip)
        slam.start()
        resp = func(*args, **kwargs)
        slam.stop()
        return resp
    return stream
