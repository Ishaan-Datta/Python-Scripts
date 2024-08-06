import pprint
import re
import csv
import pandas as pd

# Extracting bookmark/folder data from file

file_name = (
    "C:/Users/ishaa/OneDrive - UBC/Coding/Unfinished/Projects/Bookmark Parser/test.html"
)

with open(file_name, "r", encoding="UTF-8") as file:
    path = "Bookmarks Bar"
    master_directory = {}
    bookmarks = []
    folders = []

    while True:
        line = file.readline()
        master_directory[f"{path}_bookmarks"] = 
        if not line:
            break


def bookmark_parser(line, path, indent):
    bookmarks = []
    bookmark_data_pattern = re.compile(
        '<DT><A HREF="(.*?)" ADD_DATE="(\\d+)"[^>]*>(.*?)</A>'
    )
    bookmark_matches = bookmark_data_pattern.search(line)
    if bookmark_matches != None:
        bookmarks.append(
            (
                bookmark_matches[1],
                bookmark_matches[2],
                bookmark_matches[3].strip(),
            )
        )
    return bookmarks


def folder_parser(line, path, indent):
    folders = []
    folder_data_pattern = re.compile(">([^>]+)</H3>")
    folder_matches = folder_data_pattern.search(line)
    if folder_matches != None:
        folders.append(folder_matches[1])
    return folders

# # RENAMING AND DUPLICATE DETECTION
removal_patterns = []
youtube_subscription_pattern = re.compile("(\(\d+\))")
youtube_label_pattern = re.compile(" - YouTube")
google_label_pattern = re.compile(" - Google Search")


bookmark_df = {
    "Indent Level:": "bruh",
    "Folder Path:": "bruh",
    "Name:": "bruh",
    "URL:": "bruh",
    "Date Modified:": "bruh",
}

df = pd.DataFrame(bookmark_df)

# displaying potential items for renaming:
for i in df.itertuples():
    bookmark_name = i[3]
    print(bookmark_name)
    names_list = bookmark_name.split()

    for item in names_list:
        print(item)
        item = re.sub(youtube_subscription_pattern, "", item)
        item = re.sub(youtube_label_pattern, "", item)
        print(item)

# duplicate links:
bool_series = df.duplicated(subset="Name")
print(f"Found {bool_series.count()} name duplicates.")

# duplicate names:
bool_series = df.duplicated(subset="URL")
print(f"Found {bool_series.count()} URL duplicates.")

# FILE REMAKING
# make backup before modifying original file, automatic renaming, just conversion to csv?
# definitely want to output this to csv for easier analysis, pandas review
# with this understanding could export the same folder back?
# experiment w/ ctrl C ctrl C ctrl V into excel and see what format works with import back?

# ADDITIONAL MODULES
# p shuffle feature, tagging, api, possibly using yt-dl to find video details
# static delay + random smaller
# pprint.pprint(bookmarks)
# option to make folders based on keywords or domain - OF, twitter
# additional module to flag videos that are private, dont exist, channels doesnt exist, etc.
