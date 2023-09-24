from datetime import datetime
from src.configs.env.env import Env
from src.data_transfer_objects.events.google_event_dto import GoogleEventDTO
from src.services.datetime.datetime import fromGoogleDatetime, googleCalendarFormatDate

def getGCEvents(startDate: datetime, endDate: datetime, googleService) -> list[GoogleEventDTO]:
    pageToken = None
    calendarEvents = []

    while True:
        calendarList = googleService.events().list(
            calendarId=Env.googleCalendarId,
            timeMin=googleCalendarFormatDate(datetime=startDate),
            timeMax=googleCalendarFormatDate(datetime=endDate),
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        for calendarListItem in calendarList["items"]:
            try:
                calendarEvents.append(GoogleEventDTO(
                    id=calendarListItem['id'],
                    title=calendarListItem['summary'],
                    description=calendarListItem['description'] or None,
                    startDate=fromGoogleDatetime(calendarListItem['start']['dateTime']),
                    endDate=fromGoogleDatetime(calendarListItem['end']['dateTime']),
                    htmlLink=calendarListItem['htmlLink'],
                ))
            except:
                continue

        pageToken = calendarList.get("nextPageToken")

        if not pageToken:
            break
    
    return calendarEvents
