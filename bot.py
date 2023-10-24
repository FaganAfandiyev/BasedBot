import os
import asyncio
from wrappers import command
from getsol import getsol
import time
from BJ import blackjack
from BasedBot import BasedBot

bot = BasedBot()


@command("m!Ping", "md20m")
def ping():
  bot.send("md20m", "Pong")


@command("m!Sol", "kriyos")
def sol():
  solprice = getsol()
  bot.send("kriyos", solprice)


@command("b!BJ", "md20m")
def playbj():
  try:
    asyncio.run(blackjack(bot.message_sender_name("md20m"), "md20m"))
  except Exception as exc: 
     bot.send("md20m", f"{exc}")
    
while True:
  ping()
  sol()
  playbj()

#lastID = ""

#while True:
#chatid = "e3f4515f-9d06-4f04-80db-cae08d5f4c9c"
#typeOfChat = "users"
#time.sleep(1)
#if(check_for_messages(chatid, typeOfChat) == "m!Ping" and message_id(chatid, typeOfChat) != lastID):
#send_based_message("user", "e3f4515f-9d06-4f04-80db-cae08d5f4c9c", "Pong")
#lastID = last_message(chatid, typeOfChat)
