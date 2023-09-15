from datetime import datetime
from src.actions.google_calendar.get_gc_events import getGCEvents
from src.actions.notion.get_notion_tasks import getNotionTasks
from src.services.datetime.datetime import getStartDateTimeOf
from src.services.google import google_service

def scheduleTasksToday(reschedule: bool):
    currentDate = getStartDateTimeOf(datetime=datetime.now())
    service = google_service.getService()

    tasks = getNotionTasks(startDate=currentDate, endDate=currentDate)
    getGCEvents(startDate=currentDate, endDate=currentDate, gcService=service)

    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE TODAY TASKS

def scheduleTasksForDays(days: int, reschedule: bool):
    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE DAYS TASKS

