import requests
import os
from get_messages import check_for_messages, last_message, message_id, last_message_text, sender_pfp_image, message_sender
from send_based_message import send_based_message, get_id
from wrappers import command
from getsol import getsol
import time
import pymongo
from pymongo import MongoClient
from update_message import update_message

#SETTING DB
mongo_password = os.environ['dbpass']

# Replace the uri string with your MongoDB deployment's connection string.
uri = f"mongodb+srv://MD20M:{mongo_password}@baseddb.ukb0vd2.mongodb.net/?retryWrites=true&w=majority"

try:
  cluster = MongoClient(uri)
  print("connected")
except:
  print("error")

db = cluster["BasedDB"]


def get_receivertype(receiver):
  post = {}
  collection = db["users"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
    if (item['name'] == receiver):
      return "user"
  collection = db["groups"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
    if (item['name'] == receiver):
      return "user"


def get_chattype(receiver):
  post = {}
  collection = db["users"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
    if (item['name'] == receiver):
      return "users"
  collection = db["groups"]
  collection.find(post)
  item_details = collection.find(post)
  for item in item_details:
    if (item['name'] == receiver):
      return "groups"


class BasedBot:

  def send(self, receiver, message):
    sent_data = send_based_message(get_receivertype(receiver), receiver, message)
    #class edit():
      #update_message(sent_data["data"]["id"])

  def message_text(self, chat):
    return last_message_text(get_id(chat, get_chattype(chat)),
                             get_chattype(chat))

  def message_sender_pfp(self, chat):
    return sender_pfp_image(get_id(chat, get_chattype(chat)),
                            get_chattype(chat))

  def message_sender_name(self, chat):
    return message_sender(get_id(chat, get_chattype(chat)), get_chattype(chat))
    
  def message_id(self, chat):
    return message_id(get_id(chat, get_chattype(chat)), get_chattype(chat))

#bot = BasedBot()

#bot.send("kriyos", "test")

#get_receivertype("kriyos")
