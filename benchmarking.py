import time
import pdb
import face_recognition
from os import listdir
import PIL.Image
from os.path import isfile, join
import numpy as np
import base64
from tasks import load_image
import pyximport


start = time.time()


mypath = "Thumbnails/"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files.sort()
if '.DS_Store' in files:
    files.remove('.DS_Store')  # Removes the .DS_Store file

# images = [face_recognition.load_image_file(mypath + i) for i in files]

# images2 = [load_image(mypath + i) for i in files]

images2 = [load_image.delay(mypath + i) for i in files]

elapsed = time.time()
pdb.set_trace()
print('time elapsed: %.2f sec' % (elapsed - start))

# time elapsed: 6.42 sec
# np.array(images2[0].get(), dtype=np.uint8)
# face_data.append(face_recognition.face_encodings(
