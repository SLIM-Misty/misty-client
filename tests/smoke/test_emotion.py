import base64
import json
import os
import operator
import time

from misty_client.expression import Expression
from misty_client.perception.visual import Picture
from misty_client.perception import emotion

pic = Picture("10.10.0.7")
expr = Expression("10.10.0.7")

while True:
    filename = "test.png"
    resp = pic.take(filename, 600, 400)
    
    img_str = json.loads(resp.content)["result"].get("base64")
    img_data = base64.b64decode(img_str)
    
    with open(filename, 'wb') as f:
        f.write(img_data)
    
    emotions = emotion.get_face_emotion(os.path.join(os.getcwd(), filename))
    
    primary_face = emotions["face"][0]
    
    max_emotion = max(primary_face.iteritems(), key=operator.itemgetter(1))[0]
    
    if max_emotion == "happiness":
        expr.display_image("e_Joy2.jpg")
    elif max_emotion == "sadness":
        expr.display_image("e_Sadness.jpg")
    elif max_emotion == "disgust":
        expr.display_image("e_Disgust.jpg")
    elif max_emotion == "contempt":
        expr.display_image("e_ApprehensionConcerned.jpg")
    elif max_emotion == "surprise":
        expr.display_image("e_Amazement.jpg")
    elif max_emotion == "anger":
        expr.display_image("e_Anger.jpg")
    else:
        expr.display_image("e_DefaultContent.jpg")

    print(max_emotion)

    time.sleep(.01)
