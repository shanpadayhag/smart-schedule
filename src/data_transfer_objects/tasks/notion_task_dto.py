from datetime import datetime
from data_transfer_objects.tasks.task_dto import TaskDTO

class NotionTaskDTO(TaskDTO):
    def __init__(self, id: str, title: str, due: datetime, estimatedTime: int) -> None:
        super().__init__(id=id, title=title, due=due, estimatedTime=estimatedTime)
