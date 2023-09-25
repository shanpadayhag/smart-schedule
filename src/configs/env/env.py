
import os

from ast import literal_eval
from dotenv import load_dotenv

load_dotenv()

class Env:
    appTimeZone                 = os.environ.get('APP_TIMEZONE') or 'UTC'
    workingHours                = literal_eval(os.environ.get('WORKING_HOURS'))
    googleCalendarId            = os.environ.get("GOOGLE_CALENDAR_ID") or 'primary'
    googleCredentialsBaseDir    = os.environ.get("GOOGLE_CREDENTIALS_BASE_DIR") or ''
    googleScopes                = ["https://www.googleapis.com/auth/calendar"]
    notionSecretKey             = os.environ.get("NOTION_SECRET_KEY") or ''
    notionDatabaseTaskId        = os.environ.get("NOTION_DATABASE_TASK_ID") or ''
    notionDatabaseProjectsId    = os.environ.get("NOTION_DATABASE_PROJECTS_ID") or ''
    notionPageSize              = int(os.environ.get('NOTION_PAGE_SIZE')) or 100
