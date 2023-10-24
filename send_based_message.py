import requests
import os
import pymongo
from pymongo import MongoClient

Key = os.environ['Key']

url = "https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/messages"

mongo_password = os.environ['dbpass']

# Replace the uri string with your MongoDB deployment's connection string.
uri = f"mongodb+srv://MD20M:{mongo_password}@baseddb.ukb0vd2.mongodb.net/?retryWrites=true&w=majority"

try:
  cluster = MongoClient(uri)
  print("connected")
except:
  print("error")


db = cluster["BasedDB"]


#look at this
def get_id(name, typeOfChat):
 search = {"name":f"{name}"}
 collection = db[f"{typeOfChat}"]
 collection.find(search)
 item_details = collection.find(search)
 for item in item_details:
   continue
 return item['_id']

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

def send_based_message(receivertype, receiverid, message):
 if (receivertype == "users"):
  receivertype = "user"
 if (receivertype == "groups"):
  receivertype = "group"
 if (receivertype == "user"):
  receiver = get_id(receiverid, "users")
 elif (receivertype == "group"):
  receiver = get_id(receiverid, "groups")
 payload = {
  "receiver": receiver,
  "receiverType": receivertype,
  "category": "message",
  "type": "text",
  "data": {"text": message},
 }

 response = requests.post(url, headers=headers, json=payload)
 return response.json()
 # print(response.json())


#{type: "text", receiverType: "user", category: "message", data: {text: "test5"}, text: "test5",…}