import typing
import requests

from src.configs.env.env import Env

def requestNotion(url: str, parameters: typing.Dict):
    return requests.post(url, json=parameters, headers=__getNotionApiHeader()).json()

def __getNotionApiHeader() -> str:
    return {
        "accept"            : "application/json",
        "Notion-Version"    : "2022-06-28",
        "Authorization"     : "Bearer {}".format(Env.notionSecretKey),
        "content-type"      : "application/json",
    }
