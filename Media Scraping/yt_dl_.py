# remove substring: feat. w/ regex function
# yt dl: rate similarity w/ spotify track based on chars matched / total
# lowercase, string split song name / artist or get that seperately
# this module should be designed to convert the youtube bookmarks to track ids that we can input into spotify

base_video_url = 'https://www.youtube.com/watch?v='
base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1.format(api_key, channel_id)
inp = urllib.urloppen(url)
resp = json.load(inp)

vidID = resp['items'][0]['id']['videoId']

video_exists = false
with open('videoid.json', 'r') as json_file:
data = json.load(json_file)
if data['videoId] != vidID:
drier = webdriver.Firefox()
driver.get(base_video_url + vidID)
video_exists = True

if video_exists:
with open('video.json', 'w') as json_file:
data = {'videoId': vidID}
json.dump(data, json_file)

#yt dl base
import youtube_dl #to download videos
import os, sys, shutil, subprocess #file management and command center
import eyed3 #assign/load meta data?
import urllib.request #downloading cover art and adding to audio file
from urllib.parse import urlparse
import requests
import bs4

ydl_options = {
    'format': 'bestaudio/best',
}

def downloadVideo():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        # Download video as mp3
        global ytVid
        ydl.download([str(ytVid)])

support to download playlists, add/assign metadata w. eyed3, rename songs, use requests to download cover art

# Get cover art
        imgURL = input('Input cover art URL: ')
        imgLink = requests.get(imgURL)

        # Downloads cover art
        f = open('cover.jpg','wb')
        f.write(imgLink.content)
        f.close()

        # Sets cover art
        audiofile.tag.images.set(3, open('cover.jpg','rb').read(), 'image/jpeg') #test if png or jpeg, also error checks
        
        # Deletes cover art
        os.remove('cover.jpg')
        print('Cover art added!') #playlist iteration

        # Saves song
        audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
        print('Video successfully downloaded!')

spotify create a playlist DOCS 
endpoint https://api.spotify.com/v1/users/{user_id}/playlists