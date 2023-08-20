from datetime import datetime

import requests
from src.configs.env.env import Env
from src.services.datetime.datetime import notionFormatDate

def getNotionTasks(startDate: datetime, endDate: datetime):
    url = 'https://api.notion.com/v1/databases/{}/query'.format(Env.notionDatabaseTaskId)
    data = {
        "page_size": Env.notionPageSize,
        "filter": {
            "property": "Due",
            "date": {
                "on_or_after": notionFormatDate(startDate),
            }
        }
    }

    return requests.post(url, json=data, headers=__getNotionApiHeader()).json()

def getNotionTaskContent(id: int):
    pass

def saveGoogleCalendarLinkInNotionTask(taskId: int, googleCalendarLink: str):
    pass

def getNotionProjects():
    pass

def __getNotionApiHeader() -> str:
    return {
        "accept"            : "application/json",
        "Notion-Version"    : "2022-06-28",
        "Authorization"     : "Bearer {}".format(Env.notionSecretKey),
        "content-type"      : "application/json",
    }
