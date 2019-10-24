from misty_client import base


class Expression(base.Base):

    def __init__(self, ip):
        super(Expression, self).__init__(ip)

    def change_led(self, red=255, green=255, blue=255):
        url = "{}/led".format(self.url_base)
        payload = {
            "red": red,
            "green": green,
            "blue": blue,
        }
        return self.client.post(url, payload)

    def display_image(self, filename="", alpha=1):
        url = "{}/images/display".format(self.url_base)
        payload = {
            "FileName": filename,
            "Alpha": alpha,
        }
        return self.client.post(url, payload)

    def play_audio(self, assestId=None, filename=None, volume=50):
        url = "{}/audio/play".format(self.url_base)
        payload = {
            "fileName": filename,
            "volume": volume,
        }
        return self.client.post(url, payload)

    def turn_light_on(self):
        url = "{}/flashlight".format(self.url_base)
        payload = {
            "On": "true"
        }
        return self.client.post(url, payload)

    def turn_light_off(self):
        url  = "{}/flashlight".format(self.url_base)
        payload = {
            "On": "false"
        }
        return self.client.post(url, payload)
