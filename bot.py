import discord
from discord.ext import commands

TOKEN = 'YOUR BOT TOKEN'
PREFIX = ['BOT PREFIX']

client = commands.Bot(command_prefix = PREFIX)
client.remove_command("help")

cogs = ['cogs.fun', 'cogs.mod', 'cogs.misc'] # 'cogs' signifies the name of the folder, 'x' signifies the file name.

activity_status = "YOUR BOT ACTIVITY"

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(TOKEN)
