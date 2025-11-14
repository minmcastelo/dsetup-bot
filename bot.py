import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

# Loads environment variables from the .env file
load_dotenv()

# Pulls your bot token from the environment
token = os.getenv("DISCORD_TOKEN")

# Sets up the bot's intents (Discord doesn't give message content by default)
intents = discord.Intents.default()
intents.message_content = True

# Creates the bot instance with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# Fires when the bot successfully logs in
@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")  # Prints the bot's username for confirmation

# A simple test command: replies "pong!" when someone types !ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

# Starts the bot using the token
bot.run(token)
