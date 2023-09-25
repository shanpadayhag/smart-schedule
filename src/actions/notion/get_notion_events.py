from datetime import datetime
from src.configs.env.env import Env
from src.data_transfer_objects.tasks.task_dto import TaskDTO
from src.services.datetime.datetime import fromNotionDate, notionFormatDate
from src.services.notion.notion_service import requestNotion

def getNotionEvents(startDate: datetime, endDate: datetime):
    url = 'https://api.notion.com/v1/databases/{}/query'.format(Env.notionDatabaseTaskId)
    parameters = {
        'page_size': Env.notionPageSize,
        'filter': {
            'and': [
                {
                    'property': 'Due',
                    'date': {
                        'on_or_after': notionFormatDate(startDate),
                    }
                },
                {
                    'property': 'Due',
                    'date': {
                        'on_or_before': notionFormatDate(endDate),
                    }
                },
                {
                    'property': 'Status',
                    'status': {
                        'does_not_equal': '✅'
                    }
                },
                {
                    'property': 'Status',
                    'status': {
                        'does_not_equal': '♲'
                    }
                },
            ]
        }
    }

    data = requestNotion(url=url, parameters=parameters)
    events = []

    for task in data['results']:
        taskProperties = task['properties']
        events.append(TaskDTO(
            id=task['id'],
            title=taskProperties['Task name']['title'][0]['text']['content'],
            due=fromNotionDate(taskProperties['Due']['date']['start']),
            estimatedTime=taskProperties['Estimated Time (hours)']['number']
        ))

    return events
