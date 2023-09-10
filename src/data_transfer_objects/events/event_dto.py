from datetime import datetime
from src.data_transfer_objects.projects.project_dto import ProjectDTO
from src.data_transfer_objects.tasks.task_dto import TaskDTO

class EventDTO(TaskDTO):
    project: ProjectDTO

    def __init__(self, id: str, title: str, due: datetime, estimatedTime: int, project: ProjectDTO) -> None:
        super().__init__(id=id, title=title, due=due, estimatedTime=estimatedTime)
        self.project = project
