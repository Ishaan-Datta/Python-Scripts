import pprint
from bs4 import BeautifulSoup
import bs4
import re
import csv

# BEAUTIFUL SOUP TESTING
# soup = BeautifulSoup()
# with open(
#     "C:/Users/ishaa/OneDrive - UBC/Coding/Unfinished/Projects/Bookmark Parser/test.html",
#     "r",
#     encoding="cp437",
# ) as f:
#     soup = BeautifulSoup(f.read(), "lxml")

# dt = soup.find_all("dt")
# folder_name = ""
# for i in dt:
#     n = i.find_next()
#     if n.name == "h3":
#         folder_name = n.text
#         continue
#     else:
#         print(f'url = {n.get("href")}')
#         print(f"website name = {n.text}")
#         print(f'add date = {n.get("add_date")}')
#         print(f"folder name = {folder_name}")
#     print()


# bookmark_file = "bookmarks_2_10_23.html"

# def parse_bookmarks(file_content):
#     soup = BeautifulSoup(file_content, "html.parser")
#     bookmarks = []

#     for link in soup.find_all("a"):
#         href = link.get("href")
#         title = link.string
#         bookmarks.append({"title": title, "href": href})

#     return bookmarks

# def main():
#     with open(bookmark_file, encoding="utf-8") as file:
#         file_content = file.read()
#         bookmarks = parse_bookmarks(file_content)
#         for bookmark in bookmarks:
#             print("Title:", bookmark["title"], "URL:", bookmark["href"])
#         with open("bookmarks.csv", "w", encoding="utf-8", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(["Title", "URL"])
#             for bookmark in bookmarks:
#                 writer.writerow([bookmark["title"], bookmark["href"]]


# ITERTOOLS GROUPING
from itertools import groupby

line = '            <DT><A HREF="https://www.youtube.com/" ADD_DATE="1672005364" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABx0lEQVQ4jZ2TQWtTQRDHfzO7yUsNKSG0heJJ0YKnCvVSkHrV7+BBeu7Vk9+lH8CLN6EXk4Lo1V48lGClFBELGmmSmr73djy8fS8vll4c+LO7s7OzM///LhQmBmrg+uDtZrgIBQQAKyf/YQbiBexFt9t9niSP7ji3umrW7og0UfWL0ZaOzGYjmBxn2c/BdPpJxuNz+vDwFxxnqmaqZs4V8L5AuS6haqmqXcDpO3jCEN4YmEFmkMcxrSCSGqSh8GcGIY52Am91Ce5HJ5EYBRwbG45222HmUHVS+DX2DhASuKu3oAeolGSqCiDs7gqHh8L2thCCxOQSbxFAO9BToClzNQSJokwmsLUFgwHs78P6eklnlQho6c0axUKbTVhZgUYjHpeqCwE8kMWFxYNF9uVlGA5hbw8ODuqJzajqnPENPtfYDxU2N4OtrRVzkVDfC0V8/h2G/g98AR7ESkJF8tFRcYdzkOf15iRW6y/hlD48voCz+BbmELFrvhrG8OMjPBOAV3D7qXM791R73Var00qSJRoNTyifB5Dn+eVsNv19dTX+mmWj93n+4SWciM1LKkmqy7RoImFBqPqPfH39K7t/4A18f74nAH8Bjm35s3ZkOjEAAAAASUVORK5CYII=">YouTube</A>'
indent_list = [
    list(value) for keys, value in groupby(line, key=lambda x: x == " ") if keys == True
]
line_indent_level = int(max(x.count(" ") for x in indent_list) / 4)

file_name = (
    "C:/Users/ishaa/OneDrive - UBC/Coding/Unfinished/Projects/Bookmark Parser/test.html"
)

with open(file_name, "r", encoding="UTF-8") as file:
    lines = file.readlines()
    counter = 0
    for line in lines:
        if line.count("</DL><p>"):
            counter += 1
            print("found something")
            print(counter)

# def line_number(word):
#     lines = file.readlines()
#     word = f">{word}</H3>"
#     for line_number, line in enumerate(lines, 0):
#         if word in line:
#             print(f"word is in line {line_number}")

# print(line_number("Science/Math"))
