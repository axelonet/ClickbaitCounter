import base64
import PIL.Image
import dlib
import numpy as np
from celery import Celery, shared_task
import pickle
import io
import json
import face_recognition.api

app = Celery('benchmarking', broker='redis://localhost:6379/0',
             backend='redis://')


@shared_task
def load_image(file, mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array

    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    """
    im = PIL.Image.open(file)
    if mode:
        im = im.convert(mode)
    nparray = np.array(im)
    return nparray.tolist()

# dtype=np.uint8


@shared_task
def face_encodings(face_image, known_face_locations=None, num_jitters=1, model="small"):

    raw_landmarks = face_recognition.api._raw_face_landmarks(
        face_image, known_face_locations, model)
    return [np.array(face_recognition.api._face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for raw_landmark_set in raw_landmarks]


@shared_task
def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):

    return list(face_recognition.api._face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)
