import pytz

from datetime import datetime as defaultDateTime
from src.configs.env.env import Env

def notionFormatDate(datetime: defaultDateTime) -> str:
    return datetime.strftime('%Y-%m-%dT%H:%M:%S')

def fromNotionDate(datetime: str) -> defaultDateTime:
    return defaultDateTime.strptime(datetime, '%Y-%m-%d')

def googleCalendarFormatDate(datetime: defaultDateTime) -> str:
    timezone = pytz.timezone(Env.appTimeZone)
    utcDatetime = timezone.localize(datetime).astimezone(pytz.utc).replace(tzinfo=None)
    return utcDatetime.isoformat() + 'Z'

def getStartDateTimeOf(datetime: defaultDateTime) -> defaultDateTime:
    return defaultDateTime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=0,
        minute=0,
    )

def getEndDateTimeOf(datetime: defaultDateTime) -> defaultDateTime:
    return defaultDateTime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=23,
        minute=59,
        second=59,
    )
