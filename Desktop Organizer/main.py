import os, shutil
from pathlib import Path

audio = (
    ".3ga",
    ".aac",
    ".ac3",
    ".aif",
    ".aiff",
    ".alac",
    ".amr",
    ".ape",
    ".au",
    ".dss",
    ".flac",
    ".flv",
    ".m4a",
    ".m4b",
    ".m4p",
    ".mp3",
    ".mpga",
    ".ogg",
    ".oga",
    ".mogg",
    ".opus",
    ".qcp",
    ".tta",
    ".voc",
    ".wav",
    ".wma",
    ".wv",
)

videos = (
    ".webm",
    ".MTS",
    ".M2TS",
    ".TS",
    ".mov",
    ".mp4",
    ".m4p",
    ".m4v",
    ".mxf",
    ".mkv",
)

images = (
    ".jpg",
    ".jpeg",
    ".jfif",
    ".pjpeg",
    ".pjp",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".apng",
    ".avif",
    ".ai",
    ".psd",
)

applications = (".zip", ".iso", ".jar", ".msi", ".exe", ".rar", ".ttf")

documents = (
    ".epub",
    ".pages",
    ".docx",
    ".doc",
    ".txt",
    ".pdf",
    ".pptx",
    ".ppt",
    ".xlsx",
    ".csv",
)

programming = (".py", ".c", ".html", ".sql")


def is_audio(file):
    return os.path.splitext(file)[1] in audio


def is_programming(file):
    return os.path.splitext(file)[1] in programming


def is_video(file):
    return os.path.splitext(file)[1] in videos


def is_image(file):
    return os.path.splitext(file)[1] in images


def is_application(file):
    return os.path.splitext(file)[1] in applications


def is_document(file):
    return os.path.splitext(file)[1] in documents


def sort_dir():
    dir = input(
        "Please input the name or path of the directory you would like to sort: "
    )
    try:
        os.chdir(dir)
        num_files = len([f for f in os.listdir(".") if os.path.isfile(f)])
        print(num_files)
        print("Sorting files...")

        for file in os.listdir(dir):  # renaming support? # organizing by date/month
            if is_audio(file):
                shutil.move(file, "Users/patrick/Documents/audio")  # change locations
            elif is_video(file):
                shutil.move(file, "Users/patrick/Documents/video")
            elif is_image(file):
                shutil.move(file, "Users/patrick/Documents/screenshots")
            elif is_application(file):
                shutil.move(file, "Users/patrick/Documents")
            elif is_document(file):
                shutil.move(file, "Users/patrick/Documents")
            elif is_programming(file):
                shutil.move(file, "Users/patrick/Coding")
            else:
                print("File extension does not match library")
                # move to backup folder
        print("All files have been sorted!")
    except:
        print(
            "Directory name does not exist or is invalid, please enter a valid name or the full path to the directory. "
        )
        sort_dir()


sort_dir()
