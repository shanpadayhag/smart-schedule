from datetime import datetime
from src.data_transfer_objects.projects.project_dto import ProjectDTO
from typing import Optional

class EventDTO():
    id: Optional[str]
    title: str
    startDate: datetime
    endDate: datetime
    description: Optional[str]

    def __init__(
        self,
        title: str,
        startDate: datetime,
        endDate: datetime,
        id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
