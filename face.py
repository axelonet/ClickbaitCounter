from shutil import copyfile
from pathlib import Path
import face_recognition
import pdb
from os import listdir
from os.path import isfile, join
mypath = "Face Recognition Sample/"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files.sort()
files.pop(0)  # Removes the .DS_Store file

# Load the jpg files into numpy arrays
# biden_image = face_recognition.load_image_file(
#     "face_recognition/examples/biden.jpg")
# obama_image = face_recognition.load_image_file(
#     "face_recognition/examples/obama.jpg")
# unknown_image = face_recognition.load_image_file(
#     "face_recognition/examples/obama2.jpg")
images = [face_recognition.load_image_file(mypath + "/" + i) for i in files]


# I would have to remember which encoding belongs to which face.
face_data = []
for i in images:
    face_data.append(face_recognition.face_encodings(i))

# face_encodings is now a list of lists of lists. The most internal list contains 128 values for each face, this is repeated for the number of faces in an image, this is repeated for all images.

face_counter = 0
recognised_faces = {}
known_faces = []
for i in range(len(face_data[0])):
    string = "unknown_face" + str(face_counter)
    face_counter += 1
    recognised_faces[string] = [0]
    known_faces.append(face_data[0][i])

for i in range(1, len(face_data)):
    for j in range(len(face_data[i])):
        results = face_recognition.compare_faces(known_faces, face_data[i][j])
        for k in range(len(results)):
            if results[k] == True:
                # Know which face has been recognised
                string = "unknown_face" + str(k)
                recognised_faces[string].append(i)
        if not True in results:
            # Add the encodings to known faces and recognised faces
            string = "unknown_face" + str(face_counter)
            face_counter += 1
            recognised_faces[string] = [i]
            known_faces.append(face_data[i][j])
        results = []
Path("results").mkdir(parents=True, exist_ok=True)
for faces in recognised_faces:
    string = "results/" + faces
    Path(string).mkdir(parents=True, exist_ok=True)
    for i in recognised_faces[faces]:
        src = mypath + files[i]
        dst = string + "/" + files[i]
        copyfile(src, dst)

pdb.set_trace()


# with open('encodings.txt', 'w') as f:
#     for i in range(len(face_encodings)):
#         f.write("%s\n" % face_encodings)

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.

# try:
#     biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
#     obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
# except IndexError:
#     print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
#     quit()

# known_faces = [
#     biden_face_encoding,
#     obama_face_encoding
# ]

# # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
# results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# print("Is the unknown face a picture of Biden? {}".format(results[0]))
# print("Is the unknown face a picture of Obama? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(
#     not True in results))
