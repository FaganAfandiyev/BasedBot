import requests
import os
import json
import asyncio

Key = os.environ['Key']


def update_message(ID, text):
 url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/messages/{ID}"

 headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "authToken": Key,
    "Origin": "https://app.getbased.com",
    "Referer": "https://app.getbased.com/",
    "resource": "WEB-3_0_10-6f438296-7361-4313-9dc1-f4b8df8bcdbc-1675867074531",
    "sdk": "javascript@3.0.10",
    "onBehalfOf": "47d71545-a02b-4cda-9d6f-573d2ab2d870"
 }

 payload = {"data": {"text": f"{text}"}}

 response = requests.put(url, json=payload, headers=headers)

 print(response.text)