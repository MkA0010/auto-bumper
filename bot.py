import os
import discord
from discord.ext import tasks

TOKEN = "MTUyNzI0Mzc5MzAxMzkzMjAzNw.Gly200.I_NNYfxduazLfGiggEXrvVnqc9ymoEY6GER3TM"

CHANNEL_ID = 1490472870353174528

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot działa!")
    send_message.start()

@tasks.loop(minutes=10)
async def send_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("!daily")

client.run(TOKEN)