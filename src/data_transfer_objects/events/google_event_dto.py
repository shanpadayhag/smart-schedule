from datetime import datetime
from src.data_transfer_objects.events.event_dto import EventDTO
from typing import Optional

class GoogleEventDTO(EventDTO):
    htmlLink: str

    def __init__(
        self,
        id: str,
        title: str,
        description: Optional[str],
        startDate: datetime,
        endDate: datetime,
        htmlLink: str
    ) -> None:
        super().__init__(
            id=id,
            title=title,
            description=description,
            startDate=startDate,
            endDate=endDate)
        self.htmlLink = htmlLink
