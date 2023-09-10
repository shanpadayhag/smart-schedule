from datetime import datetime
from src.services.notion.notion_service import requestNotion
from src.data_transfer_objects.tasks.task_dto import TaskDTO
from src.configs.env.env import Env
from src.services.datetime.datetime import fromNotionDate, notionFormatDate

def getNotionTasks(startDate: datetime, endDate: datetime):
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
                        'equals': '🔄'
                    }
                }
            ]
        }
    }

    data = requestNotion(url=url, parameters=parameters)
    tasks = []

    for task in data['results']:
        taskProperties = task['properties']
        tasks.append(TaskDTO(
            id=task['id'],
            title=taskProperties['Task name']['title'][0]['text']['content'],
            due=fromNotionDate(taskProperties['Due']['date']['start']),
            estimatedTime=taskProperties['Estimated Time (hours)']['number']
        ))

    return tasks
