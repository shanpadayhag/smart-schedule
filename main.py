from argparse import ArgumentParser
from src.controllers.smart_schedule.smart_schedule_controller import scheduleTasksForDays, scheduleTasksToday

parser = ArgumentParser()

parser.add_argument('-t', "--today", action="store_true", help="start scheduling events today")
parser.add_argument('-r', "--reschedule", action="store_true", help="reschedule events if already scheduled")
parser.add_argument('-d', "--days", type=int, default=0, help="number of days to schedule events")
# parser.add_argument("--delete", action="store_true", help="delete events if in calendar, but do not schedule anything.")
# parser.add_argument("--force", action="store_true", help="don't ask for confirmation before rescheduling events")

args = parser.parse_args()

if __name__ == "__main__":
    if args.days >= 1:
        scheduleTasksForDays(days=args.days, reschedule=args.reschedule)
    else:
        scheduleTasksToday(reschedule=args.reschedule)

