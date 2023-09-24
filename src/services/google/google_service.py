import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from src.configs.env.env import Env

def getCredentials():
    credentials = None
    tokenFullPath = os.path.join(Env.googleCredentialsBaseDir, "token.json")
    credentialsFullPath = os.path.join(Env.googleCredentialsBaseDir, "credentials.json")

    if os.path.exists(tokenFullPath):
        credentials = Credentials.from_authorized_user_file(tokenFullPath, Env.googleScopes)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentialsFullPath, Env.googleScopes)
            credentials = flow.run_local_server(port=0)

        with open(tokenFullPath, "w") as token:
            token.write(credentials.to_json())

    return credentials

def calendarService():
    googleCredentials = getCredentials()
    return build(
        serviceName='calendar', 
        version='v3',
        credentials=googleCredentials
    )
