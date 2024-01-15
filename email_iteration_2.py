from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import datetime
from base64 import urlsafe_b64decode
from google.auth.transport.requests import Request 
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret_1014325386479-cpjuvdg33k0kpkpc79qug1oorn778fpe.apps.googleusercontent.com.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def search_messages(service, query):
    result = service.users().messages().list(userId='me', q=query).execute()
    messages = []
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def parse_parts(service, parts, folder_name, message, search_title):
    if parts:
        for part in parts:
            filename = part.get("filename")
            mimeType = part.get("mimeType")
            body = part.get("body")
            data = body.get("data")
            file_size = body.get("size")
            part_headers = part.get("headers")
            if part.get("parts"):
                parse_parts(service, part.get("parts"), folder_name, message, search_title)
            if mimeType == "text/plain":
                if data:
                    text = urlsafe_b64decode(data).decode()
                    print(text)
            elif mimeType == "text/html":
                if not filename:
                    filename = "index.html"
                filepath = os.path.join(folder_name, f"{search_title}_{filename}")
                with open(filepath, "wb") as f:
                    f.write(urlsafe_b64decode(data))
            else:
                for part_header in part_headers:
                    part_header_name = part_header.get("name")
                    part_header_value = part_header.get("value")
                    if part_header_name == "Content-Disposition":
                        if "attachment" in part_header_value:
                            print("Saving the file:", filename, "size:", file_size)
                            attachment_id = body.get("attachmentId")
                            attachment = service.users().messages().attachments().get(
                                id=attachment_id, userId='me', messageId=message['id']
                            ).execute()
                            data = attachment.get("data")
                            filepath = os.path.join(folder_name, f"{search_title}_{filename}")
                            if data:
                                with open(filepath, "wb") as f:
                                    f.write(urlsafe_b64decode(data))

def read_message(service, message, folder_path, search_title):
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    payload = msg['payload']
    parts = payload.get("parts")
    parse_parts(service, parts, folder_path, message, search_title)

def main():
    service = authenticate()
    
    while True:
        search_query = input("Enter search query (or 'exit' to quit): ")
        if search_query.lower() == 'exit':
            break
        
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        search_title = search_query.replace(" ", "_")  # Convert spaces to underscores
        folder_path = os.path.join(os.getcwd(), current_date, search_title)
        os.makedirs(folder_path, exist_ok=True)
        
        results = search_messages(service, search_query)
        print(f"Found {len(results)} results.")
        
        for msg in results:
            read_message(service, msg, folder_path, search_title)
            print("="*50)

if __name__ == "__main__":
    main()