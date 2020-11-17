import discord
from discord.ext import commands

TOKEN = 'YOUR BOT TOKEN' # Variable for storing your token.
PREFIX = ['BOT PREFIX'] # Variable for storing the bots prefix. eg:- !, ?, +, -

client = commands.Bot(command_prefix = PREFIX) # Using the value stored in variable 'PREFIX'
client.remove_command("help") # This could be useful if you're planning on making a custom help command down the line.

cogs = ['cogs.x', 'cogs.y', 'cogs.z'] # 'cogs' signifies the name of the folder, 'x' signifies the file name.

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(TOKEN) # Using the value stored in variable 'TOKEN'