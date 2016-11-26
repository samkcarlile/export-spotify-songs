import requests
import json
import codecs

f = open('spotify-songs.txt', "r")
out = codecs.open('exported.txt', "a", 'utf-8')
list = f.readlines()

pos = 0
while pos < len(list):
    stop = pos+49
    if stop > len(list):
        stop = len(list)
    ids = ""
    for i in range(pos, stop):
        ids += list[i].split(":")[2][:-1]
        if i != stop - 1:
            ids += ","
    if pos+50 > len(list):
        pos = len(list)
    else:
        pos += 49
    url = "https://api.spotify.com/v1/tracks/?ids=" + ids
    r = requests.get(url)
    jsonData = r.json()
    tracksJsonArray = jsonData["tracks"]
    for trackJson in tracksJsonArray:
        name = trackJson["name"]
        artists = ""
        for artist in trackJson["artists"]:
            if len(artists) > 1:
                artists = artists + ","
            artists = artists + artist["name"]
        trackTxt = name + " | " + artists + "\n"
        out.write(trackTxt)
out.close()