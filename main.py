#on_message_edit (discord python)
#on_message_delete (discord python)

import os
import discord
from server_ import keep_alive
from serverJoin import onMemberJoin
from serverLeave import onMemberLeave
from socials import onSocialsMessage
from Jokes import onJoke
import messages
import moderation
import youtube

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
activity = discord.Activity(type=discord.ActivityType.watching,
                            name="School Sekai")
my_secret = os.environ['TOKEN']
client = discord.Client(intents=intents, activity=activity)
blackListedWords = ["kanker", "kkr", "cancer", "https://discord.gg/"]


#Register an event and define when the bot is ready to use
@client.event
async def on_ready():
    print("I have launched with {0.user}".format(client))
    youtube.checkforVideos.start(client)


@client.event
async def on_reaction_add(reaction, member):
  Guild = client.get_guild(699557641818734634)
  
  if member != client.user:
    if reaction.emoji == "\U0001F3B5":
      role = Guild.get_role(1010980678998949938)
      await member.add_roles(role)
    if reaction.emoji == "\U0001F3B8":
      role = Guild.get_role(1010980219038990387)
      await member.add_roles(role)
    if reaction.emoji == "\U0001F3BC":
      role = Guild.get_role(1010981513849995425)
      await member.add_roles(role)
    if reaction.emoji == "\U00002615":
      role = Guild.get_role(1010981914104041572)
      await member.add_roles(role)
    if reaction.emoji == "\U0001F3A1":
      role = Guild.get_role(1010982791623745606)
      await member.add_roles(role)
    if reaction.emoji == "\U0001F4BB":
      role = Guild.get_role(1010983272806883399)
      await member.add_roles(role)
      
@client.event
async def on_reaction_remove(reaction, member):
  if member != client.user:
    if reaction.emoji == "\U0001F3B5":
      role = member.guild.get_role(1010980678998949938)
      await member.remove_roles(role)
    if reaction.emoji == "\U0001F3B8":
      role = member.guild.get_role(1010980219038990387)
      await member.remove_roles(role)
    if reaction.emoji == "\U0001F3BC":
      role = member.guild.get_role(1010981513849995425)
      await member.remove_roles(role)
    if reaction.emoji == "\U00002615":
      role = member.guild.get_role(1010981914104041572)
      await member.remove_roles(role)
    if reaction.emoji == "\U0001F3A1":
      role = member.guild.get_role(1010982791623745606)
      await member.remove_roles(role)
    if reaction.emoji == "\U0001F4BB":
      role = member.guild.get_role(1010983272806883399)
      await member.remove_roles(role)
      
        
#Function to check for a message
#The on_message function can take a argument
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content) > 0:
        for word in blackListedWords:
            if word in message.content:
                roleCheck = moderation.checkOwnerRoles(message, False)
                if (roleCheck == False):
                    await message.delete()
                    await message.channel.send(
                        "{0.author.mention} You said a blacklisted word".
                        format(message))
                    await messages.BlackListedWords(message, client)

    #Check of the messages starts with 39!M and then await a sendback depending on the message command
    if message.content.startswith('39M!Hello'):
        await message.channel.send(
            "Hello there im Big debut miku can i help you with something? {0.author.display_name}"
            .format(message))

    if message.content.startswith('39M!Socials'):
        await onSocialsMessage(message)

    if message.content.startswith('39M!Joke'):
        await onJoke(message)

    if message.content.startswith('39M!Help'):
        await messages.onHelpMessage(message)

    if message.content.startswith('39M!Elise'):
        await messages.EliseGenderStory(message)

    if message.content.startswith('39M!LMS'):
        await messages.LMSStory(message)

    if message.content.startswith('39M!MyAvatar'):
        if (len(message.mentions) == 1):
            await messages.GetAvatar(message, message.mentions[0])
        else:
            await messages.GetAvatar(message, message.author)

    if message.content.startswith('39M!8Ball') and len(message.content) > 11:
        await messages.EightBallResponse(message)
    elif message.content.startswith('39M!8Ball') and len(message.content) < 11:
        await message.channel.send(
            "I miss a question {0.author.mention}".format(message))

    if message.content.startswith('39M!Kick'):
        haha = False
        roleCheck = moderation.checkModRoles(message, haha)
        if (roleCheck):
            imuunRole = moderation.checkAdminRole(message.mentions[0], haha)
            if (imuunRole):
                await moderation.ErrorMessage(
                    message,
                    "An error occured with the 39M!Kick command. Hang om im looking into the issue <:MikuStare:714726830703247362>",
                    "I cant kick people with the role Vocaloid or Manager or Myself",
                    message.author)
            else:
                await moderation.OnKick(message, client)
        else:
            await moderation.ErrorMessage(
                message,
                "An error occured with the 39M!Kick command. Hang om im looking into the issue <:MikuStare:714726830703247362>",
                "Lacks the permissions to use this command", message.author)


#Check if a member has left or joined the guild
@client.event
async def on_member_join(member):
    await onMemberJoin(member, client)


@client.event
async def on_member_remove(member):
    await onMemberLeave(member, client)
  
#client.run to run the bot with the secret token
#Also check if the request limit has reached anf if so restart the bot
keep_alive()
try:
    print(client.run(my_secret))
    client.run(my_secret)
except:
    print("at except")
    os.system("kill 1")
