import discord
from discord.ext import commands

class hello(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    #command
    @commands.command() #first command, /hello 
    async def hello(self, ctx):
        await ctx.send("Hello, I am Sean's bot") 
    
    
    
def setup(client):
    client.add_cog(hello(client))
    
