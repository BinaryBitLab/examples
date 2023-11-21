import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="mc!", intents=intents)
import random
@bot.event
async def on_ready():
    print(f"{bot.user.name} Online.")
import asyncio
@bot.command(name="suggest")
async def suggest(ctx, *, suggestion):
    chnl = bot.get_channel(1175357570769227776)
    emb = nextcord.Embed(
        title=f"Suggestion From {ctx.author.name}",
        description=f"{suggestion}",
        color=nextcord.Color.blurple()
    )
    emb.set_footer(text="Made By .wuid @ dsc.gg/binarybotlab")

    suggestion_message = await chnl.send(embed=emb)
    
    # Add reactions to the suggestion message
    await suggestion_message.add_reaction("✅")  # Check mark
    await suggestion_message.add_reaction("❌")  # X mark

    await ctx.message.delete()

@bot.command(name="roast", description="roast someone for you")
async def roast(ctx, member: nextcord.Member):
        skele_id = 868353670343954513
        mom_jokes = [
            f"Yo {member.mention}. Your mama is so old, she knew Gandalf before he had a beard!",
            f"Yo {member.mention}. Your mom is so slow, when she tried to catch up with the times, she got a calendar from 1995!",
            f"Yo {member.mention}. Your mama is so sweet, even sugar calls her 'Mom'!",
            f"Yo {member.mention}. Your mom is so caring, when you're sick, she can make chicken soup from scratch while solving a Rubik's Cube blindfolded!",
            f"Yo {member.mention}. Yo mama is so funny, she could make a grumpy cat smile!",
        ]

        random_joke = random.choice(mom_jokes)
        if member.id == skele_id:
            await ctx.send(f"Hey {member.mention}, {ctx.author.mention} is tryna roast you. Do you want me to ban 'em.")
        else:
            await ctx.send(random_joke)


@bot.command(name="sinfo", aliases=["guildinfo", "ginfo", "serverinfo"])
async def serverinfocmd(ctx):
    szz = ctx.guild.created_at
    emb = nextcord.Embed(
        title=ctx.guild.name,
        color=nextcord.Color.og_blurple(),
        description=f"Guild ID: {ctx.guild.id} \n Server Owner: {ctx.guild.owner.display_name} \n Member Count: {ctx.guild.member_count}"
    )
    emb.set_thumbnail(url=ctx.guild.icon.url)
    emb.add_field(name="Created At:", value=szz.strftime("%Y-%m-%d"))

    # Add Role Count
    emb.add_field(name="Role Count:", value=len(ctx.guild.roles))

    # Add Channel Count
    text_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, nextcord.TextChannel)])
    voice_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, nextcord.VoiceChannel)])
    category_channels = len(ctx.guild.categories)
    emb.add_field(name="Channel Count:", value=f"Text: {text_channels}\nVoice: {voice_channels}\nCategories: {category_channels}")

    emb.set_footer(text="© .wuid / WuidBotHosting | 2023")

    await ctx.send(embed=emb)


import requests

@bot.slash_command(name="kick", description="Kick A Member | reason, member")
@commands.has_permissions(ban_members=True)
async def kickuser(ctx, user: nextcord.Member, reason: str):
    try:
        await user.kick(reason=reason)
        await ctx.send(f"Kicked {user.mention} For {reason}")
    except nextcord.Forbidden:
        await ctx.send("Error: Permission Needed | I Dont Have Perms To Kick Users.")
    except Exception as e:
        await ctx.send("Error: Invaild Permissions")
        print(f"{e}")

@bot.command(name="kick", aliases=["k", "bick"])
@commands.has_permissions(ban_members=True)
async def kickuser(ctx, user: nextcord.Member, reason: str):
    try:
        await user.kick(reason=reason)
        await ctx.send(f"Kicked {user.mention} For {reason}")
    except nextcord.Forbidden:
        await ctx.send("Error: Permission Needed | I Dont Have Perms To Kick Users.")
    except Exception as e:
        await ctx.send("Error: Invaild Permissions")
        print(f"{e}")


@bot.slash_command(name="ban")
@commands.has_permissions(ban_members=True)
async def bancmd(ctx, user: nextcord.Member, reason):
    if ctx.author.id == 895788406347558922:
        await user.ban(reason=reason)
    else:
        try:
            await user.ban(reason=reason)
            await ctx.send(f"Banned {user.mention} For {reason}")
        except nextcord.Forbidden:
            await ctx.send("Error: I Dont Have Perms To Ban This User.")
        except Exception as e:
            await ctx.send("Error: Invaild Permissions")
            print(f"{e}")


