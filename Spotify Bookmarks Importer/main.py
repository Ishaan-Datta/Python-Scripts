# Add Youtube Bookmarks to liked songs playlist
# Organize songs into playlists based on artists or genre from datasets (Kaggle?)
# Remove duplicate songs from spotify (threshold similarity checker)
# need access to liked videos/names
# create new spotify playlist
# use youtube-dl to collect track name and artist and put into json
# add song to new spotify playlist
# alert system if the song cannot be found
# using python requests library: need to know API endpoint, request body, HTTP method
# login to youtube account with credentials
# use youtube API to retrieve liked videos
# search for song with spotify query search API
# dictionary and sets usage, swap key and value pairs if no match is found
# make json with list of songs marked if completed or not
# Remove substring, feat.
# int convert duration
# tuple for track details
# itertool intersect for duplicates among playlists
# database instead of dict for large storagte
# Yt-dl to download list of bookmarks or onetabs


# app requests authorization to access data: client_id, response_type, redirect_uri, state, scopes
# sptofiy accounts service displays scopes and prompts user to login if requried
# user logs in and authorizes access: code, state
# app requests access and refresh tokens: client_id, client_secret, grant_type, code, redirect_uri
# sptofy accounts service returns access and refresh tokens: access_token, token_type, expires_in, refresh_token
# app uses access token in requests to Web API
# spotify web api returns requested data as json object
# app sends user acccess token in requests to Web API, spotityf accounts service returns json object
# sptofiy accounts ervices returns new access toiken

from flask import Flask, request, url_for, session, redirect
import spotipy
import time
import json
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

app.secret_key = "uhg83ghalkgh"
# session object is where you store data about users session
app.config["SESSION_COOKIE_NAME"] = "spotify-login-session"


# setting up endpoints
@app.route("/")
def login():
    sp_oauth = create_Spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@app.route("/authorize")
def authorize():
    sp_oauth = create_Spotify_oauth()
    session.clear()
    code = request.args.get("code")
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect("/getTracks")


@app.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")


@app.route("/getTracks")
def get_all_tracks():
    session["token_info"], authorized = get_token()
    session.modified = True
    if not authorized:
        return redirect("/")
    sp = spotipy.Spotify(
        auth=session.get("token_info").get("access_token")
    )  # type:ignore
    results = []
    # iter = 0
    # while True:
    #     offset = iter * 50
    #     iter += 1
    #     curGroup = sp.current_user_saved_tracks(limit=50, offset=offset)['items'] #type:ignore
    #     for idx, item in enumerate(curGroup):
    #         track = item['track']
    #         val = track['name'] + " - " + track['artists'][0]['name']
    #         results += [val]
    #     if (len(curGroup) < 50):
    #         break

    # df = pd.DataFrame(results, columns=["song names"])
    # df.to_csv('songs.csv', index=False)

    # my app goes here :smiling_imp:
    # Get userID/Oauth token, put into secrets.py file:
    # Spotify_token = ''
    # Spotify_user_id = ''

    # Class CreatePlaylist:
    #     Def  __init__(self):
    #         Pass
    #     Def get youtube client
    #     Def get liked videos
    #     Def create playlist
    #     Def get spotify url
    #     Def add_song_to_playlist

    return "done"


