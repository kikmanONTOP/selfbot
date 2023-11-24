# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
# discord.py 1.7.3
import discord
from discord.ext import commands
prefix = input("prefix: ")
token = 'your token'
command_prefix = prefix
intents = discord.Intents.all()
client = commands.Bot(
    command_prefix,
    case_insensitive=True,
    intents=intents,
    self_bot=True
)


@client.event
async def on_ready():
    print('Logged as', client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        await client.process_commands(message)

@client.event
async def ping(ctx):
    await ctx.send('pong!')


client.run(token, bot=False)