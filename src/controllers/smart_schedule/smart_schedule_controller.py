from datetime import datetime
from src.actions.google_calendar.get_gc_events import getGCEvents
from src.actions.notion.get_notion_events import getNotionEvents
from src.actions.notion.get_notion_projects import getNotionProjects
from src.actions.smart_schedule.create_timeline import createTimeline
from src.services.datetime.datetime import getStartDateTimeOf, getEndDateTimeOf
from src.services.google import google_service as GoogleService

def scheduleTasksToday(reschedule: bool):
    now = datetime.now()
    startDate = getStartDateTimeOf(datetime=now)
    endDate = getEndDateTimeOf(datetime=now)
    service = GoogleService.calendarService()

    projects = getNotionProjects()
    tasks = getNotionEvents(startDate=startDate, endDate=endDate)
    googleEvents = getGCEvents(startDate=now, endDate=endDate, googleService=service)
    timelineEvents = createTimeline(
        projects=projects,
        tasks=tasks,
        googleEvents=googleEvents,
        startDate=now,
        endDate=endDate,
        reschedule=reschedule)
    
    for event in timelineEvents:
        print(event.title, event.startDate, event.endDate)

def scheduleTasksForDays(days: int, reschedule: bool):
    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE DAYS TASKS

