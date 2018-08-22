"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

# Call the Gmail API
results = service.users().messages().list(userId="me",maxResults=1,q="Monica Dugan").execute()
#print (results)
messages = results.get('messages', [])
if not messages:
	print('No messages found.')
else:
    for message in messages:
        msg_id = message['id']
	#body = message['body']

msg = service.users().messages().get(userId="me",id='164b9d62b076f1f5').execute()
mimeparts = msg['payload']['parts']
print(len(mimeparts))
with open('MessageBody.txt','w') as wfp:
    for mimetps in mimeparts:
        if mimetps['mimeType'] == 'multipart/alternative':
            for part in mimetps['parts']:
                if part['mimeType'] == 'text/plain':
                    print('Body size', part['body']['size'])
                    if part['body']['size'] > 0:
                        if part['body'].get('data'):
                            wfp.write(base64.urlsafe_b64decode(part['body']['data'].encode('ASCII')))
    wfp.close()
#        print (base64.urlsafe_b64decode(part['body']['data'].encode('ASCII')))
	
#print(base64.urlsafe_b64decode(msg['payload']['body']['data'].encode('ASCII')))
