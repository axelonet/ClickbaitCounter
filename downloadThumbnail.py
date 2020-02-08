import urllib.request
read = open("videoID.txt").readlines()
videoID = []
timestamp = []

videoID = [i.split(',')[0] for i in read]
timestamp = [i.split(',')[1].split(".")[0] for i in read]

for i in range(len(videoID)):
    urllib.request.urlretrieve(
        "https://img.youtube.com/vi/"+videoID[i]+"/hqdefault.jpg", "Thumbnails/" + timestamp[i] + ".jpg")
    print("Downloaded Image " + str(i))
