import discord


async def BuildEmbed(message, embedTitle, embedDescription, imageUrl, colour,
                     footer, channel):
    newEmbed = discord.Embed(title=embedTitle, description=embedDescription)
    if not colour:
        newEmbed.colour = 0xfe3ee4
    else:
        newEmbed.colour = colour
    if len(imageUrl) > 0:
        newEmbed.set_image(url=imageUrl)
    newEmbed.set_footer(text=footer)
    if message is None:
      await channel.send(embed=newEmbed)
    else: 
      await message.channel.send(embed=newEmbed)