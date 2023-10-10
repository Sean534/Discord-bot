#import required dependicies
import discord
from discord.ext import commands
import os

#import the apikey
from apikey import BOTTOKEN

# initializing the bot
client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())


@client.event #executes the the command / getting the bot ready
async def on_ready(): 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = 'Clowing on Alex 🤡'))
    print("The bot is ready")
    print("---------------")
    
    #client.remove_command('help')
    #await client.add_cog(help_cog(client))


initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3]) #Will get rid the .py of the cogs

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

        

client.run(BOTTOKEN) 
