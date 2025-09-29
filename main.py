import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  


load_dotenv()                     
TOKEN = os.getenv("TOKEN")        

   


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

autorole_name = "Agent"  # role name

@bot.command()
@commands.has_permissions(administrator=True)
async def set_autorole(ctx, *, role_name):
        global autorole_name
        autorole_name = role_name
        await ctx.send(f"✅ Auto-role set to **{role_name}**")

@bot.command()
async def autorole(ctx):
    """Check the current auto-role"""
    await ctx.send(f"ℹ️ Current auto-role is: **{autorole_name}**")

@bot.event
async def on_member_join(member):
        # --- Welcome channel ---
        channel = discord.utils.get(member.guild.text_channels, name="welcome👋")
        if channel:
            await channel.send(f"🎉 Welcome {member.mention} to **{member.guild.name}**! 🐝")

        # --- Auto-role ---
        role = discord.utils.get(member.guild.roles, name=autorole_name)
        if role:
            try:
                await member.add_roles(role)
                print(f"✅ Assigned {role.name} to {member.name}")
            except Exception as e:
                print(f"❌ Failed to assign role: {e}")

        # --- DM the new member ---
        try:
            await member.send(
                f"👋 Hey {member.name}! Welcome to **{member.guild.name}**! "
                f"Read the rules and say hi. I’ve also given you the **{autorole_name}** role 🐝"
            )
        except:
            print(f"⚠️ Couldn't DM {member.name}")




bot.run(TOKEN)
