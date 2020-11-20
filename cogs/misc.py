import discord
from discord.ext import commands

# You can change 'Misc' to anything.
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f'**Pong! ``{round(client.latency * 1000)}ms``**')

def setup(client):
    client.add_cog(Misc(client)) # Remember based on which name you assigned your class for,
                        # It should be used at the end of the setup function right.
                        # eg:- client.add_cog(x(client)), client.add_cog(y(client)), client.add_cog(z(client))
