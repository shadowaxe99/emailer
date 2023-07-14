from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import email
import re
import os
import pickle

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def fetch_latest_email():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
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

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    message = results.get('messages', [])

    if not message:
        print('No new messages.')
    else:
        message = message[0]
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        email_data = msg['payload']['headers']
        for values in email_data:
            name = values['name']
            if name == 'From':
                from_name = values['value']
                for part in msg['payload']['parts']:
                    mime_type = part['mimeType']
                    if mime_type == 'text/plain':
                        # email text
                        data = part['body']["data"]
                        data = data.replace("-","+").replace("_","/")
                        decoded_data = base64.b64decode(data)
                        temp = str(decoded_data, "utf-8")
                        data = temp

        print(f'From: {from_name}, Message: {data}')

if __name__ == '__main__':
    fetch_latest_email()