# Second Brain Smart Scheduling: Notion + Google

## Installation
Copy and fill environment variables
```sh
cp .env.example .env
```

Install python virtual environment
```sh
python3 -m venv .venv
```

Activate virtual environment
```sh
source .venv/bin/activate
```

Run script
```sh
python second_brain.py --today
```

## Usage
```
usage: second_brain.py [-h] [--today] [--days DAYS] [--reschedule] [--force]

options:
  -h, --help    show this help message and exit
  --today       start scheduling events today
  --days DAYS   number of days to schedule events
  --reschedule  reschedule events if already scheduled
  --force       don't ask for confirmation before rescheduling events
```

## Requirements
 - Python 3.7+ (tested with python 3.11)
 - installation of requirements `pip install -r requirements.txt`
 - bashrc with API integration setup
```
# File: ~/.bashrc

standard file contents...

...
export GOOGLE_CREDENTIALS_BASE_DIR="/home/user/.second_brain_credentials" 
export NOTION_SECRET_KEY="<< notion api key>>"
export NOTION_DATABASE_TASK_ID="<< notion task list id >>"
export NOTION_DATABASE_PROJECTS_ID="<< list of notion projects >>"
export SCHEDULING_CALENDAR_ID="<< schedule calendar id >>"
export GOOGLE_CALENDAR_ID="<< work calendar id >>"
```

Duplicate Notion Template `https://excited-croissant-4e3.notion.site/project-planner-915d685969fa4d58b9ac930197fe6edd?pvs=4`

## Feature TODO
- [x] Notion API Integration
- [x] G-Cal API Integration
- [x] Notion/G-Cal Sync
  - [x] Add events formatted using worl block as title and content as event description
  - [x] Adding Calendar Events from Notion that are not in google (gcal id is empty)
  - [x] Rescheduling events option
- [ ] Ability to choose start/end range for days
- [ ] Dont schedule in the past
- [ ] Beter Optimization 
  - [ ] Finding better start times?
  - [ ] Gradient Descent using old calendar data?
  - [ ] Total number of hours can be split up into blocks?
- [ ] Arbitrary timezones
