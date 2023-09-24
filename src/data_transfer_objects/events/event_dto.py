from datetime import datetime
from src.data_transfer_objects.projects.project_dto import ProjectDTO
from typing import Optional

class EventDTO():
    id: str
    title: str
    description: Optional[str]
    startDate: datetime
    endDate: datetime

    def __init__(
        self,
        id: str,
        title: str,
        description: Optional[str],
        startDate: datetime,
        endDate: datetime
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
