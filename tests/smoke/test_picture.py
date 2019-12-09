import base64
import json

from misty_client.perception.visual import Picture


### Take a standard rbg picture
pic = Picture("10.10.0.7")
filename = "test.png"
resp = pic.take(filename, 600, 400)

img_str = json.loads(resp.content)["result"].get("base64")
img_data = base64.b64decode(img_str)

with open(filename, 'wb') as f:
    f.write(img_data)

### Take a fisheye picture
pic = Picture("10.10.0.7")
filename = "test_fisheye.png"
resp = pic.take_fisheye()

img_str = json.loads(resp.content)["result"].get("base64")
img_data = base64.b64decode(img_str)

with open(filename, 'wb') as f:
    f.write(img_data)

### Take a depth picture
pic = Picture("10.10.0.7")
filename = "test_fisheye.png"
resp = pic.take_depth()

img_arr = json.loads(resp.content)["result"].get("image")
assert len(img_arr) > 0
