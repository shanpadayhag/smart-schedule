from datetime import datetime

class TaskDTO:
    id: str
    title: str
    priority: int
    due: datetime
    estimatedTime: int

    def __init__(self, id: str, title: str, priority: int, due: datetime, estimatedTime: int) -> None:
        self.id = id
        self.title = title
        self.priority = priority
        self.due = due
        self.estimatedTime = estimatedTime
