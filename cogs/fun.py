import discord
from discord.ext import commands

# You can change 'y' to anything.
class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails", "The coin fell down, Try again."]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

def setup(client):
    client.add_cog(Fun(client)) # Remember based on which name you assigned your class for,
                        # It should be used at the end of the setup function right.
                        # eg:- client.add_cog(x(client)), client.add_cog(y(client)), client.add_cog(z(client))
