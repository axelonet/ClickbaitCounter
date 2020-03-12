import base64
import PIL.Image
import dlib
import numpy as np
from celery import Celery, shared_task
import pickle
import io
import json

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
