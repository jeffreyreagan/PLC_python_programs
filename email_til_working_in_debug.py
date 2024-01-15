'''this email script will search specified query and save results in path. Also display plain text, header, to, and from'''



'''client id:1014325386479-4puils02h3tg7crog2v40qapm3akn764.apps.googleusercontent.com         gathered from google api'''
import os
import sys
#pickle used to load and dump token
import pickle
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from mimetypes import guess_type as guess_mime_type
from urllib.parse import quote_from_bytes
#google requests
from google.auth.transport.requests import Request
#Acccess server with appflow after accessing scope and credentials.json
from google_auth_oauthlib.flow import InstalledAppFlow
# Gmail API utils
from googleapiclient.discovery import build
 
SCOPES = ['https://mail.google.com/']
our_email = 'jeffreyreagan02@gmail.com'

'''
First of all, let's make a function that loads the credentials.json, does the authentication with Gmail API and returns a service object 
that can be used later in all of our upcoming functions:'''

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
service = gmail_authenticate()
#testing base64 decoding
import base64


'''This def gathers message list matching the results = search_messages(service, "search here")'''
def search_messages(service, query):
    #result also equals search_messages(service,"example search")
    result = service.users().messages().list(userId='me',q=query).execute()
    labels = result.get('labels', [])
    messages = [ ]
    if not labels:
        print('No labels Found')
    else:
        print('labels:')
        for label in labels:
            print(label['name'])
    #this function moves the first list of messages to 'messages'
    if 'messages' in result:
        messages.extend(result['messages'])
    #this function determines if there is another page of emails to read.
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',q=query, pageToken=page_token).execute()
    #this function moves the following pages of messages to 'messages'
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages


''' the get_size_format() function will just print bytes in a nice format (grabbed from this tutorial), and we gonna need 
the clean() function to make a folder name that doesn't contain spaces and special characters.'''


''''''

# utility functions
def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)






'''Next, let's define a function that parses the content of an email partition:'''
def parse_parts(service, parts, folder_name, message):
    """
    Utility function that parses the content of an email partition
    """
    if parts:
        for part in parts:
            filename = part.get("filename")
            mimeType = part.get("mimeType")
            body = part.get("body")
            data = body.get("data")
            file_size = body.get("size")
            part_headers = part.get("headers")
            print(part_headers())
            if part.get("parts"):
                # recursively call this function when we see that a part
                # has parts inside
                parse_parts(service, part.get("parts"), folder_name, message)         
            if mimeType == "text/plain":
                # if the email part is text plain
                if data:
                    text = urlsafe_b64decode(data).decode()
                    print(text)
                    print("plain  text")
            elif mimeType == "text/html":
                print("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                # if the email part is an HTML content
                # save the HTML file and optionally open it in the browser
                if not filename:
                    filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                print("Saving HTML to", filepath)
                with open(filepath, "wb") as f:
                    f.write(urlsafe_b64decode(data))
                    print("text/html")

            else:
                # attachment other than a plain text or HTML
                for part_header in part_headers:
                    part_header_name = part_header.get("name")
                    part_header_value = part_header.get("value")
                    if part_header_name == "Content-Disposition":
                        if "attachment" in part_header_value:
                            # we get the attachment ID 
                            # and make another request to get the attachment itself
                            print("Saving the file:", filename, "size:", get_size_format(file_size))
                            attachment_id = body.get("attachmentId")
                            attachment = service.users().messages().attachments().get(id=attachment_id, userId='me', messageId=message['id']).execute()
                            data = attachment.get("data")
                            filepath = os.path.join(folder_name, filename)
                            if data:
                                with open(filepath, "wb") as f:
                                    f.write(urlsafe_b64decode(data))
                                    print(" it is getting multi type")


'''Main function for reading emails'''

def read_message(service, message):
    """
    This function takes Gmail API `service` and the given `message_id` and does the following:
        - Downloads the content of the email
        - Prints email basic information (To, From, Subject & Date) and plain/text parts
        - Creates a folder for each email based on the subject
        - Downloads text/html content (if available) and saves it under the folder created as index.html
        - Downloads any file that is attached to the email and saves it in the folder created
    """
    import json
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    # parts can be the message body, or attachments
    payload = msg['payload']
    headers = payload.get("headers")
    parts = payload.get("parts")
    attachments = payload.get("attachments")
    folder_name = "email"
    has_subject = False
    if headers:
        #print real message
        
        print("----------------------------------------------------")
        print(headers)
       
        # this section prints email basic info & creates a folder for the email
        for header in headers:
            #print attachments to terminal if present
            if attachments is True:
                print(attachments)
            '''get header properties'''
            name = header.get("name")
            value = header.get("value")
            til = header.get("data")
            til_value = header.get("value")
            if name.lower() == 'from':
                # we print the From address
                print("From:", value)
            if name.lower() == "to":
                # we print the To address
                print("To:", value)
            if name.lower() == "subject":
                # make our boolean True, the email has "subject"
                has_subject = True
                # make a directory with the name of the subject
                folder_name = clean(value)
                # we will also handle emails with the same subject name
                folder_counter = 0
                while os.path.isdir(folder_name):
                    folder_counter += 1
                    # we have the same folder name, add a number next to it
                    if folder_name[-1].isdigit() and folder_name[-2] == "_":
                        folder_name = f"{folder_name[:-2]}_{folder_counter}"
                    elif folder_name[-2:].isdigit() and folder_name[-3] == "_":
                        folder_name = f"{folder_name[:-3]}_{folder_counter}"
                    else:
                        folder_name = f"{folder_name}_{folder_counter}"
                os.mkdir(folder_name)
                print("Subject:", value)
                print("name", value)
                print("data", value)
            if name.lower() == "date":
                #print the date when the message was sent
                print("Date:", value)
    if not has_subject:
        # if the email does not have a subject, then make a folder with "email" name
        # since folders are created based on subjects
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
    parse_parts(service, parts, folder_name, message)
    print("="*50)


# get emails that match the query specified

results = search_messages(service, 'no-reply@mail.todayilearned.wiki')
print(f"Found {len(results)} results.")
# for each email matched, read it (output plain/text to console & save HTML and attachments)
#msg in read_message def with msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
for msg in results:
    #read_message is def directly above
    read_message(service, msg)

''' leaving off here, can search by keywords above. Returning saved file to python programs folder. Some emails are empty. Looking into decoding the data. All data 
is making it here, just can't format properly to a file or on terminal for certain email types (html/text). '''
