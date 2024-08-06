# pip install gspread oauth2client requests

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# Constants
SHEET_NAME = "games list"
ITA_API_URL = "https://api.isthereanydeal.com/v01/price/"
CREDENTIALS_FILE = 'credentials.json'

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open(SHEET_NAME).sheet1

# Get the list of games from the sheet
games = sheet.col_values(1)  # Assuming games are listed in the first column

# Function to get prices from IsThereAnyDeal API
def get_price(game_name):
    response = requests.get(ITA_API_URL, params={'key': 'YOUR_API_KEY', 'q': game_name})
    data = response.json()
    if data['data']['list']:
        # Extract price from the response, this is a placeholder. Adjust according to actual API response.
        return data['data']['list'][0]['price']
    return "N/A"

# Update the Google Sheet with prices
for i, game in enumerate(games, start=1):
    price = get_price(game)
    # Assuming the price column is the second column
    sheet.update_cell(i, 2, price)

print("Prices updated successfully.")
