import requests

#https://icanhazdadjoke.com/api Api used

async def onJoke(message):
  response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json", "User-Agent": "https://github.com/justinvandelaar/Discord-Bot"})
  jokeData = response.json();
  await message.channel.send(jokeData['joke'])