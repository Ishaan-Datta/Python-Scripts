# https://developers.google.com/calendar/quickstart/python
# press the "ENABLE THE GOOGLE CALENDAR API" to activate it.
# download popup with a file called credentials.json

import datetime, pickle, os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


class EventTask:
    def __init__(self, name, start_time, end_time, color):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.color = color
        self.duration = str((self.end_time - self.start_time).total_seconds())


credentials = None

# token.pickle stores user's credentials from previously sucessful logins
if os.path.exists("token.pickle"):
    print("Loading credentials from file...")
    with open("token.pickle", "rb") as token:
        credentials = pickle.load(token)

# if no valid credentials, either refresh w/ token or log in
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print("Refreshing access token...")
        credentials.refresh(Request())
    else:
        print("Fetching new tokens...")
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file="C:/Users/ishaa/OneDrive - UBC/Coding/Unfinished/Python Tutorials/client_secrets.json",  # change this secrets file path/add project etc.
            scopes=[
                "https://www.googleapis.com/auth/youtube.readonly"  # change scopes
            ],
        )

        flow.run_local_server(
            port=8080, prompt="consent", authorization_prompt_message=""
        )  # prompt consent makes server give refresh token everytime script runs
        credentials = flow.credentials
        print(credentials.to_json())

        # save credentials for next run:
        with open("token.pickle", "wb") as f:
            print("Saving credentials for future use...")
            pickle.dump(credentials, f)

# calculate and sum time planned to be spent for this week
# for blank activity: you have planned to spend 7.0 hours this week
# find duration of each task, add into list
service = build("calendar", "v3", credentials=credentials)
request = service.events().list(calendar=, maxresults=, orderby=) #get events for this week, color, 
)
response = request.execute()
print(response)

for item in response['items']:
    if not response:
        print("no upcoming events")
    for event in response:
        start = event['start'].get('dateTime', 'event')
        end = event['end'].get('dateTime', 'event')
        print(start, end, event['summary'])

def sessions_number(start_date):
    pass
    #request to count number of workout sessions completed up to today
    #break into legs, chest, etc.