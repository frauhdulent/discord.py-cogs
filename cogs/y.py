import discord
from discord.ext import commands

# You can change 'y' to anything.
class y(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def y1(self, ctx):
        await ctx.send("y")

def setup(client):
    client.add_cog(y(client)) # Remember based on which name you assigned your class for,
                        # It should be used at the end of the setup function right.
                        # eg:- client.add_cog(x(client)), client.add_cog(y(client)), client.add_cog(z(client))