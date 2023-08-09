from typing import List
from data_transfer_objects.tasks.task_dto import TaskDTO

class ProjectDTO:
    id: str
    name: str
    tasks: List[TaskDTO]

    def __init__(self, id: str, name: str, tasks: List[TaskDTO]) -> None:
        self.id = id
        self.name = name
        self.tasks = tasks
