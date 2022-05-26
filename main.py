import os
import discord
import random
from server_ import keep_alive

intents = discord.Intents.default()
intents.members = True
my_secret = os.environ['TOKEN']
client = discord.Client(intents=intents)

embedWelcomeURLS = ["https://i.kym-cdn.com/photos/images/original/001/236/970/0f1.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329033756672030/LTWB_Micrystal.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329293066108936/2ffuym.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329462636183602/ezgif.com-gif-maker_3.gif" ,"https://cdn.discordapp.com/attachments/757611689003974779/861329538398552084/ezgif-3-f1b581708e09.gif", "https://media.tenor.com/images/7452b9709e58ee148807ca1637ea308d/tenor.gif"]
imageUrl = random.choice(embedWelcomeURLS)

embed=discord.Embed(title="🎀 Welcome we have some usual information 🎀", description="We have a few rules and things to look out for here 💖 \n <#703637751274143854> <-- Channel where you can find the rules of the server 🎀 \n <#797792369416208386>  <-- For some information on the server 🎀 \n <#699557641818734638> <-- Main  chat 🎀 \n  <#709050194662260797> <-- channel  for some roles  🎀", color=0x00ffd5)
embed.set_image(url=imageUrl)
embed.set_footer(text="🎀 Welcome to elise her hangout 🎀")
#await ctx.send(embed=embed)

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

@client.event
async def on_member_join(member):
  channel = client.get_channel(797789187910664193)
  role = member.guild.get_role(699572966551322635)
  await channel.send("{0.mention} welcome to Elise her hangout".format(member))
  await channel.send(embed=embed)
  await member.add_roles(role)

#client.run to run the bot with the secret token
keep_alive()
client.run(my_secret)
