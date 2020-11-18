import discord
from discord.ext import commands

TOKEN = 'YOUR BOT TOKEN' # Variable for storing your token.
PREFIX = ['BOT PREFIX'] # Variable for storing the bots prefix. eg:- !, ?, +, -

client = commands.Bot(command_prefix = PREFIX) # Using the value stored in variable 'PREFIX'
client.remove_command("help") # This could be useful if you're planning on making a custom help command down the line.

cogs = ['cogs.x', 'cogs.y', 'cogs.z'] # 'cogs' signifies the name of the folder, 'x' signifies the file name.

# You can also change the bot's discord activity, its not necessary but if you want it maybe useful down the line.
# Not that its mandatory but it maybe useful down the line.

activity_status = "YOUR BOT ACTIVITY"

# Types of Activities:

@client.event
async def on_ready():
    # Types of Activities: Playing, Streaming, Listening, Watching.
    
    # > For more info: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot.change_presence
    
    # They're commented out, you can only choose one. You can't have 2 running at a time.
    
    # await client.change_presence(activity=discord.Game(name=activity_status))
    # await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_status))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(TOKEN) # Using the value stored in variable 'TOKEN'
