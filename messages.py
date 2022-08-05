import discord
import random
import EmbedBuilder


async def onHelpMessage(message):
    await message.channel.send(
        "<:MikuStare:714726830703247362> You wanted to know what i can do hang on ** Searching for info ** <:Cute:879363818982084618>"
    )
    await EmbedBuilder.BuildEmbed(
        message, "I found my commands. *Whistele noises*",
        "We have the following commands but first its good to know my prefix is 39M!. Most commands are also case senstive so be aware \n 🎀 39M!Help --> Show this message \n 🎀 39M!Hello --> Says hello to you \n 🎀 39M!Joke --> Gets you a random dad joke \n 🎀 39M!Socials --> See Elise her offical known socials \n 🎀 39M!MyAvatar --> Get your avatar or someones you want *Can only get up to one tag per message* \n 🎀 39M!8Ball --> Get a response from the beloved 8ball *requires a question* \n 🎀 39M!Elise --> *Wanna know what lead up to my transgender choices? Or want to know ho i dealt with some stuff your wondering yourself about?*",
        "https://i.kym-cdn.com/photos/images/original/001/139/222/6b8.gif",
        0xfe3ee4, "🎀 Someone asked for help? 🎀", None, None)


async def GetAvatar(message, member):
    if (member == "null"):
        member = message.author

    await message.channel.send(
        "I found something for you {0.author.display_name}".format(message))
    await EmbedBuilder.BuildEmbed(
        message, "Found {0.display_name} avatar".format(member),
        "I found the following avatar for you", member.avatar_url, 0xfe3ee4,
        "🎀 Pictures Left and right? 🎀", None, None)


async def EightBallResponse(message):
    response = [
        "🎱 8ball said you should rethink that one chief",
        "Is it <:MikuStare:714726830703247362>",
        "I say without a doubt <:MikuJudge:816647811092840479>",
        "<:MikuBlush:757984284052029500> I might saw that",
        "Just forget about it sweet heart 💜 ",
        "As I see it...... Well cant tell you <:MikuDerp:817310369772339200> ",
        "🎱 said yes", "Hella No <:mikuded:856532754715377664>",
        "For once a good question my friend i see it as a yes",
        "<:MikuStare:714726830703247362> no",
        "<:MikuStare:714726830703247362> Signs point to yes",
        "Just Forget about it chief"
    ]
    await message.channel.send(
        random.choice(response) + " {0.author.mention}".format(message))


async def BlackListedWords(message, client):
    channel = client.get_channel(822837640872067082)

    EmbedWords = discord.Embed(
        title="Found a banned word by {0.author.display_name}".format(message),
        description=
        "said **{0.content}** and it contains a bad word so i deleted it".
        format(message),
        color=0xff0000)
    EmbedWords.set_footer(text="🎀 Banned words 🎀")
    EmbedWords.set_author(name="{0.author.name}".format(message),
                          icon_url="{0.author.avatar_url}".format(message))
    await channel.send(embed=EmbedWords)


async def EliseGenderStory(message):
    myid = '<@203095887264743424>'
    await EmbedBuilder.BuildEmbed(
        message, "Elise Her Gender Story",
        "Well we all know our beloved juju do we. Well after LMS she got quite some time to think. Oh dindt you know yet? Well its true. Juju now goes by Elise and she started here with it in our vocaloid group. So what happend to lead to her transgender thoughts \n\n So go with Me Hatsune Miku and our new beloved girl Elise on a muscial trip. We explore the past few years and what happend to Elise. We also sing songs from your favourite diva game together after each story. \n\n Well its manily me and Elise but watch the story and also see other of your favourite vocaloids or well mine close friends. We would sing our way across the last few years and give your insight in some decisions. Choices from what lead up to the choice of her trans thoughts and some choices for twitch/yt. \n\n So interested how Elise decided to became a girl. Click the title of the emebed",
        "https://cdn.discordapp.com/attachments/709057115159003156/948212388925157436/unknown.png",
        "", "🎀 Elise her story 🎀", None,
        "https://www.youtube.com/playlist?list=PLNc-vlTat7viUYY1BuxU1T563gskQpvJJ"
    )
