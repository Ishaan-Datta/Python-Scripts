# price updater bot
# store values in excel for varying website prices
# webscraping
# add new title and automatically search and update
# update live website w/ API
# bot script seperate, api calls or headless browser
# inspect element for link source
# update every day udt
# 3d numpy array or pandas dataframes for storing data
# matplotlib visualization of historical data from database
# excel as a reporting dashboard for Python calculationsspreadsheet link with headless browser in search bar instead of id
# game wishlist platforms


#googlesheets base
import gspread # pip install gspread

'''SETUP
- google developer console: https://console.developers.google.com
- new project -> activate drive and sheets api
- credentials -> service account -> name + role=editor
  ->create key and download json
- share client_email fom json in your sheets
'''

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("xxxx") # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1

### retrieve data ###
res = worksheet.get_all_records() # list of dictionaries
res = worksheet.get_all_values() # list of lists
print(res)
print(len(res))

values_list = worksheet.row_values(1)
print(values_list)
values_list = worksheet.col_values(1)
print(values_list)

print(worksheet.row_count, worksheet.col_count)
print(worksheet.get('A1'))
#print(worksheet.get('A1:C1'))

# INSERT UPDATE

user = ["Susan", "28", "Sydney"]
#worksheet.insert_row(user, 3)
#worksheet.insert_row(user, 2) #same with column
#worksheet.append_row(user)
#worksheet.update_cell(1,2, value)

# DELETE
#worksheet.delete_rows(1)
#worksheet.delete_columns(1)

'''
USE THE FOLLOWING IF YOU HAVE THE CREDENTIALS ALREADY LOADED
AND IN JSON FORMAT
import json

from google.oauth2.service_account import (
    Credentials as ServiceAccountCredentials,
)

DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

creds = ServiceAccountCredentials.from_service_account_info(credentials, scopes=DEFAULT_SCOPES)
gc = gspread.Client(auth=creds)
'''

#price tracker base:
import unicodedata

(use beautiful soup to get price for given item)

price = unicodedata.normalize("NFKD", price_str)
(remove characters)
price = float(price)

if __name__ == '__main__':
    url = "https://www.amazon.com/Samsung-Factory-Unlocked-Smartphone-Pro-Grade/dp/B08FYTSXGQ/ref=sr_1_1_sspa?dchild=1&keywords=samsung%2Bs20&qid=1602529762&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOTdFSllWVkhNMFRFJmVuY3J5cHRlZElkPUEwNDAyODczMktKMDdSVkVHSlA2WCZlbmNyeXB0ZWRBZElkPUEwOTc5NTcxM1ZXRlJBU1k1U0ZUSyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    products = [(url, 700)]
    
    products_below_limit = []
    for product_url, limit in products:
        title, price, available = get_product_info(product_url)
        if title is not None and price < limit and available:
            products_below_limit.append((url, title, price))


    if products_below_limit:
        message = "Subject: Price below limit!\n\n"
        message += "Your tracked products are below the given limit!\n\n"
        
        for url, title, price in products_below_limit:
            message += f"{title}\n"
            message += f"Price: {price}\n"
            message += f"{url}\n\n"
        
        send_email(message)

# games list:
# for game list, check duplicates, string split into words, under same entry, if word of length > 3 is in two different titles, declare as possible duplicate
# price tracking