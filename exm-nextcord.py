import nextcord
from nextcord.ext import commands


Token = 'Your Token Here.'


# Bot
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged In As : {bot.user.name}")

@bot.command(name="hello", aliases=["hi", "ello"])
async def hi(ctx):
    await ctx.send(f"Hello {ctx.author.mention}, How are You?")

bot.run(Token)