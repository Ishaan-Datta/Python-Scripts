import snappy  
import sqlite3
import contextlib
import chardet
import re
import os
import shutil
import psutil

db_path = "C:/Users/ishaa/AppData/Roaming/Mozilla/Firefox/Profiles/qn28j8cf.default-release-1714690611274/storage/default/moz-extension+++d682773b-6d15-4715-8bab-7882772506c9^userContextId=4294967295/idb"

def check_firefox():
    for process in psutil.process_iter():
        if process.name() == "firefox.exe":
            return True
    # do something...

def copy_db():
    current_path = os.getcwd()
    os.chdir(db_path)
    shutil.copy2("3647222921wleabcEoxlt-eengsairo.sqlite", "file_copy.sqlite")
    shutil.move("file_copy.sqlite", current_path)
    os.chdir(current_path)

# def decompress_and_save():
#     with sqlite3.connect("file_copy.sqlite") as conn:
#         cursor = conn.cursor()
#         cursor.execute("select object_store_id, key, data from object_data")
#         for row in cursor: 
#             file_name = "{}_{}.bin".format(row[0], row[1].hex())              
#             data = snappy.decompress(row[2])     
#             print("saving", file_name)
#             with open(file_name, "wb") as file:
#                 file.write(data)

def decompress_and_save():
    with contextlib.closing(sqlite3.connect("file_copy.sqlite")) as conn:
        with contextlib.closing(conn.cursor()) as cursor:
            tmp = cursor.execute("select object_store_id, key, data from object_data").fetchall()
            length = len(tmp)
            row = tmp[length-1]
            data = snappy.decompress(row[2])
            with open("tab_data.bin", "wb") as file:
                file.write(data)

def extract_tabs():
    tab_data = {}
    
    with open ("tab_data.bin", "rb") as file:
        binary_data = file.read()
        trimmed = binary_data[binary_data.find(b'{'):]
        
        result = chardet.detect(binary_data)
        encoding = result['encoding']
        decoded = trimmed.decode(encoding)
        
        groupPattern = re.compile('"tabsMeta":\[(.*?)],"')
        tabsPattern = re.compile('"url":"([^"]*)","title":"([^}]*)"')
        
        groups_matches = groupPattern.findall(decoded)
        for index, group in enumerate(groups_matches):
            tabs_matches = tabsPattern.findall(group)
            tab_data[index] = tabs_matches
    
    return tab_data

def write_import_file(tab_data):
    with open("import.txt", "w", encoding="utf-16le") as file:
        for key, value in tab_data.items():
            for tab in value:
                file.write(f"{tab[0]} | {tab[1]}\n")
            file.write("\n")

def clean_up():
    os.remove("file_copy.sqlite")
    os.remove("tab_data.bin")

if __name__ == "__main__":
    copy_db()
    decompress_and_save()
    data = extract_tabs()
    write_import_file(data)
    clean_up()