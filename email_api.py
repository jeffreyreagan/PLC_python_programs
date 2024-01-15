import os
import pickle
from base64 import urlsafe_b64decode
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define constants
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
OUR_EMAIL = 'jeffreyreagan02@gmail.com'

def gmail_authenticate():
    """Authenticate with Gmail API and return the service object."""
    creds = None
    token_path = Path("token.pickle")

    # Load existing credentials if available
    if token_path.exists():
        with token_path.open("rb") as token:
            creds = pickle.load(token)

    # If there are no valid credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_1014325386479-4puils02h3tg7crog2v40qapm3akn764.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with token_path.open("wb") as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def search_messages(service, query):
    """Search for messages matching the given query."""
    result = service.users().messages().list(userId='me', q=query).execute()
    messages = result.get('messages', [])

    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
        messages.extend(result.get('messages', []))

    return messages

def parse_parts(service, parts, folder_path, message_id):
    """Parse the content of email partitions."""
    for part in parts:
        filename = part.get('filename')
        mimeType = part.get('mimeType')
        body = part.get('body')
        data = body.get('data')
        file_size = body.get('size')

        if part.get('parts'):
            parse_parts(service, part.get('parts'), folder_path, message_id)

        if mimeType == 'text/plain':
            if data:
                text = urlsafe_b64decode(data).decode()
                print(text)
                print("plain text")

        elif mimeType == 'text/html':
            if not filename:
                filename = 'index.html'
            filepath = folder_path / filename
            print(f"Saving HTML to {filepath}")
            with filepath.open('wb') as f:
                f.write(urlsafe_b64decode(data))
                print("text/html")

        else:
            for part_header in part.get('headers', []):
                part_header_name = part_header.get('name')
                part_header_value = part_header.get('value')

                if part_header_name == 'Content-Disposition' and 'attachment' in part_header_value:
                    print(f"Saving the file: {filename}, size: {file_size}")
                    attachment_id = body.get('attachmentId')
                    attachment = service.users().messages().attachments().get(
                        id=attachment_id, userId='me', messageId=message_id
                    ).execute()
                    attachment_data = attachment.get('data')
                    filepath = folder_path / filename

                    if attachment_data:
                        with filepath.open('wb') as f:
                            f.write(urlsafe_b64decode(attachment_data))
                            print("it is getting multi type")

def read_message(service, message):
    """Read and process the content of an email."""
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    payload = msg.get('payload', {})
    headers = payload.get('headers', [])
    parts = payload.get('parts', [])
    folder_name = "email"

    for header in headers:
        name = header.get('name')
        value = header.get('value')

        if name.lower() == 'from':
            print(f"From: {value}")
        elif name.lower() == 'to':
            print(f"To: {value}")
        elif name.lower() == 'subject':
            folder_name = clean(value)
            print(f"Subject: {value}")
            print(f"Folder Name: {folder_name}")
            folder_path = Path(folder_name)
            folder_path.mkdir(exist_ok=True)
        elif name.lower() == 'date':
            print(f"Date: {value}")

    parse_parts(service, parts, folder_path, message['id'])
    print("=" * 50)

def clean(text):
    """Clean text for creating a folder."""
    return "".join(c if c.isalnum() else "_" for c in text)

def main():
    service = gmail_authenticate()
    #edit this query for a senders email
    results = search_messages(service, query= any)
    print(f"Found {len(results)} results.")

    for msg in results:
        read_message(service, msg)

if __name__ == "__main__":
    main()
