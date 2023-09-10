from datetime import datetime
from src.services.datetime.datetime import getStartDateTimeOf
from src.actions.notion.get_notion_tasks import getNotionTasks

def scheduleTasksToday(reschedule: bool):
    currentDate = getStartDateTimeOf(datetime=datetime.now())

    tasks = getNotionTasks(startDate=currentDate, endDate=currentDate)
    print(tasks)

    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE TODAY TASKS

def scheduleTasksForDays(days: int, reschedule: bool):
    if reschedule:
        # TODO: DELETE EXISTING TASKS
        pass
    # TODO: SCHEDULE DAYS TASKS

