import json
import requests 
import re
import urllib
import urllib.request
import EmbedBuilder
from discord.ext import tasks

@tasks.loop(seconds=60)
async def checkforVideos(client):
  with open("youtubeJson.json", "r") as ytData:
    data=json.load(ytData)

    for youtube_channel in data:
      channel = f"https://www.youtube.com/channel/{youtube_channel}"

      #getting html of the /videos page
      html = requests.get(channel+"/videos").text

      #try to get the latetes video url
      #anwsers used from stackoverflow 
      #https://stackoverflow.com/questions/59627108/retrieve-youtube-video-title-using-api-python
      #https://github.com/AdvicSaha443/Discord.py-Youtube-Notification-Bot/blob/main/main.py
      #https://www.youtube.com/watch?v=qZ6kcQJxbzQ          #https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html
      #discord.ext.tasks.Loop.start
      
      try:
        latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
      except:
        continue
 
      if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
        
        #chaning the last video url
        data[str(youtube_channel)]["latest_video_url"] = latest_video_url

        #Dumping the new youtube lateste url into the json file
        with open("youtubeJson.json", "w") as ytJson:
          json.dump(data, ytJson)

        discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
        discord_channel = client.get_channel(int(discord_channel_id))

        vidId = re.search('(?<="videoId":").*?(?=")', html).group()
        parmas = {"format": "json", "url": latest_video_url}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(parmas)
        url = url + "?" + query_string
        
        with urllib.request.urlopen(url) as response:
          response_text = response.read()
          data = json.loads(response_text.decode())
          if("Perfect" in data['title'] or "Divaroadmap" in data["title"]):
            vidTitle = "<@&934500064364216390> <@203095887264743424> has uploaded a Project diva video go check it out 💜"
            embedTitle = "Project diva video"
            embedDescription = "🎀 Elise has uploaded a new project diva video. Care to see if she got a perfect or got a new divaroadmap. See what happends by checking the title of the embed 🎀"
          elif("Megamix" in data["title"] or "AFT" in data["title"] or "Diva" in data["title"] or "Future tone" in data["title"]):
            vidTitle = " 🎀 <@&934500064364216390> <@203095887264743424> has uploaded a recent project diva stream to her vods channel 🎀"
            embedTitle = "Miku/Project Diva stream"
            embedDescription = "🎀 Elise recently streamed a project diva game to her twitch. After downloading and maby a little bit editing. Its finally uploaded to her vods channel. Interested to see what happends on a stream click the title of the embed 🎀"
          elif("Stream" in data["title"]):
            vidTitle = " 🎀 <@&934500064364216390> <@203095887264743424> has uploaded a reccent stream to her vods channel 🎀"
            embedTitle = "Recent twitch stream"
            embedDescription = "🎀 Elise recently streamed something because sometimes it hard to tell what. Well here i see a upload so. After downloading and maby a little bit editing. Its finally uploaded to her vods channel. Interested to see what happends on a stream click the title of the embed 🎀"
          else:
            vidTitle = "<@&934500064364216390> <@203095887264743424> has uploaded a lets play video. Go check it out 💜"
            embedTitle = "Lets play video"
            embedDescription = "🎀 Elise has uploaded a new lets play video. Is it horror or a fun lets play video. Well its hard to tell but i see a new upload so. Care to check it out? Click on the title to take you to the vid. 🎀"

          await discord_channel.send(vidTitle)
          await EmbedBuilder.BuildEmbed(None, embedTitle, embedDescription, "http://img.youtube.com/vi/" + vidId + "/0.jpg", None, "🎀 New Vid Upload 🎀", discord_channel, latest_video_url)