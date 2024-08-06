# PostgreSQL and MySQL databases on CentOS
# -> PostgreSQL for time tracker app to read/write w/ graphQL


import datetime
import time
import os

import pandas as pd

import win32gui as w
from pywinauto import Application

from pynput import keyboard, mouse
import tldextract

last_input = time.time()
original_window = "None"
window_start = time.time()

os.chdir(os.path.dirname(os.path.realpath(__file__)))


# returns website domain or window name, updates application active to current time
def record_window_activity():
    full_window_name = w.GetWindowText(w.GetForegroundWindow())
    print(full_window_name)
    application_name = full_window_name.split(" - ")[-1]
    print(application_name)

    if application_name == "Google Chrome":
        app = Application(backend="uia")
        app.connect(title_re=".*Chrome.*")
        element_name = "Address and search bar"
        dlg = app.top_window()
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
        print(url)
        extracted = tldextract.extract(url)
        domain = extracted.domain + "." + extracted.suffix
        print(domain)
        return domain
    else:
        return application_name


# determines if window or website has been swapped and changes original window if true
def windows_swapped():
    global original_window
    old_window = original_window
    current_window = record_window_activity()

    if original_window != current_window:
        original_window = current_window
        return True, old_window

    else:
        return False, old_window


# creates new file for the year if none exists
def check_file():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = f"activites_{datetime.date.today().year}.csv"
    if file_name not in os.listdir(file_dir):
        return False, file_name
    return True, file_name


# determines if daily activity entry already exists, updates or adds new entry
def update_daily(dataframe, data):
    criterion1 = dataframe["activity_name"].map(lambda x: x == data["activity_name"])
    criterion2 = dataframe["date"].map(lambda x: x == data["date"])
    if dataframe[criterion1 & criterion2].empty:
        dataframe = dataframe.append(data, ignore_index=True)
    else:
        dataframe.loc[criterion1 & criterion2, "duration"] = float(
            dataframe.loc[criterion1 & criterion2, "duration"]
        ) + float(data["duration"])


def update_file(activity):
    file_exists, file_name = check_file()
    data = {
        "activity_name": activity["name"],
        "date": activity["event_date"],
        "duration": activity["duration"],
    }
    if file_exists:
        dataframe = pd.read_csv(file_name)
        update_daily(dataframe, data)
    else:
        dataframe = pd.DataFrame(data, index=[0])
        with open(file_name, "w") as csv_file:
            dataframe.to_csv(csv_file, sep=",", index=False, encoding="utf-8")


def activation():
    global last_input
    global window_start
    difference = time.time() - last_input
    print(difference)
    if difference > 120:
        print("afk detected")
    else:
        # if windows are swapped, want to take the old one and record it
        swapped, application_domain = windows_swapped()
        if swapped:
            activity = {
                "name": f"{application_domain}",
                "duration": f"{str(round((time.time() - window_start),2))}",
                "event_date": str(datetime.date.today()),
            }
            update_file(activity)
            window_start = time.time()
    last_input = time.time()


def on_release(key):
    activation()


def on_click(x, y, button, pressed):
    activation()


def initiliazation():
    listener = keyboard.Listener(on_release=on_release)
    listener.start()

    listener1 = mouse.Listener(on_click=on_click)
    listener1.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()
        listener1.stop()


initiliazation()

# time tracker if app or tab is playing sound
# chrome adnd mozilla firefox dertectionm
# desktop time tracker w/ UI, graph of data summary w/ seaborn
