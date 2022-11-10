import discord

async def OnKick(message, client):
  message_array = message.content
  user = await client.fetch_user(message.mentions[0].id)
  await message.guild.kick(user, reason=message_array[2])
  await message.channel.send(f'{user} has been kicked for {message_array}')
  channel = client.get_channel(822837640872067082)
  
  EmbedKicked = discord.Embed(title=f"Someone has been kicked by {message.author.display_name}", description=f"**{user.display_name}** been kicked with the following reason {message_array}", color=0xff0000)
  EmbedKicked.set_footer(text="🎀 Someone is kicked 🎀")
  await channel.send(embed=EmbedKicked)

def checkModRoles(message, boolean):
  for userRole in message.author.roles:
    if userRole.name == 'Vocaloids' or userRole.name == 'Managers':
      boolean = True
      break;
  return boolean

def checkOwnerRoles(message, boolean):
  for userRole in message.author.roles:
    if userRole.name == 'Vocaloids':
      boolean = True
      break;
  return boolean
  
def checkAdminRole(member, boolean):
  for userRole in member.roles:
   if userRole.name == 'Vocaloids' or userRole.name == 'Managers' or userRole.name == 'Sekai Miku Bot': 
     boolean = True
     break;
  return boolean
  
async def ErrorMessage(message, description, reason, user):
  embed = discord.Embed(title="Something went wrong", description=f"{description}")
  embed.add_field(name="Error:", value=f'{reason}')
  embed.colour = 0xfe3ee4
  embed.set_footer(text="Error: " + user.display_name)
  await message.channel.send(content=None, embed=embed)

async def UpdatedMessage(client, beforeMessage, afterMessage):
  member = beforeMessage.author

  if member == client.user:
        return
    
  updateEmbed = discord.Embed(title=f"I saw someone updated their message in {beforeMessage.channel.name}", description=f"Message before was: **{beforeMessage.content}** \n New update message is: **{afterMessage.content}**")
  updateEmbed.add_field(name="**Link to message**", value=f"{beforeMessage.jump_url}", inline=True)
  updateEmbed.set_author(name=f"{beforeMessage.author.display_name}", icon_url=member.avatar_url)

  channel = client.get_channel(822837640872067082)
  
  await channel.send(embed=updateEmbed)

async def DeleteMessage(message, client):
  member = message.author
  
  if member == client.user:
        return
    
  deletedEmbed = discord.Embed(title=f"A message has been deleted in {message.channel.name}", description=f"{member.display_name} has deleted **{message.content}**")       
  deletedEmbed.add_field(name="**Link to channel**", value=f"{message.jump_url}", inline=True)
  deletedEmbed.set_author(name=f"{member.display_name}", icon_url=member.avatar_url)
  
  channel = client.get_channel(822837640872067082)
  
  await channel.send(embed=deletedEmbed)