import discord

helpEmbed=discord.Embed(title="I found my commands. *Whistele noises*", description="We have the following commands but first its good to know my prefix is 39M!. Most commands are also case senstive so be aware \n 🎀 39M!Help --> Show this message \n 🎀 39M!Hello --> Says hello to you \n 🎀 39M!Joke --> Gets you a random dad joke \n 🎀 39M!Socials --> See Elise her offical known socials", color=0xfe3ee4)
helpEmbed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/139/222/6b8.gif")
helpEmbed.set_footer(text="🎀 Someone asked for help? 🎀")

async def onHelpMessage(message): 
  await message.channel.send("<:MikuStare:714726830703247362> You wanted to know what i can do hang on ** Searching for info ** <:Cute:879363818982084618>")
  await message.channel.send(embed=helpEmbed)