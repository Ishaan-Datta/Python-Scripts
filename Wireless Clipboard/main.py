# Clipboard to share text between computers
# pages for what technology used and methodoloy
# tkinter gui
# https server
# password and unique computer identifier
# include images, text, file paths


def clipboard_copy():
    pyautogui.hotkey("ctrl", "c")
    password = clipboard.paste()
    print("The password has been copied to your clipboard")


# same technology for onetab sync app
# notification for duplicate onetab and bookmark extensions modification
# For program that bookmarks onetabs/open tabs: use requests module to request browser tab name from website, plug into name w/ url
# have global hotkey detection for ditto clone
