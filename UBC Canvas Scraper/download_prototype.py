import requests, shutil, os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

file_url =  'https://canvas.ubc.ca/files/30845374/download?download_frd=1'
file_page = 'https://canvas.ubc.ca/api/v1/courses/135127/files/30845374'
file_name = '333_0_intro.pdf'
course_name = 'CPEN 333B'
firefox_profile_path = '/path/to/your/firefox/profile'

headers = {
    "Authorization": "Bearer 11224~mlkX4ksmPJcY2krFsnjUAjJ8lWBCl14w27LTq4g0J4tm5nDw2wOiIsIfXsDDKGnM"
}

DOWNLOAD_DIR = str(Path.home() / "Downloads")
# COURSE_DIR = str(Path.home() / "OneDrive - UBC/Resources/3rd Year")

# response = requests.get(file_url, headers=headers)
# print(response.content)

# # with open(Path(DOWNLOAD_DIR) / file_name, "wb") as file:
#     # file.write(response.content)
#     # print("downloaded")
    
# course_dir = Path(COURSE_DIR) / course_name
# # shutil.move(Path(DOWNLOAD_DIR) / file_name, Path(course_dir) / file_name)


options = Options()
options.set_preference("browser.download.folderList", 2)  # Use for custom location
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", DOWNLOAD_DIR)  # Set your path
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # MIME Type

profile = FirefoxProfile(firefox_profile_path)
driver = webdriver.Firefox(firefox_profile=profile, options=options)

driver.get('file_page')
download_link = driver.find_element(By.XPATH, '//a[contains(@href, "download?download_frd=1")]')
download_link.click()

# logging