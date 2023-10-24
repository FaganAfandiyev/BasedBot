import requests
import os
import pymongo
from pymongo import MongoClient

Key = os.environ['Key']
mongo_password = os.environ['dbpass']

# Replace the uri string with your MongoDB deployment's connection string.
uri = f"mongodb+srv://MD20M:{mongo_password}@baseddb.ukb0vd2.mongodb.net/?retryWrites=true&w=majority"

try:
  cluster = MongoClient(uri)
  print("connected")
except:
  print("error")


def groups():
 db = cluster["BasedDB"]

 collection = db["groups"]


 url = 'https://api.getbased.com/based/api/discovery/groups/f978e6e0-7bd8-4ad4-a717-058947c47cab'
 headers = {
  'accept': 'application/json',
  'authToken': Key,
  'x-api-key': "8c3cb2b8-5fd6-4bb4-97ed-0ec81f4d5247"
 }

 response = requests.get(url, headers=headers)

 #print(response.json())

 groups = response.json()
 #print(groups)

 for group in groups:
  _id = group['group']['id']
  name = group['group']['name']
  post = {"_id": f"{_id}", "name": f"{name}", "lastMessageID": ""}
  print(_id)
  print(name)
  try:
    collection.insert_one(post)
  except:
    print("Already added")

def users():
 db = cluster["BasedDB"]

 collection = db["users"]


 url = 'https://1985732681269cb5.apiclient-us.cometchat.io/v3.0/users'
 headers = {
  'accept': 'application/json',
  'authToken': Key,
  'x-api-key': "8c3cb2b8-5fd6-4bb4-97ed-0ec81f4d5247"
 }
 for i in range(10000000):
  payload = {
    "page":i
  }
  
  response = requests.get(url, headers=headers, json=payload)

  #print(response.json())

  users = response.json()
  #print(users)

  for user in users['data']:
   _id = user['uid']
   name = user['name']
   post = {"_id": f"{_id}", "name": f"{name}", "lastMessageID": ""}
   print(_id)
   print(name)
   try:
     collection.insert_one(post)
   except:
     print("Already added")


users()
#curl "https://api.getbased.com/based/api/discovery/groups/f978e6e0-7bd8-4ad4-a717-058947c47cab" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0" -H "Accept: application/json" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "x-api-key: 8c3cb2b8-5fd6-4bb4-97ed-0ec81f4d5247" -H "Origin: https://app.getbased.com" -H "DNT: 1" -H "Connection: keep-alive" -H "Referer: https://app.getbased.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site"