@bot.command(name="ban", aliases=["b", "kan"])
@commands.has_permissions(ban_members=True)
async def bancmd(ctx, user: nextcord.Member, reason):
    if ctx.author.id == 895788406347558922:
        await user.ban(reason=reason)
    else:
        try:
            await user.ban(reason=reason)
            await ctx.send(f"Banned {user.mention} For {reason}")
        except nextcord.Forbidden:
            await ctx.send("Error: I Dont Have Perms To Ban This User.")
        except Exception as e:
            await ctx.send("Error: Invaild Permissions")
            print(f"{e}")

@bot.command(name="membercount", aliases=["mc", "mem"])
async def membercountcmd(ctx):
    emv = nextcord.Embed(
        title="Member Count",
        description=f"{ctx.guild.member_count} Members in {ctx.guild.name}",
        color=nextcord.Color.blue()
    )
    await ctx.send(embed=emv)

@bot.command(name="say", aliases=["talk", "speak", "sa"])
async def sayyy(ctx, *,say):
    x = say
    msg = "Sorry, That Has Blacklisted Words In It."
    if "discord.gg" in x:
        await ctx.send("Sorry, That Has Blacklisted Words In It, Words: [discord.gg]")
        return
    if "https://" in x:
        await ctx.send(msg+" Words: [https://]")
        return
    if ".gg" in x:
        await ctx.send(msg+" Words: [.gg]")
        return
    if "nigger" in x:
        await ctx.send(msg+" Words: [the n-word]")
        return
    else:
        emb = nextcord.Embed(
            title=f"{ctx.author.name} Said",
            description=say,
            color=nextcord.Color.dark_purple()
        )
        await ctx.send(embed=emb)

@bot.command(name="prefix")
@commands.has_permissions(administrator=True)
async def change_prefix(ctx, new_prefix: str):
    # Check if the new prefix is not empty
    if new_prefix:
        bot.command_prefix = new_prefix
        await ctx.send(f"Command prefix changed to `{new_prefix}`.")
    else:
        await ctx.send("Please provide a new prefix.")


bot.remove_command("help")
@bot.command(name="help", aliases=["hlp"])
async def heeeeeeelp(ctx):
        embed = nextcord.Embed(
            title="Bot Commands",
            description=" ",
            color=nextcord.Color.green()
        )
        embed.add_field(name="!prefix", value="Change the bot's command prefix.", inline=False)
        embed.add_field(name="!info", value="Displays bot information.", inline=False)
        embed.add_field(name="!kick", value="Kicks a member from the server.", inline=False)
        embed.add_field(name="!ban", value="Bans a member from the server.", inline=False)
        embed.add_field(name="!membercount", value="Displays the member count of the server.", inline=False)
        embed.add_field(name="!pfp", value="Displays the profile picture of a user.", inline=False)
        embed.add_field(name="!roast", value="roasts some mf", inline=False)
        embed.add_field(name="!say", value="Makes the bot say something.", inline=False)
        embed.add_field(name="!sinfo", value="Displays server information.", inline=False)
        await ctx.send(embed=embed)


@bot.command(name="info", aliases=["about", "aboutbot", "bot", "botinfo"])
async def botinfo(ctx):
    emb =nextcord.Embed(
        title="Bot Info",
        description=" ",
        color=nextcord.Color.dark_green()
    )
    a = bot.get_user(1174590228476993576)
    emb.set_thumbnail(url=a.avatar.url)
    emb.add_field(name="Support Server:", value="[Support Server Invite](https://discord.gg/BcqtWPhWXa)")
    emb.add_field(name="About:", value="Made By .wuid For Idenaty.")
    emb.set_footer(text="© .wuid / WuidBotHosting | 2023")
    await ctx.send(embed=emb)

@bot.command(name="pfp", aliases=["avatar", "icon"])
async def avatarcmd(ctx, user: nextcord.Member):
    emb = nextcord.Embed(
        title=" ",
        description=" ",
        color=nextcord.Color.teal()
    )
    emb.set_image(url=user.avatar.url)
    await ctx.send(embed=emb)

Token = "Add Yours Here"


bot.run(Token)