# Checks to see if token is valid and gets a new token if not
def get_token():
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get("token_info", False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = (
        session.get("token_info").get("expires_at") - now < 60
    )  # type:ignore

    # Refreshing token if it has expired
    if is_token_expired:
        sp_oauth = create_Spotify_oauth()
        token_info = sp_oauth.refresh_access_token(
            session.get("token_info").get("refresh_token")
        )  # type:ignore

    token_valid = True
    return token_info, token_valid


def create_Spotify_oauth():
    return SpotifyOAuth(
        client_id="c39f421890d541e8b24af2449d5f2e69",
        client_secret="60974b4a939447fcbfd66464a277981f",
        redirect_uri=url_for("authorize", _external=True),
        scope="user-library-read",
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

import spotipy
import spotipy.util as util
from pymongo import MongoClient
from profileinfo import username, client_id, client_secret, cluster
import time

# database setup
client = MongoClient(cluster)
db = client.spotify
stats = db.stats

# spotify login
token = util.prompt_for_user_token(
    username,
    scope=[
        "user-read-recently-played",
        "playlist-modify-private",
    ],  # https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost/",
)

# sets starting point
most_recent = {
    "name": "Dark seeks light",
    "artist": "ニノミヤユイ",
    "duration": 214426,
    "played_at": "2022-01-24T16:11:20.801Z",
}

while True:
    sp = spotipy.Spotify(auth=token)
    recently_played = sp.current_user_recently_played(limit=50)["items"]

    for song in recently_played:
        my_dict = {"name": [], "artist": [], "duration": [], "played_at": []}
        my_dict["name"] = song["track"]["name"]
        my_dict["artist"] = song["track"]["artists"][0]["name"]
        my_dict["duration"] = song["track"]["duration_ms"]
        my_dict["played_at"] = song["played_at"]

        # check if updated
        if my_dict == most_recent:
            print("caught up!")
            break

        result = stats.insert_one(my_dict)
        print(f"Inserted: {my_dict}")

    # set new most_recent
    most_recent = {
        "name": recently_played[0]["track"]["name"],
        "artist": recently_played[0]["track"]["artists"][0]["name"],
        "duration": recently_played[0]["track"]["duration_ms"],
        "played_at": recently_played[0]["played_at"],
    }

    print(f"most recent: {most_recent}")
    time.sleep(7200)

import base64
import json
import os
import requests
import uuid
import urllib.parse
from credentials import id, secret
from flask import Flask, redirect, render_template, request

client_id = id
client_secret = secret
redirect_uri = "http://localhost:8888/callback"
state = str(uuid.uuid4())
access_token = None

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET"])
def login():
    params = {
        "response_type": "code",
        "client_id": client_id,
        "scope": "user-top-read",
        "redirect_uri": redirect_uri,
        "state": state,
    }

    url_safe_params = urllib.parse.urlencode(params)
    return redirect("https://accounts.spotify.com/authorize?" + url_safe_params)


@app.route("/callback")
def callback():
    # verify state
    compare_state = request.args.get("state")
    if state == compare_state or state != None:
        print("state verified")

        params = {
            "grant_type": "authorization_code",
            "code": request.args.get("code"),
            "redirect_uri": redirect_uri,
        }

        headers = {
            "authorization": "Basic "
            + base64.b64encode(
                bytes(f"{client_id}:{client_secret}", "ISO-8859-1")
            ).decode("ascii"),
            "content-type": "application/x-www-form-urlencoded",
        }

        r = requests.post(
            "https://accounts.spotify.com/api/token", data=params, headers=headers
        )

        global access_token
        access_token = r.json()["access_token"]

        get_top_songs(access_token, "short_term")

        return render_template("callback.html")

    else:
        # error
        return render_template("home.html")


@app.route("/refresh")
def refresh():
    params = {
        "grant_type": "refresh_token",
        "refresh_token": request.args.get("refresh_token"),
    }

    headers = {
        "authorization": "Basic "
        + base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode(
            "ascii"
        ),
        "content-type": "application/x-www-form-urlencoded",
    }

    r = requests.post(
        "https://accounts.spotify.com/api/token", data=params, headers=headers
    )

    global access_token
    access_token = r.json()["access_token"]

    return render_template("callback.html")


def get_top_songs(access_token, term_length):
    headers = {"Authorization": "Bearer " + access_token}

    params = {"time_range": term_length, "limit": 50}

    r = requests.get(
        "https://api.spotify.com/v1/me/top/tracks", headers=headers, params=params
    )
    print(r.json())


if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True)

# spotify initial handshake
import json
import requests
from credentials import id, secret

client_id = id
client_secret = secret

url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": "Basic",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {"grant_type": "client_credentials"}

initial_call = requests.post(
    url, headers=headers, data=data, auth=(client_id, client_secret)
).json()

access_token = initial_call["access_token"]

get_data = requests.get(
    "https://api.spotify.com/v1/search?q=artist:abba&type=album",
    headers={"Authorization": "Bearer " + access_token},
).json()

print(get_data)

# happens after bookmark parser, give path to bookmark file, parser cleans up duplicates, then select folder with music bookmarks, should automatically parse from start to end of folder from pandas dataframe which is cleaned from duplicates/renamed properly, adds all youtube videos to playlist, maybe parses liked videos for music related ones, applies yt-dl to all videos in playlist, logs into spotify and uses API to add them to playlist which you set name for, loading messages all the time
# genre vs random shuffle
# volume mixer stabilizer system
