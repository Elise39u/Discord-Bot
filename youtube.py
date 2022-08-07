import json
import requests 
import re
import urllib
import urllib.request
from discord.ext import tasks

@tasks.loop(seconds=7200)
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
      #https://www.youtube.com/watch?v=qZ6kcQJxbzQ          #https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html#discord.ext.tasks.Loop.start
      
      try:
        latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
      except:
        continue
 
      if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
        
        #chaning the last video url
        data[str(youtube_channel)]["latest_video_url"] = latest_video_url

        #Dumping the new youtube lateste url into the json file
        with open("youtube.json", "w") as ytJson:
          json.dump(data, ytJson)

        discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
        discord_channel = client.get_channel(int(discord_channel_id))

        params = {"format": "json", "url": latest_video_url}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(parmas)
        url = url + "?" + query_string
        
        with urllib.request.urlopen(url) as response:
          response_text = response_read()
          data = json.loads(response_text.decode())
          await discord_channel.send("Dont worry Elise is testing something no panic ")
          await discord_channel.send(data['title'])