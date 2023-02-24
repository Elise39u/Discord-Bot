import discord
import random
import EmbedBuilder


async def onHelpMessage(message):
    await message.channel.send(
        "<:MikuStare:1048727307612868640> You wanted to know what i can do hang on ** Searching for info ** <:Cute:879363818982084618>"
    )
    await EmbedBuilder.BuildEmbed(
        message, "I found my commands. *Whistele noises*",
        "We have the following commands but first its good to know my prefix is 39M!. Most commands are also case senstive so be aware \n 🎀 39M!Help --> Show this message \n 🎀 39M!Hello --> Says hello to you \n 🎀 39M!Joke --> Gets you a random dad joke \n 🎀 39M!Socials --> See Elise her offical known socials \n 🎀 39M!MyAvatar --> Get your avatar or someones you want *Can only get up to one tag per message* \n 🎀 39M!8Ball --> Get a response from the beloved 8ball *requires a question* \n 🎀 39M!Elise --> *Wanna know what lead up to my transgender choices? Or want to know ho i dealt with some stuff your wondering yourself about?* \n 🎀 39M!LMS --> *The LMS tag explained on youtube. Interested make sure to check out.* \n 🎀 39M!Roles --> *Want a sekai themed role color here is your menu. Changes role color. You also can remove the other roles from this menu with it.* \n 🎀 39M!ThemeSong --> *Curious what song describes my life the best?* \n 🎀 39M!Name --> *Wanna know how i became known as Hatsune Juju?* \n 🎀 39M!108 --> *get the secrets to Pjd?* \n 🎀 39M!OwO --> *OwOfiy your text* **Requies a text to be given** \n 🎀 39M!Cosplay --> *Get the list with current cosplays i own.* \n 🎀 39M!CosplayIdeas--> *Gain insight into cosplays i want to get later in life* \n 🎀 39M!Covers --> *Ever wonder how i sound while singing. Yeah i know you wouldnt but i do make covers if your interested*",       "https://64.media.tumblr.com/58a7faae192fe804e0b0a74a105124e8/448b302783b0d2a5-00/s540x810/3aa732a81923fafcae364c16fe38218d39a1198c.gif",
        0xfe3ee4, "🎀 Someone asked for help? 🎀", None, None)


async def GetAvatar(message, member):
    if (member == "null"):
        member = message.author

    await message.channel.send(
        "I found something for you {0.author.display_name}".format(message))
    await EmbedBuilder.BuildEmbed(
        message, "Found {0.display_name} avatar".format(member),
        "I found the following avatar for you", member.avatar, 0xfe3ee4,
        "🎀 Pictures Left and right? 🎀", None, None)

async def RandomVocaloid(message):
  vocaloidChoice = [
    "<:MikuStare:1048727307612868640> Hatsune Miku",
    "<:LukaStare:813132474082525215> Megurine Luka",
    "<:RinStare:816647976129921082> Kagamine Rin",
    "<:LenStare:878744221501227018> Kagamine Len",
    "<:MeikoStare:816647748135682058> Meiko",
    "<:KaitoStare:878744250207055892> Kaito",
    "<:GumiStare:816647571216007178> Gumi",
    "<:IaStare:813132456315322399> IA"
  ]
  randomChoice = ["Is the best for sure <3", "Is the worst sorry", "Well i dont know about this vocaloid one"]

  await message.channel.send(random.choice(vocaloidChoice))
  await message.channel.send(random.choice(randomChoice) + f" {message.author.display_name}")
  
async def EightBallResponse(message):
    response = [
        "🎱 8ball said you should rethink that one chief",
        "Is it <:MikuStare:1048727307612868640>",
        "I say without a doubt <:MikuJudge:816647811092840479>",
        "<:MikuBlush:757984284052029500> I might saw that",
        "Just forget about it sweet heart 💜 ",
        "As I see it...... Well cant tell you <:MikuDerp:817310369772339200> ",
        "🎱 said yes", "Hella No <:mikuded:856532754715377664>",
        "For once a good question my friend i see it as a yes",
        "<:MikuStare:1048727307612868640> no",
        "<:MikuStare:1048727307612868640> Signs point to yes",
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
                          icon_url="{0.author.avatar}".format(message))
    await channel.send(embed=EmbedWords)


