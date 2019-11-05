import base64
import json
import os

from misty_client.perception.visual import Picture
from misty_client.perception import emotion

### Take a standard rbg picture
pic = Picture("10.10.0.7")
filename = "test.png"
resp = pic.take(filename, 600, 400)

img_str = json.loads(resp.content)["result"].get("base64")
img_data = base64.b64decode(img_str)

with open(filename, 'wb') as f:
    f.write(img_data)

emotions = emotion.get_face_emotion(os.path.join(os.getcwd(), filename))

print(emotions)
