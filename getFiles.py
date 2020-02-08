import pdb
from os import listdir
from os.path import isfile, join
mypath = "Thumbnails/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

files = [i[:-4] for i in onlyfiles]
files.sort()
files.pop(0)  # Removes the .DS_Store file
read = open("videoID.txt").readlines()

timestamp = [i.split(',')[1].split("T")[0] for i in read]

missing = list((set(files) | set(timestamp)) -
               (set(files) & set(timestamp)))  # if you need a list

pdb.set_trace()
print(missing)

# There was an isssue where the number of Downloads were not matching the number of video IDs being passed.
# This was because I named the files with just the date initially so days where multiple videos were being uploaded in a day were being omitted
# This script has served its purpose.
