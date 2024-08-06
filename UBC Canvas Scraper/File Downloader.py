import requests, shutil, time, os, json, re

from urllib.parse import urljoin
from pathlib import Path
from datetime import datetime
from canvasapi import Canvas

CANVAS_URL = "https://canvas.ubc.ca/api/v1/"
headers = {
    "Authorization": "Bearer 11224~mlkX4ksmPJcY2krFsnjUAjJ8lWBCl14w27LTq4g0J4tm5nDw2wOiIsIfXsDDKGnM"
}


def send_request(url):
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        return None
    else:
        paginated = response.json()
        while "next" in response.links:
            response = requests.get(response.links["next"]["url"], headers=headers)
            paginated.extend(response.json())

    return paginated


# add functionality to load meta data from files into database
def check_existing(course_name):
    COURSE_DIR = str(Path.home() / "OneDrive - UBC/Resources/3rd Year")
    file_list = []

    path = str(Path(COURSE_DIR) / course_name)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_list.append(file)
    existing_files[course_name] = file_list


def get_files(id, course_name):
    url = urljoin(CANVAS_URL, f"courses/{id}/files")

    if send_request(url) is not None:
        response_dict = send_request(url)
        files_count = len(response_dict)  # type: ignore
        print(f"Number of files: {files_count}")

        for x in range(files_count):
            if response_dict[x]["url"] != "":  # type: ignore
                course_files[course_name].append(response_dict[x]["display_name"])  # type: ignore
                file_id = response_dict[x]["url"].split("/")[-2]  # type: ignore
                real_url = url + "/" + file_id
                course_file_urls[course_name].append(real_url)  # type: ignore
                # download_file(response_dict[x], course_name)


def download_file(response, course_name):
    DOWNLOAD_DIR = str(Path.home() / "Downloads")
    COURSE_DIR = str(Path.home() / "OneDrive - UBC/Resources/3rd Year")

    file_name = response["display_name"]
    file_url = response["url"]
    created_at = response["created_at"]
    modified_at = response["modified_at"]
    size = response["size"]

    check_file_metadata(file_name, created_at, modified_at, size)

    # compare against file database metadata
    if file_name not in existing_files[course_name]:
        existing_files[course_name].append(file_name)
        response = requests.get(file_url, headers=headers)
        with open(Path(DOWNLOAD_DIR) / file_name, "wb") as file:
            file.write(response.content)
            print("downloaded")
        course_dir = Path(COURSE_DIR) / course_name
        shutil.move(Path(DOWNLOAD_DIR) / file_name, Path(course_dir) / file_name)
    else:
        print("already exists")


def load_meta_data(file_name, created_at, modified_at, size):
    pass


# load metadata from database and compare against file that is abotu to be downloaded to prompt notification system if newer version exists
def check_file_metadata(file_name, created_at, modified_at, size):
    pass


def get_modules(id, course_name):
    url = urljoin(CANVAS_URL, f"courses/{id}/modules")

    if send_request(url) is not None:
        response_dict = send_request(url)
        module_count = len(response_dict)  # type: ignore

        for x in range(module_count):
            response = requests.get(response_dict[x]["items_url"], headers=headers)  # type: ignore
            items_dict = response.json()
            item_count = len(items_dict)
            for y in range(item_count):
                if items_dict[y]["type"] == "File":
                    course_files[course_name].append(items_dict[y]["title"])
                    course_file_urls[course_name].append(items_dict[y]["url"])
                    # download_file(items_dict[y]['url'], course_name)
                if items_dict[y]["type"] == "Page":
                    get_page_files(items_dict[y]["url"], course_name)


def get_page_files(url, course):
    response = requests.get(url, headers=headers)
    response_dict = response.json()
    response_str = json.dumps(response_dict)

    name_pattern = re.compile(r'title="(.*?)"')
    name_matches = name_pattern.findall(response_dict["body"])
    filtered_names = [
        s
        for s in name_matches
        if "." in s
        and "Video player" not in s
        and "@" not in s
        and re.search(r"\.[a-zA-Z0-9]{1,8}$", s)
    ]
    course_files[course].extend(filtered_names)

    url_pattern = re.compile(r'data-api-endpoint="(.*?)"')
    file_matches = url_pattern.findall(response_dict["body"])
    filtered_files = [s for s in file_matches if "files" in s]

    for url in filtered_files:
        # download_file(url, course)
        course_file_urls[course].append(url)


def get_user_courses():
    API_URL = "https://ubc.instructure.com"
    API_KEY = "11224~mlkX4ksmPJcY2krFsnjUAjJ8lWBCl14w27LTq4g0J4tm5nDw2wOiIsIfXsDDKGnM"
    course_ids = {}

    canvas = Canvas(API_URL, API_KEY)
    user = canvas.get_user(606135)
    courses = user.get_courses(enrollment_state="active")

    for x in courses:
        if "-" not in x.name:
            components = x.name.split(" ")
            course = components[0] + " " + components[1]
            course_ids[course] = x.id

    return course_ids


def initialize():
    courses = get_user_courses()

    # asyncio implementation goes here
    for key, value in courses.items():
        print(f"Current Course: {key}")
        course_files[key] = []
        course_file_urls[key] = []
        get_files(value, key)
        get_modules(value, key)

    for course in courses:
        # check_existing(course)
        course_files[course] = list(set(course_files[course]))
        course_file_urls[course] = list(set(course_file_urls[course]))

        print(f"\n Course: {course}")

        print(f"Files: {len(course_files[course])}")
        print(course_files[course])

        print(f"URLs: {len(course_file_urls[course])}")
        print(course_file_urls[course])


existing_files = {}
course_files = {}
course_file_urls = {}

initialize()

# while True:
#     initialize()
#     time.sleep(300)

# comparison logic for existing files vs downloaded files
# download file should record file names and urls now
# api ate limits for downloads?
# test shutil behaviour for duplicate files, move ot backup folder
