import asyncio

async def give_role_menu(client, message, member):
  roleMessage = await message.channel.send(f"""{member.display_name} Welcome we have the following roles  for you. They give a nice color and are based on the Sekai themed game 
  
  (🎵) Virtual Siner --> Teal \n 
  (🎸) Leo/Need --> Dark Blue \n
  (🎼) More More Jump --> Darker YellowGreen \n
  (☕) Vivid Bad Squad --> Magenta colored \n
  (🎡) Wonderland X Showtime --> Orange \n
  (💻) NightCord 25:00 --> Purple

  Please respond with the correct emote for the correct role. **You have 30sec and the top role wil be your color role**
  """)

  try:
    reaction = await client.wait_for('reaction_add', timeout=30.0)
    await giveUserRole(message, client, member, reaction, roleMessage)
  except asyncio.TimeoutError:
    await roleMessage.delete()
    await message.channel.send(f"**30 seconds** has passed and i dindt saw a emoji reaction **{message.author.display_name}**")

async def giveUserRole(message, client, member, reaction, roleMessage):
  Guild = client.get_guild(699557641818734634)

  if member != client.user:
    if str(reaction[0]) == "🎵":
      role = Guild.get_role(1010980678998949938)
    if str(reaction[0]) == "🎸":
      role = Guild.get_role(1010980219038990387)
    if str(reaction[0]) == "🎼":
      role = Guild.get_role(1010981513849995425)
    if str(reaction[0]) == "☕":
      role = Guild.get_role(1010981914104041572)
    if str(reaction[0]) == "🎡":
      role = Guild.get_role(1010982791623745606)
    if str(reaction[0]) == "💻":
      role = Guild.get_role(1010983272806883399)

  await roleMessage.delete()
  await checkRoleState(role, member, message)


async def checkRoleState(role, member, message):
  roleCheck = False
  for userRole in member.roles:
    if userRole.name == role.name:
      roleCheck = True
      break;

  if roleCheck == False:
    await member.add_roles(role)
    await message.channel.send(f"{member.display_name} i have given you the following role: {role.name}")
  else:
    await member.remove_roles(role)
    await message.channel.send(f"{member.display_name} i have removed the following role: {role.name}")