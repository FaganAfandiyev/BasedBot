import os
from get_messages import check_for_messages, chatid, last_message, typeOfChat, message_id, message_sender
from send_based_message import send_based_message
from BasedBot import BasedBot
from wrappers import command
import time
import nextcord
from nextcord import Interaction, SlashOption, Webhook
from nextcord.ui import Button, View
from nextcord.ext import commands

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN=os.environ["TOKEN"]
sender = ""

basedBot = BasedBot()


@bot.event
async def on_ready():
  print("bot running ser")


# @ctx.slash_command(name="send", description="Send your message to sellected group")
# async def send(interaction: Interaction, receiver: str = SlashOption(description="Who you want to send to", required=True), type: str = SlashOption(description="groups/users", required=True), message: str = SlashOption(description="The message you want to send", required=True)):


@bot.slash_command(name="sendbased",
                   description="Send your message to selected group")
async def sendbased(interaction: Interaction,
                    message,
                    receiver=SlashOption(name="receiver",
                                         choices={
                                           "kriyos": "kriyos",
                                           "md20m": "md20m",
                                           'moss': 'moss'
                                         }),
                    type=SlashOption(name="type",
                                     choices={
                                       "user": "user",
                                       "group": "group"
                                     })):
  basedBot.send(type, receiver, message)
  sentConfirmation = nextcord.Embed(title=f"You sent a message to {receiver}",
                                    description=message,
                                    colour=0x00ff00)
  await interaction.send(embed=sentConfirmation)


@bot.slash_command(name="ping",
                   description="Send your message to selected group")
async def ping(interaction: Interaction):
  await interaction.send("pong")


@bot.slash_command(name="createwebhook", description="Self explanatory")
async def createwebhook(interaction: Interaction):
  webhook = await interaction.channel.create_webhook(name='Test Webhook')
  print(f'Webhook URL: {webhook.url}')


# @bot.slash_command(name="pfp", description="Get pfp")
# async def createwebhook(interaction: Interaction):
#   await interaction.send(basedBot.message_sender_pfp("kriyos"))


@bot.slash_command(name="channel",
                   description="create channel if moss still dont give perm")
async def channel(interaction: Interaction, name):
  guild = interaction.guild
  await interaction.send("<@949737170896314469>")
  await guild.create_text_channel(name=f"{name}")


print("_")

bot.run(
  "TOKEN")
