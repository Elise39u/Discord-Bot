import os
import discord
from server_ import keep_alive
from serverJoin import onMemberJoin
from serverLeave import onMemberLeave
from socials import onSocialsMessage
from Jokes import onJoke
from TextToOwO.owo import text_to_owo
import messages
import moderation
import youtube
import roles

activity = discord.Activity(type=discord.ActivityType.playing,
                            name="Traveling through Sekais with Elise")
my_secret = os.environ['TOKEN']
client = discord.Client(intents=discord.Intents.all(), activity=activity)
blackListedWords = ["kanker", "cancer", "https://discord.gg/", "tranny"]


#Register an event and define when the bot is ready to use
@client.event
async def on_ready():
    print("I have launched with {0.user}".format(client))
    youtube.checkforVideos.start(client)

@client.event
async def on_message_edit(beforeMessage, afterMessage):
  await moderation.UpdatedMessage(client, beforeMessage, afterMessage)

@client.event
async def on_message_delete(message):
  if message.author == client.user or "39M!" in message.content:
    return
  else:
    await moderation.DeleteMessage(message, client)

#Function to check for a message
#The on_message function can take a argument
@client.event
async def on_message(message):
    if message.author == client.user:
        return

      
    if len(message.content) > 0:
        for word in blackListedWords:
            if word in message.content.lower():
                roleCheck = moderation.checkOwnerRoles(message, False)
                if (roleCheck == False):
                    await message.delete()
                    await message.channel.send('https://cdn.discordapp.com/attachments/997798399728418867/997798441004568597/unknown.png')
                    await message.channel.send(
                        "{0.author.mention} You said a blacklisted word".
                        format(message))
                    await messages.BlackListedWords(message, client)

    #Check of the messages starts with 39!M and then await a sendback depending on the message command
    if message.content.startswith('39M!Hello'):
        await message.channel.send(
            "Hello there i`m Hatsune miku can i help you with something? {0.author.display_name} \nI suggested if you want to know what i can do by using 39M!Help \nOther wise feel free to look around here in the sekai world"
            .format(message))

    if message.content.startswith('39M!Vocaloid'):
      await messages.RandomVocaloid(message)

    if message.content.startswith('39M!Woah'):
      await message.delete()
      await message.channel.send('https://cdn.discordapp.com/attachments/997798399728418867/997798441004568597/unknown.png')
      
    if message.content.startswith('39M!Point'):
      await message.delete()
      await message.channel.send('https://cdn.discordapp.com/attachments/847134276448288830/1038796885240066089/point.png')  
    
    if message.content.startswith('39M!Roles'):
      await message.delete()
      await roles.give_role_menu(client, message, message.author)

    if message.content.startswith('39M!ThemeSong'):
      await message.channel.send("Want to know what song describes my life the best? \nWell lets says that doning the cosplays streams transformed into a rather weird person.\nI often had friends ask me:\nElise are you Hatsune Miku?, Is Hatsune miku you alter ego?. How fun it would look but nope\nI mean also you guys called me at a point Hatsune Miku or Hatsune juju\n\nSo that is why i say As long i can put a smile on your face as Hatsune miku.\nI will be Hatsune miku for you guys and girls!\n https://www.youtube.com/watch?v=ygY2qObZv24")

    if message.content.startswith('39M!Name'):
      await message.channel.send("So you want to know how i oringally got the name Hatsune juju?\nWell its one given by my friends from bening such a Miku lover.\nAt first i dindt took the name because it felt weird to be named with the same name as your idol.\n\nOnly at a point i asked you guys and you all seemed to want me to do it.\nSo thats how i became Hatsune Juju")
      
    if message.content.startswith('39M!108'):
      await message.delete()
      await message.channel.send(f'{message.author.name} you want to know the secrets of project diva. Here you go https://108memo.jp/en/')
      
    if message.content.startswith('39M!Socials'):
        await onSocialsMessage(message)

    if message.content.startswith('39M!Joke'):
        await onJoke(message)

    if message.content.startswith('39M!Help'):
        await messages.onHelpMessage(message)

    if message.content.startswith('39M!Elise'):
        await messages.EliseGenderStory(message)

    if message.content.startswith('39M!LMS'):
        await messages.LMSStory(message)

    if message.content == '39M!Cosplay':
      await messages.Cosplay(message)

    if message.content == '39M!CosplayIdeas':
      await messages.CosplayIdeas(message)

    if message.content.startswith('39M!Covers'):
      await messages.Covers(message)

    if message.content.startswith('39M!MyAvatar'):
        if (len(message.mentions) == 1):
            await messages.GetAvatar(message, message.mentions[0])
        else:
            await messages.GetAvatar(message, message.author)

    if message.content.startswith('39M!8Ball') and len(message.content) > 11:
        await messages.EightBallResponse(message)
    elif message.content.startswith('39M!8Ball') and len(message.content) < 11:
        await message.channel.send(
            "I miss a question {0.author.mention}".format(message))

    if message.content.startswith('39M!OwO') and len(message.content) > 7:
      await message.delete()
      await message.channel.send(text_to_owo(message.content[7:]))
    elif message.content.startswith('39M!OwO') and len(message.content) <= 7:
      await message.delete()
      await message.channel.send(text_to_owo(f"{message.author.display_name} please add a text for me to OWO. Love Miku"))

    if message.content.startswith('39M!Say') and len(message.content) > 7 and "@everyone" not in message.content and "@here" not in message.content:
      await message.delete()
      await message.channel.send(message.content[7:])
    elif message.content.startswith('39M!Say') and len(message.content) > 7 and "@everyone"  in message.content:
      await message.delete()
      await message.channel.send(f"{message.author} please dont use the everyone tag")
    elif message.content.startswith('39M!Say') and len(message.content) > 7 and "@here" in message.content:
      await message.delete()
      await message.channel.send(f"{message.author} please dont use the here tag")
    elif message.content.startswith('39M!Say') and len(message.content) <=7:
      await message.delete()
      await message.channel.send(f"{message.author} im not gonna say my own command uwu!")
  

    if message.content.startswith('39M!WristWorld'):
      await message.delete()
      await message.channel.send("You’ve 📡👨 seen 👀👤🎅🏻 Miku on 🔛 stage, 4️⃣💖 but 😠 what 👏🏼 about 🥴 your 👉 wrist? ⌚💯 Wrist ⌚💯 World 🌍 is an AR game 🎯 using 😏 wristbands, now 🫂 featuring Hatsune Miku! Collect songs, dances, and even ✋ save 🦎 the world! 🌍 Do 👀 You 👀👦 Wrist ⌚💯 World? 🌎 wrist ⌚💯 world 🌍🌎🌏")

    if message.content.startswith('39M!ShitPost'):
      await message.channel.send("I just need to get this out of my system because god dang is this game hard 😠. I've beaten Elden Ring, done nightmare in Doom Eternal, played Osu for a bit, done a lot of SIF, some Bandori, some Cytus 1-2 but I feel like none of that could have prepared me for how difficult this game actually is 🤨. I finally got my hands on it for Steam yesterday and I'm just genuinely shocked at how bad I am in this game 🥺. \n\n I could usually manage 200 in combos in games like Bandori on hard-expert difficulty 😤 but I genuinely could not get a single 100 combo on any song I tried 😠. Among the songs I've tried were Dune, Sweet Devil, Happiness committee, Freely Tomorrow on medium difficulty and the highest I could ever average throughout them were 55%~ 🥺 \n\n Is there any general advice to get better at the game besides just playing the same beat map? 🥺 A general problem I have is hitting a lot of safe notes, I rarely miss notes unless I choke but I am hitting a lot of massive safe breaking combos. Challenge Time unironically for once, actually gives me a challenge for once. I've choked a couple of times in my 2 hour play through. 🥺")

    
    if message.content.startswith('39M!Kick'):
        haha = False
        roleCheck = moderation.checkModRoles(message, haha)
        if (roleCheck):
            imuunRole = moderation.checkAdminRole(message.mentions[0], haha)
            if (imuunRole):
                await moderation.ErrorMessage(
                    message,
                    "An error occured with the 39M!Kick command. Hang om im looking into the issue <:MikuStare:1048727307612868640>>",
                    "I cant kick people with the role Vocaloid or Manager or Myself",
                    message.author)
            else:
                await moderation.OnKick(message, client)
        else:
            await moderation.ErrorMessage(
                message,
                "An error occured with the 39M!Kick command. Hang om im looking into the issue <:MikuStare:1048727307612868640>",
                "Lacks the permissions to use this command", message.author)


#Check if a member has left or joined the guild
@client.event
async def on_member_join(member):
    await onMemberJoin(member, client)


@client.event
async def on_member_remove(member):
    await onMemberLeave(member, client)
  
#client.run to run the bot with the secret token
#Also check if the request limit has reached anf if so restart the bot
keep_alive()
try:
    client.run(my_secret)
except:
    print("at except")
    os.system("kill 1")
    client.run(my_secret)
