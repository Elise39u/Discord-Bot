import random
import EmbedBuilder

embedLeaveUrls = ["http://24.media.tumblr.com/5f8223ae07c725cea7a77be14c45a55d/tumblr_mlor7isREZ1s96b9jo1_500.gif", "https://data.whicdn.com/images/104730073/original.gif", "https://cdn75.picsart.com/185243629000202.gif?to=min&r=640", "https://cdn.discordapp.com/attachments/757611689003974779/861351458824781875/ezgif-6-00b29df6c68e.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861351473162223656/ezgifmaker.gif", "https://i.pinimg.com/originals/d4/19/73/d419735eb285e55e0a38093683fb3503.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861351713444331550/Hibana.gif"]
imageUrl = random.choice(embedLeaveUrls)


async def onMemberLeave(member, client):
  channel = client.get_channel(797789187910664193)
  await channel.send("Oh Goodbye {0.name} We hope you return one day again to this sekai".format(member))
  await EmbedBuilder.BuildEmbed(None, "Wait someone disappeared", "I saw that someone left the gamergirl sekai. I hope they will come back one day with more games :'(. <:Cute:879363818982084618>", imageUrl, 0xfe3ee4, "🎀 Someone has decided to leave the sekai 🎀", channel, None)