import discord

helpEmbed=discord.Embed(title="I found my commands. *Whistele noises*", description="We have the following commands but first its good to know my prefix is 39M!. Most commands are also case senstive so be aware \n 🎀 39M!Help --> Show this message \n 🎀 39M!Hello --> Says hello to you \n 🎀 39M!Joke --> Gets you a random dad joke \n 🎀 39M!Socials --> See Elise her offical known socials \n 🎀 39M!MyAvatar --> Get your avatar or someones you want *Can only get up to one tag per message*", color=0xfe3ee4)
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
  avatarUrl = member.avatar_url
  avatarEmbed.set_image(url=avatarUrl)
  
  await message.channel.send("I found something for you {0.author.display_name}".format(message))
  await message.channel.send(embed=avatarEmbed)