# insta/tiktok automation w/ pyautogui and bot delay (watch video)
# database for insta and tikotk to find removed/banned users and inactive users from post history
# downloads naming
# instaloader module

import os
from TikTokApi import TikTokApi

def download_user_videos(username, folder):
    api = TikTokApi()

    # Get user object by username
    user = api.getUserObject(username)

    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Iterate through the user's videos
    for video in api.byUsername(username, count=user['userInfo']['stats']['videoCount']):
        video_url = video['video']['downloadAddr']
        video_id = video['id']
        video_file = os.path.join(folder, f"{video_id}.mp4")

        # Download the video
        api.downloadVideo(video_url, video_file)
        print(f"Downloaded video: {video_file}")

# Specify the username and folder to save the videos
username = "example_user"
folder = "downloaded_videos"

download_user_videos(username, folder)

# Make sure to replace "example_user" with the actual TikTok username of the user you want to download videos from, 
# and specify the desired folder to save the videos by replacing "downloaded_videos".


# from TikTokApi import TikTokApi
# import string
# import random
# did=''.join(random.choice(string.digits) for num in range(19))
# verifyFp="verify_YOUR_VERIFYFP_HERE"
# api = TikTokApi.get_instance(custom_verifyFp=verifyFp, custom_did=did)
# print(api.trending())
# count = 100
# tiktoks = api.trending(count=count)
# from pathlib import Path
# Path("downloads").mkdir(exist_ok=True)
# for i in range(len(tiktoks)):
#     data = api.get_Video_By_TikTok(tiktoks[i])# bytes of the video
#     with open("downloads/{}.mp4".format(str(i)), 'wb') as output:
#         output.write(data)

# tiktok notifier for when following banned
