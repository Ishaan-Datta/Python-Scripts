"Uses webscraping and the Canvas API to automatically download course content" 
# execute every 10 seconds

# if new file added, move files, create subfolders with date as name, if not exists, move it
# should not rename files unless file already exists, then notify duplicate and rename, not appending to file extension
# run in background
# design for canvas
# notifications for when file has been uploaded, moved successfuly, potential update, change, mistake by prof

# make seperate folder within downloadsd to watch
# Module for locating file directory and changing to that before module starts looking in it (need if __name__ == __main__)

# # f = Path(file)

# # create directory
# Path("data").mkdir(exist_ok=True)

# # or
# if not os.path.exists("data"):
#     os.mkdir("data")

# # move file and folder
# shutil.move("f", "d")  # works for file and folder

# # copy file and folder
# shutil.copy("src", "dest")
# shutil.copy2("src", "dest")

# # remove file and folder
# os.remove("filename")  # error if not found
# os.rmdir("folder")  # error if not empty, or not found
# shutil.rmtree("folder")  # works for non empty directories

FileSystemEventHandler: Base file system event handler that you can override methods from.
PatternMatchingEventHandler: Matches given patterns with file paths associated with occurring events.
RegexMatchingEventHandler: Matches given regexes with file paths associated with occurring events.
LoggingEventHandler: Logs all the events captured.

we can override as the other remaining classes inherits from FileSystemEventHandler

on_any_event(event)
on_created(event)
on_deleted(event)
on_modified(event)

For each of the functions, it will have an input parameter called event which contains the following variables:
event_type — The type of the event as a string. Default to None.
is_directory — True if event was emitted for a directory; False otherwise.
src_path — Source path of the file system object that triggered this event.