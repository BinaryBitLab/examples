import nextcord
from nextcord.ext import commands
import json
import json
import io
import aiohttp
http_session = aiohttp.ClientSession()

try:
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)
except FileNotFoundError:
    user_data = {}
intents = nextcord.Intents(messages=True, guilds=True, members=True)

bot = commands.Bot(command_prefix='!', intents=intents)

import time
user_message_counts = {}







@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from bots

    author_id = str(message.author.id)
    current_time = time.time()

    # Check if the user has sent messages recently
    if author_id in user_message_counts:
        last_message_time, message_count = user_message_counts[author_id]

        # Check if the user has sent 4 or more messages in less than 5 seconds
        if current_time - last_message_time < 5 and message_count >= 4:
            # Handle spam (e.g., warn or mute the user)
            # Replace this with your preferred spam handling logic
            print('no')
        # Update the user's message count and timestamp
        user_message_counts[author_id] = (current_time, message_count + 1)
    else:
        # Initialize the user's message count and timestamp
        user_message_counts[author_id] = (current_time, 1)
    # Add XP to the user for each message sent (adjust as needed)
    if author_id not in user_data:
        user_data[author_id] = {'xp': 0, 'level': 0}
    user_data[author_id]['xp'] += 6

    # Calculate the amount of XP needed for the next level
    next_level_xp = (user_data[author_id]['level'] + 1) * 120

    # Check if the user has leveled up
    if user_data[author_id]['xp'] >= next_level_xp:
        user_data[author_id]['level'] += 1

        # Increase XP requirement every 2 levels
        if user_data[author_id]['level'] % 2 == 0:
            next_level_xp += 5

        # Create an embed for the level up message
        embed = nextcord.Embed(
            title=f'{message.author.display_name} has leveled up!',
            description=f'Congratulations, {message.author.mention}! You are now level {user_data[author_id]["level"]}!',  # You can adjust the color as needed
        )
        await message.channel.send(embed=embed)

    # Save user data to the file
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

    await bot.process_commands(message)



@bot.slash_command(name='leaderboard', description="Check The BEST!")
async def leaderboard(ctx):
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['xp'], reverse=True)
    max_entries = min(10, len(sorted_users))  # Limit to 10 entries or less if there are fewer users
    
    embed = nextcord.Embed(title='Leaderboard')
    
    for index, (user_id, data) in enumerate(sorted_users[:max_entries], start=1):
        user = ctx.guild.get_member(int(user_id))
        if user and not user.bot:
            display_name = data.get('display_name', user.display_name)  # Use display_name
            embed.add_field(
                name=f'{index}. {display_name}',
                value=f'Level: {data["level"]} | XP: {data["xp"]}',
                inline=False
            )
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("Ready.")
    print(f'{bot.user.name} ID | {bot.user.id}')

@bot.slash_command(name="hello", description="Test Command")
async def testh(ctx):
    await ctx.send("Hello! Im Blu-Bot. My Commands are /ban, /kick, and /giverole!")

# Moderation Commands

@bot.slash_command(name="giverole", description="Add A Role To the Mentioned User.")
@commands.has_permissions(administrator=True)
async def giverole(ctx, user: nextcord.Member, role: nextcord.Role):
    try:
        idr = role.id
        main = ctx.guild.get_role(idr)
        await user.add_roles(main)
        await ctx.send(f"Role {main.name} added to {user.mention}.")
    except nextcord.Forbidden:
        # Invaild Perms | Bot Side
        await ctx.send("Error: Permission Needed | I Dont Have Perms To Add Roles.")
    except nextcord.HTTPException:
        # This exception is raised when an error occurs during an HTTP request (e.g., role not found).
        await ctx.send("Error: HTTP Request Fail. | Try again.")
    except Exception as e:
        # Handle other exceptions here.
        await ctx.send(f"Error: Invaild Permissions.")



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

try:
    with open('sstats.json', 'r') as file:
        moderator_data = json.load(file)
except FileNotFoundError:
    moderator_data = {}

@bot.slash_command(name="ban", description="Ban A Member | reason, member")
@commands.has_permissions(ban_members=True)
async def banuser(ctx, user: nextcord.Member, reason: str):
    
    try:
        if moderator_name in moderator_data:
            moderator_data[moderator_name] += 1
        else:
            moderator_data[moderator_name] = 1

        # Save the updated data
        with open('moderator_data.json', 'w') as file:
            json.dump(moderator_data, file)
        await user.ban(reason=reason)
        await ctx.send(f"Banned {user.mention} For {reason}")
    except nextcord.Forbidden:
        await ctx.send("Error: Permission Needed | Ban Members")
    except Exception as e:
        await ctx.send("Error: Invaild Permissions")
        print(e)

import requests

Token = "ur token here"

bot.run(Token)
