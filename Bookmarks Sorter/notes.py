# most recent folder = folder you are within, include indent for subfolder information, when </p>, remove subfolder
# just need logic for when hit </p> move back one, dont worry about indents, when new folder declared, everything inside it put into it
# if not line, break
# lines = file.readlines()  # [line_start]
# for line in lines:
#     if detecting_stop(line, indent):
#         line_bookmarks, line_folders = filtering_elements(line, indent)
#         bookmarks = bookmarks + line_bookmarks
#         folders = folders + line_folders
# need to input trimmed file that specifies indent to search and stop at next subfolder to walk through next time
# logic for setting up parent path
# boolean for within based on <DL><p>?
# firstly master_folder is broken, indent level is fucked up, bookmarks are indented 1 level deeper than levels remember
# fix printing, cant handle this many strings in list being printed all at once
# not sure why it wont start reading from file again, in folder logic doesnt work, print where it stops and what it does after
# maybe play with loop order, should only start reading lines if you are still in the folder
# def need to play with conditional order, should check line_indent level in different place, start at level 1 and debug down
# Recording number of folders yielded, add subdirectory folders into count for while loop
# Start index where folder name appears, index until the stop sign, input folder name in gen
# managing initial bookmarks bar folder might not be necessary? unless mobile bookmarks and other bookmarks folders are also a thing,
# remake test file with less bokkmarks, more subs, sounts

# for master_folder, subfolders, bookmarks, indent in bookmark_generator(
#     file, indent_level, path, 1
# ):
#     print(master_folder)
#     print(subfolders)
#     print(bookmarks)
#     print(indent)
# if cant get csv bookmark format, just rewrite netscape format
# know rules like after h3 there is DLP tag
# indents directly correlate to nesting
# if folder has less indents, not within folder, add DLP end tag
# export requirements.txt and actually make pipenv
# copy code and makre comparison to what was loaded earlier
# two bookmarks per folder
# need to know what is detected
# in recursive generator statement call index+1
# could remove if string split by - gives same name as domain name like stack overflow
# if line_indent_level == indent_level:
#     print(line)
#     line_bookmarks, line_folders = filtering_elements(line)
#     bookmarks = bookmarks + line_bookmarks
#     folders = folders + line_folders

# # managing subfolder recursion
# bookmarks.clear()
# if folders:
# for subfolder in folders:
#     new_path = path + "/" + subfolder
#     yield from bookmark_generator(file, indent + 1, new_path, 1)


# def detecting_stop(line, indent_level):
# if line.count("</DL><p>"):
# print("works")
# line_indent_level = line.count("    ")
# if line_indent_level == indent_level - 1:
# if line.count("</DL><p>"):
#     print("works")
#     return False
# return True
# generator yield statment format here: current folder path, folders inside, bookmarks inside
# if there are sub folders, should handle indentation detection accordingly and search each one with logic
# need to play with loop formatting, generator might be the play, cant work well with while True loop
# end goal is to put these into pandas datasheet, just record them in order, name, date, url, indent level, can recreate files

# determining if video links are dead and notifying (channel deleted, etc.)
# If row below has more indent then insert tag
# Folder is whatever is 1 indent level above with h3
# Can decide <DL><p> tags based on indent change
# Copy initial garbage as header info for reprinting

# dynamic menu to add bookmarks w/ keywords to folder, highlight conflicting titles for manual resolve
# dynamic tag system, give it keyword which forces it to go into certain folder, bookmark extension check if exists before adding

# after declaring duplicates, process for selection, just join the lines w/ proper syntax and then locate/delete line from file?
# domain + extension matter
# option to replace such as nhentai.to to .net or luscious or
# exact match and similarity match are separate
# split url link for keywords in domain, check similarity if main branch is similar enough and end garbage character length is small or less relevant
# might as well just create master db for bookmarks, delete in place on file

# assuming preliminary cleaning has been finished, sorted by domain, duplicate search first with pandas, sub dataframes with pandas by folder?
# create handler function to manage pairs of url or title with indexing, for i check everything above and below i
# for potential matches based on similarity, use yt-dl to verify they are the same, get video title, duration etc.
# then use multiprocessing to check for similarities in urls and titles at same time iwthin folders then ignore folders
# use regex to get the end of the url after the domain garbage

# logic first to sort into folders based on domain after clean up and duplicate check, then similarity check

# string split on "-" strip and first part is title
# don’t match cases
# after parsing domain, if in thing, ignore
# ignore playlists
# list=???
# open db when browsing, when bookmarking, extension steps in to make sure url or title isnt identical
# notice for bookark domains that have a large number that werent sorted into folders
# if two strings match similarity index, try substring and pick the shorter one
# permutations, dont make duplicate comparison between bookmark indexes ex. 1-2 and 2-1 for simlarity check
# string split by space and check for common single words like watch or 1080P, HD, brand names
# server to host bookmark access html server
# random selector to open from folder or normal tap/click to open multiple things button to open after clicking all
# library for inactive or removed accounts, instagram account archiving
# quiteaplaylist.com -> to find titles of old youtube videos if we find privated video -> chrome extension to override default YouTube message and display videos
# script to check if websites are still alive, record failures, if 3 in a row over last 6 months, then website is down, alert
# verify and archive inactive youtube channels with api
# dynamic filter system for sort domains, can have menu and associate domains with different folders
