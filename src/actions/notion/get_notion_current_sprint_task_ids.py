from src.configs.env.env import Env
from src.services.notion.notion_service import requestNotion
import src.services.object.object_service as ObjectService

def getNotionCurrentSprintTaskIds() -> list[str]:
    url = 'https://api.notion.com/v1/databases/{}/query'.format(Env.notionDatabaseSprintId)
    parameters = {
        'page_size': Env.notionPageSize,
        'filter': {
            'property': 'Sprint status',
            'status': {
                'equals': 'Current'
            }
        },
    }

    tasks = []

    for taskIdObject in ObjectService.getNestedValue(
        object=requestNotion(url=url, parameters=parameters),
        keys=['results', 0, 'properties', 'Tasks', 'relation']):
        tasks.append(taskIdObject['id'])

    return tasks
