import os

path = "C:/Users/ishaa/OneDrive - UBC/Coding"
master_directory = {}

print(" ")
for dirpath, dirnames, filenames in os.walk(path):
    count = dirpath.count("\\")
    string = "-" * count * 2
    basename = os.path.basename(dirpath)
    print(string + basename)

    master_directory[dirpath] = filenames
    for file in master_directory[dirpath]:
        count = dirpath.count("\\") + 1
        string = "-" * count * 2
        print(string + file)
