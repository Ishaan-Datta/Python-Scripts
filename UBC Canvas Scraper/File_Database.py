import os

# add functionality to pickup meta data from files, compare to existing files, if different, notify
def check_existing(course_name):
    file_list = []
    path = "C:/Users/ishaa/OneDrive - UBC/Resources/3rd Year" + "/" + course_name
    # alternate for vancouver desktop
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_list.append(file)
    return file_list

# need date time, pandas dataframe and csv for file metadata
# store as file in database, include file name, date modifed