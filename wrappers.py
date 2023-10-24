import os
import pymongo
from pymongo import MongoClient
from get_messages import check_for_messages, last_message, message_id, last_message_text, message_sender, sender_pfp_image
from update_message import update_message
import time

mongo_password = os.environ['dbpass']

# Replace the uri string with your MongoDB deployment's connection string.
uri = f"mongodb+srv://MD20M:{mongo_password}@baseddb.ukb0vd2.mongodb.net/?retryWrites=true&w=majority"

try:
  cluster = MongoClient(uri)
  print("connected")
except:
  print("error")


db = cluster["BasedDB"]

#for coll in db.list_collection_names():
    #print(coll)

#collection = db["users"]

#look at this / this one works the one in send_based_message doesn't
def get_id(name, typeOfChat):
 search = {"name":f"{name}"}
 collection = db[f"{typeOfChat}"]
 collection.find(search)
 item_details = collection.find(search)
 for item in item_details:
   continue
 return item['_id']

def get_last_message(name, lastMessageID):
 search = {"name":f"{name}"}
 collection = db[f"{lastMessageID}"]
 collection.find(search)
 item_details = collection.find(search)
 for item in item_details:
   continue
 return item['lastMessageID']

def get_chattype(receiver):
  post = {}
  collection = db["users"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
   if(item['name'] == receiver):
     return "users"
  collection = db["groups"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
   if(item['name'] == receiver):
     return "groups"

def command(string_arg, chat_info):
    def decorator(func):
        def wrapper(*args, **kwargs):
            typeOfChat = get_chattype(chat_info)
            print(typeOfChat)
            chatid = get_id(chat_info, typeOfChat)
            lastID = get_last_message(chat_info, typeOfChat)
            time.sleep(1)
            # print(chatid)
            if string_arg in check_for_messages(chatid, typeOfChat) and message_id(chatid, typeOfChat) != lastID:
                lastID = last_message(chatid, typeOfChat)
                search = {"name":f"{chat_info}"}
                collection = db[f"{typeOfChat}"]
                collection.find(search)
                item_details = collection.find(search)
                for item in item_details:
                 continue
                update = { "$set": { "lastMessageID": f"{last_message(item['_id'], f'{typeOfChat}')}" } }
                collection.update_one(search, update)
                class message():
                 def ID():
                  id = last_message(chatid, typeOfChat)
                  return id
                 def text():
                  txt = last_message_text(chatid,typeOfChat)
                  #print(txt)
                  return txt
                 def update(uID, uText):
                   update_message(uID, uText)
                 class sender():
                  def pfp():
                    pfp_image = sender_pfp_image(chatid, typeOfChat)
                    return pfp_image
                  def name():
                    sender_name = message_sender(chatid, typeOfChat)
                    return sender_name
                try:
                 return func(message, *args, **kwargs)
                except:
                 return func(*args, **kwargs)
        return wrapper
    return decorator

def listen(chat_info, lastID):
    def decorator(func):
        def wrapper(*args, **kwargs):
            typeOfChat = get_chattype(chat_info)
            print(typeOfChat)
            chatid = get_id(chat_info, typeOfChat)
            lastID = get_last_message(chat_info, typeOfChat)
            time.sleep(1)
            if message_id(chatid, typeOfChat) != lastID:
              class message():
                def ID():
                 id = last_message(chatid, typeOfChat)
                 return id
                def text():
                  txt = last_message_text(chatid,typeOfChat)
                  #print(txt)
                  return txt
                def update(uID, uText):
                   update_message(uID, uText)
                class sender():
                  def pfp():
                    pfp_image = sender_pfp_image(chatid, typeOfChat)
                    return pfp_image
                  def name():
                    sender_name = message_sender(chatid, typeOfChat)
                    return sender_name
              return func(message, *args, **kwargs)
        return wrapper
    return decorator

@command("m!Ping", "md20m")
def test():
    print("Do something here")

lID = ""


