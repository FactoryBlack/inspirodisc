import os
import discord
from discord.ext import commands
import requests

token = os.getenv("DISCORD_BOT_TOKEN")  # grabbed from Pelican's environment

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def inspire(ctx):
    try:
        url = "https://inspirobot.me/api?generate=true"
        resp = requests.get(url)
        image_url = resp.text
        await ctx.send(image_url)
    except Exception as e:
        print(e)
        await ctx.send("Oops, couldn't fetch inspiration now.")

bot.run(token)
