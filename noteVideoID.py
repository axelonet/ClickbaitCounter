import json
videoID = []
timestamp = []
for j in range(1, 12):
    page = "API requests/page" + str(j) + ".json"
    with open(page) as f:
        data = json.load(f)

    for i in range(50):
        videoID.append(data["items"][i]["contentDetails"]["videoId"])
        timestamp.append(data["items"][i]["contentDetails"]
                         ["videoPublishedAt"])

with open('videoID.txt', 'w') as f:
    for i in range(len(videoID)):
        f.write("%s,%s\n" % (videoID[i], timestamp[i]))
