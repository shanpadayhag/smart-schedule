from datetime import datetime as defaultDateTime

def notionFormatDate(datetime: defaultDateTime) -> str:
    return datetime.strftime('%Y-%m-%dT%H:%M:%S')

def getStartDateTimeOf(datetime: defaultDateTime) -> defaultDateTime:
    return defaultDateTime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=0,
        minute=0,
    )
