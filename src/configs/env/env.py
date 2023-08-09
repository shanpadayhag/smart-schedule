import os

from dotenv import load_dotenv

load_dotenv()

class Env:
    googleCalendarId: str
    googleCredentialsBaseDir: str
    notionSecretKey: str
    notionDatabaseTaskId: str
    notionDatabaseProjectsId: str

    def __init__(self) -> None:
        self.googleCalendarId           = os.environ.get("NOTION_SECRET_KEY") or ''
        self.googleCredentialsBaseDir   = os.environ.get("GOOGLE_CREDENTIALS_BASE_DIR") or ''
        self.notionSecretKey            = os.environ.get("NOTION_SECRET_KEY") or ''
        self.notionDatabaseTaskId       = os.environ.get("NOTION_DATABASE_TASK_ID") or ''
        self.notionDatabaseProjectsId   = os.environ.get("NOTION_DATABASE_PROJECTS_ID") or ''
