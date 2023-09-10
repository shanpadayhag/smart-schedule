class ProjectDTO:
    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
