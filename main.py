import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()                     # load variables from .env
TOKEN = os.getenv("TOKEN")        # read the token

    # ... your existing imports and bot setup ...

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
        print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
        await ctx.send("👋 Hello! I'm out there vro ! Whatchu wanna mod?")

@bot.command()
async def ping(ctx):
        await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)} ms")

@bot.command()
async def say(ctx, *, message):
        await ctx.send(message)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason="No reason"):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f"👢 Kicked {member} | Reason: {reason}")
        else:
            await ctx.send("You don't have permission to do that.")
bot.run(TOKEN)