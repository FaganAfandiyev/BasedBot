import requests
import os
import json
import asyncio

Key = os.environ['Key']

chatid = "e3f4515f-9d06-4f04-80db-cae08d5f4c9c"
typeOfChat = "users"

url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "authToken": Key,
    "appId": "1985732681269cb5",
    "Origin": "https://app.getbased.com",
    "Referer": "https://app.getbased.com/",
    "resource": "WEB-3_0_10-6f438296-7361-4313-9dc1-f4b8df8bcdbc-1675867074531",
    "sdk": "javascript@3.0.10"
}

payload = {
    "category": "message",
    "type": "text",
    "per_page":"1"
}




#response = requests.get(url, headers=headers, json=payload)


#jsonstring = response.json()

#length=(len(list(jsonstring['data']))-1)

#print(jsonstring['data'][length]['id'])

def last_message(chatid, typeOfChat):
  url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
  response = requests.get(url, headers=headers, json=payload)
  jsonstring = response.json()
  length=(len(list(jsonstring['data']))-1)
  lastMessageID = jsonstring['data'][length]['id']
  return lastMessageID

def message_id(chatid, typeOfChat):
  url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
  response = requests.get(url, headers=headers, json=payload)
  jsonstring = response.json()
  length=(len(list(jsonstring['data']))-1)
  messageID = jsonstring['data'][length]['id']
  return messageID

def check_for_messages(chatid, typeOfChat):
  try:
    url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
    response = requests.get(url, headers=headers, json=payload)
    jsonstring = response.json()
    length=(len(list(jsonstring['data']))-1)
    #print(jsonstring['data'][length]['data'])
    result = jsonstring['data'][length]['data']['text']
    # print(jsonstring['data'][length])
    return result
  except KeyError:
    try:
      if str(jsonstring['data'][length]['data']['action'])=="deleted":
        result = '⚠️ This message was deleted'
    # # print(result)
        return result
    except:
      try:
        if str(jsonstring['data'][length]['type'])=="reply":
          repto=str(jsonstring['data'][length]['data']['customData']['parentMessage']['senderName'])
          repmsg=str(jsonstring['data'][length]["data"]["customData"]['parentMessage']["messageText"])
          repas=str(jsonstring['data'][length]["data"]["customData"]["messageText"])
          result=str(f"`{repto}: {repmsg}` \n{repas}")
          return result
      except:
        result='An error occured'
        return result

def last_message_text(chatid, typeOfChat):
  url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
  response = requests.get(url, headers=headers, json=payload)
  jsonstring = response.json()
  length=(len(list(jsonstring['data']))-1)
  result = jsonstring['data'][length]['data']['text']
  # print(result)
  return result

def message_sender(chatid, typeOfChat):
  try:
    url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
    response = requests.get(url, headers=headers, json=payload)
    jsonstring = response.json()
    length=(len(list(jsonstring['data']))-1)
    result = jsonstring['data'][length]['data']['entities']['sender']['entity']['name']
    return result
  except KeyError:
    url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
    response = requests.get(url, headers=headers, json=payload)
    jsonstring = response.json()
    length=(len(list(jsonstring['data']))-1)
    #action by entity name
               # uid
                #avatar
    # print(str(jsonstring['data'][length]))
    result = jsonstring['data'][length]["data"]['entities']['by']['entity']['name']
    return result

def sender_pfp_image(chatid, typeOfChat):
  try:
    url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
    response = requests.get(url, headers=headers, json=payload)
    jsonstring = response.json()
    length=(len(list(jsonstring['data']))-1)
    picture = jsonstring['data'][length]['data']['entities']['sender']['entity']['avatar']
    return picture
  except KeyError:
    url = f"https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/{typeOfChat}/{chatid}/messages"
    response = requests.get(url, headers=headers, json=payload)
    jsonstring = response.json()
    length=(len(list(jsonstring['data']))-1)
    picture = jsonstring['data'][length]['data']['entities']['by']['entity']['avatar']
    return picture

#message_data("e3f4515f-9d06-4f04-80db-cae08d5f4c9c", "users")

#message_sender("e3f4515f-9d06-4f04-80db-cae08d5f4c9c", "users")

#check_for_messages(chatid, typeOfChat)