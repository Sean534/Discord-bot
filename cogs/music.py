import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


class music(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.queues = {}
    
    def check_queue(self, ctx, id):
        if self.queues[id] != []:
            voice = ctx.guild.voice_client
            source = self.queues[id].pop(0)
            player = voice.play(source) 
    
    @commands.command(pass_context = True) #This lets the bot join vc
    async def joinvc(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio("./audio/" + 'clown.mp3')
            player = voice.play(source)
        
        else:
            await ctx.send("You are not in a voice channel, must be in a voice channel to run this command!")
            
    @commands.command(pass_context = True) #This lets the bot leave vc
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")
    
    @commands.command(pass_context = True) #Pause audio
    async def pause(self, ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("There is no audio playing in the voice channel!")

    @commands.command(pass_context = True) #Resume audio
    async def resume(self, ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("No song is paused currently!")

    @commands.command(pass_context = True) #Stops the audio and clears it
    async def stop(self, ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        voice.stop()
    
    @commands.command(pass_context = True) #Plays the audio
    async def play(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = arg + '.mp3'
        source = FFmpegPCMAudio("./audio/" + song)
        player = voice.play(source, after = lambda x = None: self.check_queue(ctx, ctx.message.guild.id))

    @commands.command(pass_context = True) #Queue the audio
    async def queue(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = arg + '.mp3'
        source = FFmpegPCMAudio("./audio/" + song)
    
        guild_id = ctx.message.guild.id
    
        if guild_id in self.queues:
            self.queues[guild_id].append(source)
    
        else: 
            self.queues[guild_id] = [source]
    
        await ctx.send("Added to queue")
        
def setup(client):
    client.add_cog(music(client))
