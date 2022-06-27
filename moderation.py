import discord

async def OnKick(message, client):
  message_array = message.content[28:]
  user = await client.fetch_user(message.mentions[0].id)
  await message.guild.kick(user, reason=message_array[2])
  await message.channel.send(f'{user} has been kicked for {message_array}')
  channel = client.get_channel(822837640872067082)
  
  EmbedKicked = discord.Embed(title=f"Someone has been kicked by {message.author.display_name}", description=f"**{user.display_name}** been kicked with the following reason {message_array}", color=0xff0000)
  EmbedKicked.set_footer(text="🎀 Someone is kicked 🎀")
  await channel.send(embed=EmbedKicked)

def checkRole(message, boolean):
  for userRole in message.author.roles:
    if userRole.name == 'Vocaloids' or userRole.name == 'Managers':
      boolean = True
      break;
  return boolean

def checkAdminRole(member, boolean):
  for userRole in member.roles:
   if userRole.name == 'Vocaloids' or userRole.name == 'Managers' or userRole.name == 'Big Debut Miku': 
     boolean = True
     break;
  return boolean
  
async def ErrorMessage(message, description, reason, user):
  embed = discord.Embed(title="Something went wrong", description=f"{description}")
  embed.add_field(name="Error:", value=f'{reason}')
  embed.colour = 0xfe3ee4
  embed.set_footer(text="Error: " + user.display_name)
  await message.channel.send(content=None, embed=embed)
