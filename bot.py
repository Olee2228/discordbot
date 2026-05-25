import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist online!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("MTQ4OTcwOTAxNTUxNTUyOTMwNg.G5b_RY.Cutr7dpjdIY3xWMrNp6CO37CvJRmJX-xqIg0WM"))
