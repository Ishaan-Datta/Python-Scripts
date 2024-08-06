# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

import os
import pickle
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/tasks']

def authenticate():
    """Shows basic usage of the Tasks API.
    Lists the user's task lists.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def get_tasks(service, tasklist_id):
    """Get all tasks from the specified task list."""
    tasks = []
    page_token = None
    while True:
        result = service.tasks().list(tasklist=tasklist_id, pageToken=page_token).execute()
        tasks.extend(result.get('items', []))
        page_token = result.get('nextPageToken')
        if not page_token:
            break
    return tasks

def delete_task(service, tasklist_id, task_id):
    """Delete a task from the specified task list."""
    service.tasks().delete(tasklist=tasklist_id, task=task_id).execute()

def main():
    # Authenticate and build the service
    creds = authenticate()
    service = build('tasks', 'v1', credentials=creds)

    # Specify the task list ID
    tasklist_id = 'YOUR_TASKLIST_ID'

    # Get tasks
    tasks = get_tasks(service, tasklist_id)
    
    # Write tasks to a text file
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(f"Task: {task['title']}\n")
            f.write(f"Due: {task.get('due', 'No due date')}\n")
            f.write(f"Notes: {task.get('notes', 'No notes')}\n")
            f.write("\n")

    # Delete tasks
    for task in tasks:
        delete_task(service, tasklist_id, task['id'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py YOUR_TASKLIST_ID")
    else:
        main()


# Ensure you have credentials.json (downloaded from the Google Cloud Console).
# python google_tasks.py YOUR_TASKLIST_ID

# Set Up Google Cloud Project and Enable API Access:

#     Create a new project in the Google Cloud Console.
#     Enable the Google Tasks API for your project.
#     Set up OAuth 2.0 credentials (specifically, you need OAuth 2.0 Client IDs).