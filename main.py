import os
import discord
from server_ import keep_alive
from serverJoin import onMemberJoin
from serverLeave import onMemberLeave
from socials import onSocialsMessage

intents = discord.Intents.default()
intents.members = True
my_secret = os.environ['TOKEN']
client = discord.Client(intents=intents)

#Register an event and define when the bot is ready to use
@client.event
async def on_ready():
  print("I have launched with {0.user}".format(client))

#Function to check for a message 
#The on_message function can take a argument
@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  #Check of the messages starts with 39!M and then await a sendback
  if message.content.startswith('39M!Hello'):
    await message.channel.send("Hello there im Big debut miku can i help you with something?")

  if message.content.startswith('39M!Socials'):
    await onSocialsMessage(message)
    

@client.event
async def on_member_join(member):
  await onMemberJoin(member, client)

@client.event
async def on_member_remove(member):
  await onMemberLeave(member, client)

#client.run to run the bot with the secret token
keep_alive()
client.run(my_secret)
