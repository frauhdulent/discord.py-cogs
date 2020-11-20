import discord
from discord.ext import commands

# You can change 'Moderation' to anything.
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Ban command:
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    # Ban error:
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            # You can customize what is said by the bot in the f strings:
            await ctx.send(f'{(ctx.message.author.mention)} User is not defined.')
    
    # Unban command:
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        user = await client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f'{user} has been unbanned.')
    
    # Unban error:
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'{(ctx.message.author.mention)} Sorry. I can only unban users by their IDs.')
        if isinstance(error, commands.CommandInvokeError):
            # You can customize what is said by the bot in the f strings:
            await ctx.send(f"{(ctx.message.author.mention)} This user wasn't banned to begin with.")

def setup(client):
    client.add_cog(Moderation(client)) # Remember based on which name you assigned your class for,
                        # It should be used at the end of the setup function right.
                        # eg:- client.add_cog(x(client)), client.add_cog(y(client)), client.add_cog(z(client))
