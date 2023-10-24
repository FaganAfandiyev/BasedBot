import os
from get_messages import check_for_messages, last_message, message_id, message_sender, sender_pfp_image
from wrappers import command
import time
from BasedBot import BasedBot
from discord_webhook import DiscordWebhook
from keep_alive import keep_alive

chatid = "c03378ee-c395-45f5-ad46-9eb5be747db6"
typeOfChat = "groups"

webhook_url = os.environ['WebhookUrl']

basedBot = BasedBot()

lastmsg = check_for_messages(chatid, typeOfChat)
lastID = last_message(chatid, typeOfChat)
webhook_name = message_sender(chatid, typeOfChat)
webhook_avatar = sender_pfp_image(chatid, typeOfChat)
webhook = DiscordWebhook(url=webhook_url,
                         username=webhook_name,
                         avatar_url=webhook_avatar)
webhook.content = lastmsg
webhook.execute()

keep_alive()

while True:
  if (message_id(chatid, typeOfChat) != lastID):
    webhook_name = message_sender(chatid, typeOfChat)
    webhook_avatar = sender_pfp_image(chatid, typeOfChat)
    webhook = DiscordWebhook(url=webhook_url,
                             username=webhook_name,
                             avatar_url=webhook_avatar)
    lastmsg = check_for_messages(chatid, typeOfChat)
    webhook.content = lastmsg
    name = message_sender(chatid, typeOfChat)
    print(name)
    webhook.execute()
    lastID = last_message(chatid, typeOfChat)

    time.sleep(1)
