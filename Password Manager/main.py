import psycopg2
from hashlib import sha256
import pyautogui
import clipboard

def create_db():
    # design schema with what is null, what isnt, id primary key, joining queries
    pass

def login():
    # terminal in postgres? -> \c password manager, connected 
    # to database password_manager as user postgres, \dt, \l, select * from accounts;
    password = input("Please enter the master password: ")
    # if successful access menu
    try:
        connection = psycopg2.connect(
            user="kalle",
            password="kalle",
            host="127.0.0.1",
            database="password manager",
        )
    except (Exception, psycopg2.Error) as error:
        print(error)
        
    return connection

def menu():
    key = input("Please enter a key to access the following options")
    #add password for app/site
    #generate password for app/site
    #find sites/apps connected to email
    #find password for for site/app
    # exit
    #display table print module

def encrypt():
    pass

def decrypt():
    pass

def find_password(app_name, admin_pass):
    #search by username, email, url, app name
    #unhash before printing
    try:
        cursor = connection.cursor
        postgres_select query = """"""
        cursor.execute(query, app_name)
        connection.commit
        result = cursor.fetchone
        # print
    except (Exception, psycopg2.Error) as error:
        print(error)
    # password | email | username | url | app_name
    #display table print module
    # conneciton = connect()

def add_password(service, admin_pass):
    #try and except blocks ot ensure proper format is being stored
    password = input("Please provide the password for this site: ")
    site_app_name = input("Please provide the name of the app or site you want to create a password for: ")
    email = input("Please provide the email you used for this site: ")
    username = input("Please provide the username used if applicable")
    url = input("Please provide the url of the website: ")
    
    secret_key = get_hex_key(admin_pass, service)
    command = "insert into keys (pass_key) values secret_key"
    conn.execute(command)
    conn.commit()

    #basically hashing password entered with the master password, that gets inputted into db, when pulled out is is decoded
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (
            "password123",
            "kalle@email.com",
            "kalle",
            "https://kalletech.com/",
            "kalletech",
        )
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount()
        print(count, "record inserted")
        return create_password(secret_key, service, admin_pass)
    except:
        pass
    
    #success message for store

def update_password():
    #encrypt/hash
    #success message for udpate
    #verify record exists in table
    pass

def clipboard_copy():
    pyautogui.hotkey("ctrl", "c")
    password = clipboard.paste()
    print("The password has been copied to your clipboard")

# create basic terminal interface
# later modify to host on webserver to access from phone/etc.
# downloading and installing dependencies automatically including posgres


# SQL database, open/store files as well, pseudo cloud storage
# list all subdirectories and files within them
# add to shell script to run it from anywhere
# database API and run local webserver ot host database/API on
# app sends request to API which translates into database query to fetch name
# tagging system for finding files faster
# using python libraries to manipulate database (not direct SQL injection)
# build searchbar UI or command line text interface to interact (CLI)
# synchronize system reminders here
# onetab google sync support
# later learn how to display data on a webpage w/ html and css


def create_db():
    pass


def add_items():
    # add new data into table
    pass


def update_items():
    pass


def download_items():
    pass


def remove_items():
    pass


# if input == 's'
# path = raw_input(Type full path of where you want to store file)

# with open(file, 'wb') as f_output:
#     f_output.write(base64.b64decode(file_string))

# splitting file_name = path.split(/)

# image = cv2.imread(path)
# file_string = base64.b64encode(cv2.imencode(args))

# command = "INSERT INTO SAFE (FULL_NAME, NAME, EXTENSION, FILES) VALUES (%s, %s, %s, %s); $(file_name, ...)
# conn.execute(command)
# conn.commit()

# with connection?

# recursive file checker code
