import random
import requests
import string
import urllib


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_random_tracks(self):
        wildcard = f"%{random.choice(string.ascii_lowercase)}%"
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)
        url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}",
            },
        )
        response_json = response.json()

        tracks = [track for track in response_json["tracks"]["items"]]

        print(f"Found {len(tracks)} tracks to add to your library")

        return tracks

    def add_tracks_to_library(self, track_ids):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={"ids": track_ids},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}",
            },
        )

        return response.ok


import os

from spotify_client import SpotifyClient


def run():
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track["id"] for track in random_tracks]

    was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
    if was_added_to_library:
        for track in random_tracks:
            print(f"Added {track['name']} to your library")


if __name__ == "__main__":
    run()

# oauth:
# oauth = SpotifyOAuth(
# 			client_id='clientid',
# 			client_secret='clientsecret',
# 			redirect_uri='localhost:8080/callback',
# 			scope='user-library-read'
# )

# redirect uri: after user approves, where do we send them back to?
# client secret: private secret only you and the server know (ex. password)
# scope: what i get access to (ex. user-playlists, email, ....)
# client id: unique ID for your app (ex. username)
# Automatic camera upload plus photo recognition for spotify -> companion app
# photo to text and classify song based on genre and add to respective fav playlist
# take screenshots on phone, sync photo to folder
# Sort artists by genre dataset
# for music recommendations/music trianer w/ keras use rico zhu
# could make smaller project for recommendation engine and listening tracking
# Stores Spotify listening history and metadata in a MongoDB database.
# track shuffle plays and skips to remove bad songs
# personalized music trainer using keras
# Vue.js web app to visualize sentiments throughout a piece of music!
# Track what users play and suggest similar songs based on their preferences.
# To challenge yourself, build a suggestion engine.
# remove duplicate songs on spotify
# Spotify remove not liked songs from all time and like them again
# smart shuffle
# queue storage
# streaming app for seamless transition between listeining from headphones, phone, laptop, desktop
# queue storage
# automated scraper for yotube vids from youtube music channels take their titles, add to spotify queue database
# analytics for how many songs from artist liked/listened to
# view playlists, if songs cannot be sorted by genre, check the playlist they are contained in, then ask user what genre the playlist goes under if you don’t select manual/individual organization option
# make playlist of songs next to listen to grouped by genre
# every 5 minutes when connected to home network swap spotify to online to donwload songs then turn off when disconnected from the home network
# dataset for artists and their respective genre for sorting within item folders in sptofy (linear regression)
# companion app: after some familiarity from bookmark app, just use api to get listening history, add entries to database and determine what songs are most listened to, skipped, and determine what should be removed from playlist accordingly
# image to text module to scrape names of songs from images
# consider making truly random widget player for windows etc.