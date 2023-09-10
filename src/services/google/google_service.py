import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from src.configs.env.env import Env

def getCredentials():
    creds = None

    if os.path.exists(os.path.join(Env.googleCredentialsBaseDir, "token.json")):
        creds = Credentials.from_authorized_user_file(os.path.join(Env.googleCredentialsBaseDir, "token.json"), Env.googleScopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join(Env.googleCredentialsBaseDir, "credentials.json"), Env.googleScopes)
            creds = flow.run_local_server(port=0)

        with open(os.path.join(Env.googleCredentialsBaseDir, "token.json"), "w") as token:
            token.write(creds.to_json())

    return creds
