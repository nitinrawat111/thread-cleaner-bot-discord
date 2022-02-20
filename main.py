import discord
import os

DELETE_CAPACITY = 250
client = discord.Client()

def messageChecker(message):
  return True

@client.event
async def on_ready():
  print("Logged in as " + client.user.name)

@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  if(message.content == "$clear"):
    await message.channel.purge(limit = DELETE_CAPACITY, bulk = True)
    

client.run(os.environ['TOKEN'])