import discord
from discord.ext import commands, bridge


Token = 'Your Token Here.'


# Bot
intents = discord.Intents.all()
client = bridge.Bot(command_prefix="?", intents=intents)

# An event Handler
@client.event
async def on_ready():
    print(f"Logged In As : {bot.user}")

# A Bridge Command (Makes a command used by prefix and /)
@client.bridge_command(name="hello")
async def hi(ctx):
    await ctx.respond(f"Hello {ctx.author.mention}, How are You?")

client.run(Token)
