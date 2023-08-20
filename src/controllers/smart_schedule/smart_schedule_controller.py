from datetime import datetime, timedelta
from src.services.datetime.datetime import getStartDateTimeOf
from src.services.notion.notion_service import getNotionTasks

def scheduleTasksToday(reschedule: bool):
    currentDate = getStartDateTimeOf(datetime=datetime.now())
    endDate = currentDate + timedelta(days=1)

    getNotionTasks(startDate=currentDate, endDate=endDate)

    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE TODAY TASKS

def scheduleTasksForDays(days: int, reschedule: bool):
    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE DAYS TASKS

