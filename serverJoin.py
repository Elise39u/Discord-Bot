import random
import discord

embedWelcomeURLS = ["https://i.kym-cdn.com/photos/images/original/001/236/970/0f1.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329033756672030/LTWB_Micrystal.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329293066108936/2ffuym.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861329462636183602/ezgif.com-gif-maker_3.gif" ,"https://cdn.discordapp.com/attachments/757611689003974779/861329538398552084/ezgif-3-f1b581708e09.gif", "https://media.tenor.com/images/7452b9709e58ee148807ca1637ea308d/tenor.gif"]
imageUrl = random.choice(embedWelcomeURLS)

embed=discord.Embed(title="🎀 Welcome we have some usual information 🎀", description="We have a few rules and things to look out for here 💖 \n <#703637751274143854> <-- Channel where you can find the rules of the server 🎀 \n <#797792369416208386>  <-- For some information on the server 🎀 \n <#699557641818734638> <-- Main  chat 🎀 \n  <#709050194662260797> <-- channel  for some roles  🎀", color=0xfe3ee4)
embed.set_image(url=imageUrl)
embed.set_footer(text="🎀 Welcome to elise her hangout 🎀")
#await ctx.send(embed=embed)

async def onMemberJoin(member, client):
  channel = client.get_channel(797789187910664193)
  role = member.guild.get_role(699572966551322635)
  await channel.send("{0.mention} welcome to Elise her hangout".format(member))
  await channel.send(embed=embed)
  await member.add_roles(role)