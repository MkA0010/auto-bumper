import os
import discord
from discord.ext import tasks

TOKEN = os.getenv("TOKENMTUyNzI0Mzc5MzAxMzkzMjAzNw.G05KnI.ghqTTPp9W3JuvIbLCVkQsi8PlacRyijepf0orw"MTUyNzI2MzU4NTgzMzU4Njg0Mg.GV3qRg.pVrJ0ahf1EeS4AJPQo-6-n9JLi7U_QA2IefMto)

CHANNEL_ID = 1490472870353174528

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot działa!")
    send_message.start()

@tasks.loop(minutes=120)
async def send_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("/bump")

client.run(TOKEN)
