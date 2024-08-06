from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
import psutil
import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

profile_path = "C:/Users/ishaa/AppData/Roaming/Mozilla/Firefox/Profiles/qn28j8cf.default-release-1714690611274"
import_path = "C:/Users/ishaa/Personal Folder/Tabs Sync/import.txt"
export_path = "C:/Users/ishaa/Personal Folder/Tabs Backup"
importURL = "moz-extension://d682773b-6d15-4715-8bab-7882772506c9/import-export.html"
tabsURL = "moz-extension://d682773b-6d15-4715-8bab-7882772506c9/onetab.html"
cycleTrigger = False

class FileWatcher(FileSystemEventHandler):
    def __init__(self, file_name, callback):
        self.file_name = file_name
        self.callback = callback

    def on_created(self, event):
        if event.src_path.endswith(self.file_name):
            self.callback()

def watch_directory(directory, file_name, callback):
    event_handler = FileWatcher(file_name, callback)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    
    try:
        while True:
            sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def callback():
    print("File created")
    global cycleTrigger
    cycleTrigger = True
    while cycleTrigger:
        check_firefox()
        sleep(5)

def check_firefox():
    global cycleTrigger
    for process in psutil.process_iter():
        if process.name() == "firefox.exe":
            return True
    cycleTrigger = False
    update_tabs()

def delete_old_tabs(driver):
    driver.get(tabsURL)
    elements = WebDriverWait(driver, 10, 0.01).until(lambda x: x.find_elements(By.CLASS_NAME, 'clickable.deleteAllButton')) 
    for element in elements:
        element.click()
        WebDriverWait(driver, 10, 0.01).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    return

def import_new_tabs(driver, tabs):
    driver.get(importURL)
    import_expand = WebDriverWait(driver, 10, 0.01).until(lambda x: x.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/img")) 
    import_expand.click()
    textarea = WebDriverWait(driver, 10, 0.01).until(lambda x: x.find_element(By.CSS_SELECTOR, "#contentAreaDiv > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(2)"))
    driver.execute_script("arguments[0].value = arguments[1];", textarea, tabs)
    sleep(0.05)
    import_button = WebDriverWait(driver, 10, 0.01).until(lambda x: x.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/div[2]/span"))
    import_button.click()
    return

def update_tabs():
    options = Options()
    options.add_argument(f"--profile {profile_path}")
    options.add_argument("--headless")
    
    driver = webdriver.Firefox(options=options)
    driver.get(importURL)
    
    textarea = WebDriverWait(driver, 10, 0.01).until(lambda x: x.find_element(By.CSS_SELECTOR, "#contentAreaDiv > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(2)"))
    text_value = driver.execute_script("return arguments[0].value;", textarea)
    
    os.chdir(export_path)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open(f"{time}.txt" , "w", encoding="utf-16le") as file:
        file.write(text_value)
        
    data = ""
    with open (import_path, "r") as file:
        data = file.read()
    os.remove(import_path)

    first_section = text_value.split("\n\n")[0]
    tabs = first_section + "\n\n" + data
    
    delete_old_tabs(driver)
    import_new_tabs(driver, tabs)

    driver.quit()
    return

if __name__ == "__main__":
    watch_directory("C:/Users/ishaa/Personal Folder/Tabs Sync", "import.txt", callback)