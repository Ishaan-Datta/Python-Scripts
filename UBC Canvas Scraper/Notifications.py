# if file name (before appending datetime) already exists, notify w/ email that we scraped possible update/duplicate
# make list of files downloaded, when retrieving file data, if any files were removed, notify w/ email that we scraped possible mistake
# datetime properties for file upload class, if added-deleted <_, start or notify
# consider file database for comparisons
# compare file meta data to see if file has been updated, if so, notify

# and command line notifications

import logging

def monitor_files():
    existing_files = set()

    while True:
        files = get_files()

        for file in files:
            file_name = file["filename"]
            file_url = file["url"]

            if file_name not in existing_files:
                notify(file_name)
                download_file(file_url, file_name)
                existing_files.add(file_name)

def log():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )