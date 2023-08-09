import os

from dotenv import load_dotenv

load_dotenv()

class Env:
    googleCalendarId            = os.environ.get("GOOGLE_CALENDAR_ID") or ''
    googleCredentialsBaseDir    = os.environ.get("GOOGLE_CREDENTIALS_BASE_DIR") or ''
    notionSecretKey             = os.environ.get("NOTION_SECRET_KEY") or ''
    notionDatabaseTaskId        = os.environ.get("NOTION_DATABASE_TASK_ID") or ''
    notionDatabaseProjectsId    = os.environ.get("NOTION_DATABASE_PROJECTS_ID") or ''
