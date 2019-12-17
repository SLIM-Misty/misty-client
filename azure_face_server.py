import base64
import json
import os
import operator
import time
import websockets
import asyncio

from misty_client.perception import emotion
from misty_client.expression import Expression

expr = Expression("10.10.0.7")

async def process_image(websocket, message):
    parsed_message = json.loads(message)
    image_base_64 = parsed_message['image']

    filename = "cur_image.png"
    img_data = base64.b64decode(image_base_64)
    
    with open(filename, 'wb') as f:
        f.write(img_data)
    
    emotions = emotion.get_face_emotion(os.path.join(os.getcwd(), filename))
    
    if not emotions:
        return_data = {}
        return_data['max_emotion'] = 'none'
        await websocket.send(json.dumps(return_data))
    else:
        primary_face = emotions["face"][0]
        
        max_emotion = max(primary_face.items(), key=operator.itemgetter(1))[0]
        
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
        
        return_data = {}
        return_data['max_emotion'] = max_emotion
        return_data['all_emotion_data'] = emotions
        print("image successfully processed")
        await websocket.send(json.dumps(return_data))


# Websocket logic 
# https://websockets.readthedocs.io/en/stable/intro.html
 
async def consumer_handler(websocket, path):
  async for message in websocket:
    print('recvd messg')
    await process_image(websocket, message)

start_server = websockets.serve(consumer_handler, "localhost", 8766)
print('Websocket listening on port 8766!')
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
