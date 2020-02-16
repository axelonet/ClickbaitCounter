from shutil import copyfile
from pathlib import Path
import face_recognition
import pdb
from os import listdir
from os.path import isfile, join
from PIL import Image

mypath = "Thumbnails/"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files.sort()
if '.DS_Store' in files:
    files.remove('.DS_Store')  # Removes the .DS_Store file

images = [face_recognition.load_image_file(mypath + "/" + i) for i in files]


# I would have to remember which encoding belongs to which face.
face_data = []
face_positions = []
for i in images:
    face_data.append(face_recognition.face_encodings(i))
    face_positions.append(face_recognition.face_locations(i))

# face_data is now a list of lists of lists. The most internal list contains 128 values for each face, this is repeated for the number of faces in an image, this is repeated for all images.
# face_positions is now a list of lists of tuples. The most internal tuple contains (top, right, bottom, left) co-ordinates of each face, this is repeated for the number of faces in an image, this is repeated for all images.

face_counter = 0
recognised_faces = {}
known_faces = []

Path("results").mkdir(parents=True, exist_ok=True)

for i in range(len(face_data[0])):
    string = "unknown_face" + str(face_counter)
    face_counter += 1
    recognised_faces[string] = [0]
    known_faces.append(face_data[0][i])

    string = "results/" + string
    Path(string).mkdir(parents=True, exist_ok=True)
    imageSrc = mypath + files[0]
    image = Image.open(imageSrc)
    tempImage = image.crop(
        (face_positions[0][i][3], face_positions[0][i][0], face_positions[0][i][1], face_positions[0][i][2]))
    string = string + "/" + files[0]
    tempImage.save(string)

for i in range(1, len(face_data)):
    for j in range(len(face_data[i])):
        results = face_recognition.compare_faces(known_faces, face_data[i][j])
        for k in range(len(results)):
            if results[k] == True:
                # Know which face has been recognised
                string = "unknown_face" + str(k)
                recognised_faces[string].append(i)

                string = "results/" + string
                Path(string).mkdir(parents=True, exist_ok=True)
                imageSrc = mypath + files[i]
                image = Image.open(imageSrc)
                tempImage = image.crop(
                    (face_positions[i][j][3], face_positions[i][j][0], face_positions[i][j][1], face_positions[i][j][2]))
                string = string + "/" + files[i]
                tempImage.save(string)

        if not True in results:
            # Add the encodings to known faces and recognised faces
            string = "unknown_face" + str(face_counter)
            face_counter += 1
            recognised_faces[string] = [i]
            known_faces.append(face_data[i][j])

            string = "results/" + string
            Path(string).mkdir(parents=True, exist_ok=True)
            imageSrc = mypath + files[i]
            image = Image.open(imageSrc)
            tempImage = image.crop(
                (face_positions[i][j][3], face_positions[i][j][0], face_positions[i][j][1], face_positions[i][j][2]))
            string = string + "/" + files[i]
            tempImage.save(string)
        results = []
