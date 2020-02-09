from PIL import Image
from os import listdir
import face_recognition

from os.path import isfile, join
mypath = "Face Recognition Sample/"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files.sort()
files.pop(0)  # Removes the .DS_Store file
string = mypath + files[0]

images = face_recognition.load_image_file(mypath + "/" + files[0])

location = face_recognition.face_locations(images)
# (top, right, bottom, left) tuple. Needs to be converted to crop
print(location)
# For Cropping the faces
image = Image.open(string)
width, height = image.size
coordinates = []

# Converts (top, right, bottom, left) to (left, top, right, bottom)
for i in range(len(location)):
    coordinates.append((location[i][3], location[i][0],
                        location[i][1], location[i][2]))

image = image.crop(coordinates[0])
# image = image.crop((0, 0, 160, 360)) #face-1
# image = image.crop((160, 0, 320, 360))  # face-2
# image = image.crop((320, 0, 480, 360))  # face-3

image.save(files[2])

# This script successfully finds the faces and saves them in a new file.
# This script has served its purpose.
