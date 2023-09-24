from datetime import datetime
from src.actions.google_calendar.get_gc_events import getGCEvents
from src.actions.notion.get_notion_events import getNotionEvents
from src.services.datetime.datetime import getStartDateTimeOf, getEndDateTimeOf
from src.services.google import google_service as GoogleService

def scheduleTasksToday(reschedule: bool):
    now = datetime.now()
    startDate = getStartDateTimeOf(datetime=now)
    endDate = getEndDateTimeOf(datetime=now)
    service = GoogleService.calendarService()

    tasks = getNotionEvents(startDate=startDate, endDate=endDate)
    googleEvents = getGCEvents(startDate=now, endDate=endDate, googleService=service)
    print(googleEvents)

    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE TODAY TASKS

def scheduleTasksForDays(days: int, reschedule: bool):
    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE DAYS TASKS

