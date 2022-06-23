import requests

#https://icanhazdadjoke.com/api Api used
#Error handeling adding due to the fact last time the bot crashed
#This expected due to a error with recving a joke from the api

async def onJoke(message):
  response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json", "User-Agent": "https://github.com/justinvandelaar/Discord-Bot"})
  jokeData = response.json();
  if(jokeData['status'] == 200):
    await message.channel.send(jokeData['joke'])
  else:
    await message.channel.send("A error occured and i got back: " + jokeData['status'] + " please contact my owner Hatsune Elis for more help")