import discord
from discord.ext import commands

class Clown(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    target_user_id = 286333613803569153  # THIS IS ALEX's USER

    @commands.Cog.listener()  # Clowning on Alex HEHE
    async def on_message(self, message):
        if str(message.author.id) == str(self.target_user_id):
            await message.channel.send("A clown just typed 🤡")

    @commands.command()  # SEND CLOWN DM
    async def sendclown(self, ctx, target_user: discord.Member):
        if target_user:
            #emoji = "🤡🤡🤡🤡🤡" These 2 codes let me type the message
            #await target_user.send(emoji)
            video_file_path = './audio/gerson_D_clown.mov'  # SEND VIDEO HEHE
            video_file = discord.File(video_file_path)
            await target_user.send(file=video_file)
        else:
            await ctx.send("You need to mention a user to use this command.")

def setup(client):
    client.add_cog(Clown(client))
