from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import FaceAttributeType

KEY = "1837b9d29e0b4a22843d103a7ca8b3c9"
ENDPOINT = "https://westus2.api.cognitive.microsoft.com/"

class NoFaceFoundException(Exception):

    def __init__(self, filepath):
        self.message = "File: {}".format(filepath)


def get_face_emotion(filepath):
    """Gets emtion information about faces in provided image.

    Args:
     filepath (str): Full path to input file. Must be one of: .png, .jpg, .gif. File size from 1KB to 6MB.

    Returns:
       emotion_data (OrderedDict): Returns data on each emotion each face is showing. Largest face is first. 
    """

    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    with open(filepath, "rb") as face_fd:
        detected_faces = face_client.face.detect_with_stream(face_fd, return_face_attributes=FaceAttributeType.emotion)

    if not detected_faces:
        raise NoFaceFoundException(filepath) 

    emotion_data = {}
    emotion_data["face"] = []

    for face in detected_faces:
        emotion_data["face"].append({
            "anger": face.face_attributes.emotion.anger,
            "contempt": face.face_attributes.emotion.contempt,
            "disgust": face.face_attributes.emotion.fear, 
            "happiness": face.face_attributes.emotion.happiness, 
            "neutral": face.face_attributes.emotion.neutral, 
            "sadness": face.face_attributes.emotion.sadness, 
            "surprise": face.face_attributes.emotion.surprise 
        })

    return emotion_data 
