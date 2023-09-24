from datetime import datetime
from src.services.datetime.datetime import googleCalendarFormatDate

def getGCEvents(startDate: datetime, endDate: datetime, googleService):
    pageToken = None
    calendarEvents = []

    while True:
        calendarList = googleService.events().list(
            calendarId='primary',
            timeMin=googleCalendarFormatDate(datetime=startDate),
            timeMax=googleCalendarFormatDate(datetime=endDate),
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        for calendarListEntry in calendarList["items"]:
            calendarEvents.append(calendarListEntry)

        pageToken = calendarList.get("nextPageToken")

        if not pageToken:
            break
    
    return calendarEvents