async def EliseGenderStory(message):
    await EmbedBuilder.BuildEmbed(
        message, "Elise Her Gender Story",
        "What you never heared of Elise? Elis? Juju. Oh Hatsune Juju rings a bell well that is our girl. After the LMS adventure she had some time to think. Oh wait you dindt know yet that Elise is trans ohhh. Juju now goes by Elise indeed and she started it first here in our vocaloid group, then the school sekai and so on. So what happend that lead to her choice? \n\n Go with me Hatsune Miku and your girl Elise on a Musical Trip. We go on a journey through the past and see what happend to your streamer girl. Elise will explain certain thoughts behind certain actions. \n\n After that we close the story with a song. Its usally me and Elise but you can also expect: My friends like Luka, Rin Kaito etc... Also favourites from the sekais like the Leo/Need band or the Wonderland X Showtime Group!. \n\n As we sing our way across the last few years. Elise want to learn you something or tell you. Choices from how she tested out bening a woman, to getting you know fake tits, getting dress, makeup, HRT treatmant, Telling family and friends and well stuff about singing or twitch/yt. \n\n So interested how Elise decided to became a girl. Click the title of the emebed",
        "https://cdn.discordapp.com/attachments/709057115159003156/1005109230849773648/20220805144206_1.jpg",
        "", "🎀 Elise her story 🎀", None,
        "https://www.youtube.com/playlist?list=PLNc-vlTat7viUYY1BuxU1T563gskQpvJJ"
    )


async def LMSStory(message):
   await EmbedBuilder.BuildEmbed(
        message, "Luka missing story",
        "A fan fiction story about our beloved Girl Juju and her friend Hatsune Miku. Read through the story on how 2 girls waited one day on her friend luka. But she never seemed to appear at the place they were suppose to meet. \n\n Go on with Miku, Juju and  much more of their vocaloid friends on a musical tour. Watch as Juju and Miku travel across the world to find their missing friend luka. Go with the 2 as the travel and sing songs from your favourite diva games. \n\n Juju never sung before in her life. Can Miku teach her new friend to sing and be an artist. Or does the story have some weird and loving twits. Or does Juju really transform into a true artist girl? \n\n Find out by clicking on the title", "https://cdn.discordapp.com/attachments/709057115159003156/1005109230610694264/20220805144557_1.jpg",
        None, "🎀 LMS on youtube 🎀", None,
        "https://www.youtube.com/playlist?list=PLNc-vlTat7vhdoo6Zg6tL7VcMibwc74w6"
    )

async def Cosplay(message):
  await EmbedBuilder.BuildEmbed(message, "Cosplays Elises Owns", "So you want to know the cosplays that Elise owns. Well hold my leek and i will search it up. \n\n 1. Ofcourse the first cosplay that i could find was the OG miku costume. I meant my main outfit you know but oh well. \n 2. Oh when the snow comes we often change into a snow type. Elise has no difference she changes from time to time into Snow Elise 2019. Only the outfit is incomplete at the moment. She lost some pieces while moving so. \n 3. This one was a special one and one close to heart. She got a innocent dress. Its barely long enough but hey it was a fun one she had. \n 4. As last the one she loves the most. Its only a few sizes to big for her but that doesnt matter. Can ribbon girl Elise melt your hearts? \n\n This is it for now.", "https://www.goodsmileracing.com/en/wp-content/uploads/2014/10/Rmiku2017f.jpg", None, "🎀 Cosplay right here 🎀 \n🎀 last update: Sun 19 Feb 2023 🎀", None, None)
  
async def CosplayIdeas(message):
  await EmbedBuilder.BuildEmbed(message, "Cosplay Ideas Elise has", "So with owning cosplay usually also comes the ideas of new cosplay ideas. But which ideas has Elise in mind. Well she asked me to keep track of an list with ideas for now. *One not for now its only more focused on miku cosplays* \n\n 1. With Ribbon Girl bening opassed and moved to own a new most likey candidate. You prob seen it already in the cosplay command but its **Racing Miku 2017** She really likes the butterfly miku racing look. \n 2. One that has crossed her mind is the **Marai 2017 Look**. Why you may ask? Well idk she finds it cute and ofcurses links back to Suna no wakusei. \n 3. The list is for now short but Elise was also thinking about **Leo/Need Miku** or the **More More Jump Miku** Dress \n\n This is it for now. Expect more ideas coming soon \n *List is gonna expend later down the line*", "https://corocoro.jp/wp-content/uploads/2022/06/2a616a6471aea0f184e9d6643916906f.jpg", None, "🎀 Cosplay right here 🎀 \n🎀 last update: Sun 19 Feb 2023 🎀", None, None)

async def Covers(message):
  await EmbedBuilder.BuildEmbed(message, "Covers!!!", "Do you know that i make covers... No well i dont blame you.... \n\n Lets say that i plan on releasing one a month for 2023 but failed that already. So ever wonder how i sound while i sing. Make sure to click the title of the emebd then. I promise il get better i have to learn it here in my Girly Gamer Sekai. \n\n *You also can find it by going to my YT channel main page and scroll down*", "https://media.discordapp.net/attachments/709057115159003156/1076827279784681573/Screenshot_5.png?width=1199&height=678", None, "🎀 Cover List found here 🎀", None, "https://www.youtube.com/playlist?list=PLNc-vlTat7vj9kTilBCUuFl3wsOA1pQkV")