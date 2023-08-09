import requests
import os
from filters import date_filter, today_filter, tomorrow_filter
import pprint
from dotenv import load_dotenv

load_dotenv()

printer = pprint.PrettyPrinter()
pprint = printer.pprint

# Notion Environment Variables
NOTION_SECRET_KEY = os.environ.get("NOTION_SECRET_KEY")
NOTION_DATABASE_TASK_ID = os.environ.get("NOTION_DATABASE_TASK_ID")
NOTION_DATABASE_PROJECTS_ID = os.environ.get("NOTION_DATABASE_PROJECTS_ID")

cache = {}
priorities = ["High", "Medium", "Low"]


def get_event_content(event_id):
    url = "https://api.notion.com/v1/blocks/{}/children".format(event_id)
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data["results"]


def get_event_data(event, projects):
    event["properties"] = {
        str(key.encode("ascii", errors="ignore"))[2:-1].strip(): value
        for key, value in event["properties"].items()
    }
    project_ids = event["properties"]["Project"]["relation"]
    project = "Personal Management"

    if len(project_ids) > 0:
        project = projects[project_ids[0]["id"]]
        project = event["properties"]["Task name"]["title"][0]["plain_text"]

    priority = event["properties"]["Priority"]["select"]
    priority = priority["name"] if priority else "Low"
    priority = priorities.index(priority)
    work_block = event["properties"]["Task name"]["title"][0]["plain_text"]

    title = event["properties"]["Task name"]["title"][0]["plain_text"]
    gcal_id = event["properties"]["gcal_id"]["rich_text"]
    gcal_id = "" if len(gcal_id) == 0 else gcal_id[0]
    date = event["properties"]["Due"]["date"]["start"]

    created_time = event["properties"]["Created time"]["created_time"]
    est_time = event["properties"]["Estimated Time (hours)"]["number"]
    if not est_time:
        est_time = 1
    if len(event["properties"]["Parent-task"]["relation"]) > 0:
        pid = event["properties"]["Parent-task"]["relation"][0]["id"]
        if pid in cache:
            parent_event = cache[pid]
        else:
            parent_event = get_event_by_id(pid)
            cache[pid] = parent_event
        parent_title = get_event_data(parent_event, projects)["title"]
        title = "[{}] {}".format(parent_title, title)
    is_parent = len(event["properties"]["Sub-tasks"]["relation"]) > 0
    
    result = {
        "id": event["id"],
        "gcal_id": gcal_id,
        "is_parent": is_parent,
        "title": title,
        "date": date,
        "created_time": created_time,
        "estimate": est_time,
        "priority": priority,
        "project": project,
        "work_block": work_block,
    }
    return result


def get_event_by_id(id_):
    url = "https://api.notion.com/v1/pages/{}".format(id_)

    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def get_notion_date(start_date, end_date):
    # Get all events for today and prior
    url = "https://api.notion.com/v1/databases/{}/query".format(NOTION_DATABASE_TASK_ID)
    payload = {
        "page_size": 100,
        "filter": date_filter(start_date, end_date),
    }
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
        "content-type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data["results"]


def get_notion_today():
    # Get all events for today and prior
    url = "https://api.notion.com/v1/databases/{}/query".format(NOTION_DATABASE_TASK_ID)
    payload = {
        "page_size": 100,
        "filter": today_filter(),
    }
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
        "content-type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    events = data["results"]
    return events


def get_notion_projects():
    # Get all events for tomorrow and prior
    url = "https://api.notion.com/v1/databases/{}/query".format(NOTION_DATABASE_PROJECTS_ID)
    payload = {
        "page_size": 100,
    }
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
        "content-type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    projects = {p["id"]: p for p in data["results"]}
    return projects


def get_notion_tomorrow():
    # Get all events for tomorrow and prior
    url = "https://api.notion.com/v1/databases/{}/query".format(NOTION_DATABASE_TASK_ID)
    payload = {
        "page_size": 100,
        "filter": tomorrow_filter(),
    }
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
        "content-type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data["results"]


def get_notion_events(start_date, end_date):
    projects = get_notion_projects()
    events = get_notion_date(start_date, end_date)
    event_data = [
        e
        for e in sorted(
            [get_event_data(e, projects) for e in events],
            key=lambda x: (
                x["priority"],
                float(x["estimate"]),
                x["created_time"],
            ),
        )
        if not e["is_parent"]
    ]
    return event_data


def update_notion_event(notion_id, gcal_id, gcal_link):
    url = "https://api.notion.com/v1/pages/{}".format(notion_id)
    payload = {
        "properties": {
            "gcal_id": {
                "rich_text": [
                    {
                        "type": "text",
                    }
                ]
            },
        }
    }
    if not gcal_id or not gcal_link:
        payload["properties"]["gcal_id"]["rich_text"] = []

    else:
        payload["properties"]["gcal_id"]["rich_text"] = [
            {
                "type": "text",
                "plain_text": gcal_id,
                "text": {
                    "content": "Google Calendar Link",
                    "link": {"url": gcal_link},
                },
            }
        ]
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer {}".format(NOTION_SECRET_KEY),
        "content-type": "application/json",
    }

    response = requests.patch(url, json=payload, headers=headers)
