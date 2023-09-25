from typing import Optional

class ProjectDTO:
    id: str
    name: str
    color: Optional[str]

    def __init__(self, id: str, name: str, color: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.color = color
