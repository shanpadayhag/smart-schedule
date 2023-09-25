from src.configs.env.env import Env
from src.data_transfer_objects.projects.project_dto import ProjectDTO
from src.services.notion.notion_service import requestNotion
import src.services.object.object_service as ObjectService

def getNotionProjects() -> list[ProjectDTO]:
    url = 'https://api.notion.com/v1/databases/{}/query'.format(Env.notionDatabaseProjectsId)

    projects = []
    data = requestNotion(url=url)

    for project in data['results']:
        projects.append(ProjectDTO(
            id=project['id'],
            name=project['properties']['Project name']['title'][0]['text']['content'],
            color=ObjectService.getNestedValue(project, ['properties', 'Color', 'rich_text', 0, 'plain_text']),
        ))

    return projects
