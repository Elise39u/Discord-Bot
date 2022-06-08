import discord
import random

helpEmbed=discord.Embed(title="I found my commands. *Whistele noises*", description="We have the following commands but first its good to know my prefix is 39M!. Most commands are also case senstive so be aware \n 🎀 39M!Help --> Show this message \n 🎀 39M!Hello --> Says hello to you \n 🎀 39M!Joke --> Gets you a random dad joke \n 🎀 39M!Socials --> See Elise her offical known socials \n 🎀 39M!MyAvatar --> Get your avatar or someones you want *Can only get up to one tag per message* \n 🎀 39M!8Ball --> Get a response from the beloved 8ball *requires a question*", color=0xfe3ee4)
helpEmbed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/139/222/6b8.gif")
helpEmbed.set_footer(text="🎀 Someone asked for help? 🎀")

async def onHelpMessage(message): 
  await message.channel.send("<:MikuStare:714726830703247362> You wanted to know what i can do hang on ** Searching for info ** <:Cute:879363818982084618>")
  await message.channel.send(embed=helpEmbed)

async def GetAvatar(message, member):
  if(member == "null"):
    member = message.author

  avatarEmbed = discord.Embed(title="Found {0.display_name} avatar".format(member), description="I found the following avatar for you", color=0xfe3ee4)
  avatarEmbed.set_footer(text="🎀 Pictures Left and right? 🎀")
  avatarEmbed.set_image(url=member.avatar_url)
  
  await message.channel.send("I found something for you {0.author.display_name}".format(message))
  await message.channel.send(embed=avatarEmbed)

async def EightBallResponse(message):
  response = [
     "🎱 8ball said you should rethink that one chief",
    "Is it <:MikuStare:714726830703247362>",
    "I say without a doubt <:MikuJudge:816647811092840479>",
    "<:MikuBlush:757984284052029500> I might saw that",
    "Just forget about it sweet heart 💜 ",
    "As I see it...... Well cant tell you <:MikuDerp:817310369772339200> ",
    "🎱 said yes",
    "Hella No <:mikuded:856532754715377664>",
    "For once a good question my friend i see it as a yes",
    "<:MikuStare:714726830703247362> no",
    "<:MikuStare:714726830703247362> Signs point to yes",
    "Just Forget about it chief"
  ]
  await message.channel.send(random.choice(response) + " {0.author.mention}".format(message))

async def BlackListedWords(message, client):
  channel = client.get_channel(822837640872067082)
  
  EmbedWords = discord.Embed(title="Found a banned word by {0.author.display_name}".format(message), description="said **{0.content}** and it contains a bad word so i deleted it".format(message), color=0xff0000)
  EmbedWords.set_footer(text="🎀 Banned words 🎀")
  EmbedWords.set_author(name="{0.author.name}".format(message), icon_url="{0.author.avatar_url}".format(message))
  await channel.send(embed=EmbedWords)
