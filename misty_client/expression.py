from misty_client import base


class NoAudioFileException(Exception):
    pass


class Expression(base.Base):
    """Contains various functions to interact with Misty's expression endpoints."""

    def __init__(self, ip):
        """Initializes the Expression class with the IP of Misty.

        Args:
          ip (str): IP address of the Misty robot.
        """
        super(Expression, self).__init__(ip)

    def change_led(self, red=255, green=255, blue=255):
        """Changes the color of the LED light behind the logo on Misty's torso.

        Args:
          red (int): The red RGB color value (range 0 to 255).
          green (int): The green RGB color value (range 0 to 255).
          blue (int): The blue RGB color value (range 0 to 255).

        Return:
          bool: Returns true if there are no errors related to this command.
        """

        url = "{}/led".format(self.url_base)
        payload = {
            "red": red,
            "green": green,
            "blue": blue,
        }
        return self.client.post(url, payload)

    def display_image(self, filename, alpha=1):
        """Displays an image on Misty's screen.

        Args:
          filename (str): Name of the file containing the image to dislpay.
          alpha (float): The transparency of the image from 0 to 1.

        Return:
          bool: Returns true if there are no errors related to this command.
        """

        url = "{}/images/display".format(self.url_base)
        payload = {
            "FileName": filename,
            "Alpha": alpha,
        }
        return self.client.post(url, payload)

    def play_audio(self, assetId=None, filename=None, volume=50):
        """Plays an audio file.

        Args:
          assetId (str): ID of the file to play.
          filename (str): Name of the file to play.
          volume (int): A value between 0 and 100 for loudness of audio. 

        Return:
          str: Returns a string with any errors related to this command.
        """

        if not assetId and not filename:
            raise NoAudioFileException("No file or assetId specified")
        url = "{}/audio/play".format(self.url_base)
        payload = {
            "fileName": filename,
            "volume": volume,
        }
        return self.client.post(url, payload)

    def turn_light_on(self):
        """Turns the LED flashlight on Misty's head on.

        Return:
          str: Returns a string with any errors related to this command.
        """

        url = "{}/flashlight".format(self.url_base)
        payload = {
            "on": "true"
        }
        return self.client.post(url, payload)

    def turn_light_off(self):
        """Turns the LED flashlight on Misty's head off.

        Return:
          str: Returns a string with any errors related to this command.
        """

        url  = "{}/flashlight".format(self.url_base)
        payload = {
            "on": "false"
        }
        return self.client.post(url, payload)
