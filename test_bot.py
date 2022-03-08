import asyncio
import functools
import itertools
import math
from os import name
import random
from discord import Intents
import discord
from discord import FFmpegPCMAudio
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
import datetime
import requests
from discord.utils import find
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import aiohttp
from discord import Intents
from discord import Streaming
from discord import Game
from discord.utils import get
from urllib.parse import quote_plus
import asyncio
from discord import Spotify 
from typing import List
from discord.ext.commands import has_permissions, MissingPermissions
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents =Intents.all())

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("Thanks for adding Shin music to your server typle `!help` to get a list of the commands. Shin music is still in a development state so expect more fetures in the future ")

@bot.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

class Server(commands.Cog):
    def __init__(self, bot ):
        self.bot = bot
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def rules(self ,ctx,*, rules = "unspecified rules"):
        """ Custom rules for the server """
        embed=discord.Embed(title=f"Server rules  {ctx.guild.name}", description=f"```{rules}\n \n ```")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def servers(self ,ctx):
     await ctx.send(f"I'm in {len(bot.guilds)} servers!")
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def stats(self,ctx):
     embed=discord.Embed(title=f"Server stats for : {ctx.guild.name}")
     embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
     embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
    
     await ctx.send(embed=embed) 
        



# This is our actual board View


class Fun(commands.Cog):
    def __init__(self, bot, ):
        self.bot = bot
    @commands.command() 
    async def spotify(self,ctx, user: discord.Member = None):
     """Sends a users Spotify activity"""
     print('debug 0')
     if user == None:
        user = ctx.author
        pass
     print(user.activities) 
     if user.activities:
        print('debug 1')
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title = f"{user.name}'s Spotify",
                    description = "Listening to {}".format(activity.title),
                    color = 0xC902FF)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=embed)
     else:
        print('something went wrong')
        await ctx.send("something went wrong")

    @commands.command() 
    async def meme(self,ctx):
     """Send a random meme via the subreddit r/dankmemes"""  
     embed = discord.Embed(title="Random Memes", description="")

     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
    
        

 


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command() 
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx, member:discord.Member, *, reason = "unspecified reason"):
     """Bans  a specified member with an optional reason"""
     if member.id == ctx.author.id:
        await ctx.send("You cannot ban yourself, sorry")
     else: 
        await member.ban(reason = reason)
        reasonEmbed = discord.Embed(description = f'Succesfully banned {member.mention} for {reason}\n \n ',colour = 0xFF0000)
        reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar))
        reasonEmbed.set_footer(text=f"Banned by {ctx.author.name}")
        await ctx.send(embed=reasonEmbed) 
    @commands.command() 
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, why=None):
     await member.kick(reason=why)
     await ctx.channel.send(f"**{member} has been kicked from this server by {ctx.author}**")
    @ban.error
    async def ban_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions): 
         embed=discord.Embed(title="Invalid command usage, try using it like:",color=0xfe0606)
         embed.add_field(name="Looks like you dont have `permissions` to ban a user",value="```Turn on ban_members permission```")
         await ctx.send(embed=embed)   
        elif isinstance(error, commands.MissingRequiredArgument):
         embed=discord.Embed(title="Invalid command usage, try using it like:",color=0xfe0606)
         embed.add_field(name="!ban `[member]` with `(optional reason)`",value="Arguments: member: User mention ")
         await ctx.send(embed=embed) 
         
         



@commands.command() 
async def rank(ctx, member: discord.Member):
     author = ctx.author # we get the member object
     color = author.color
     if member:
        info_user = member
     elif member == None:
        info_user = ctx.author
     info_embed = discord.Embed(color=color)
     info_embed.set_thumbnail(url=f"{info_user.avatar}")
     
     
  
    


     
     info_embed.add_field(name="Highest Role:", value=member.top_role , inline=False)
    
     await ctx.send(embed=info_embed)

queue = []   
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, play=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream or play))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

def check_queue(ctx,id):
  if queues[id] !=[]:
    voice = ctx.guild.voice_client
    source = queues[id].pop(0)
    voice.play(source, after=lambda x=0: check_queue(ctx, ctx.message.guild.id)) 
queues = {}
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def play(ctx,*, url):
     if (ctx.author.voice):
       channel = ctx.message.author.voice.channel
       voice = get(bot.voice_clients, guild=ctx.guild)
       if voice and voice.is_connected():
        await voice.move_to(channel)
       else:
        voice = await channel.connect()
     else:
      await ctx.send('You are not in a voice channel')      
     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True','default_search': 'auto'}
     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
     voice = get(bot.voice_clients, guild=ctx.guild)
     with YoutubeDL(YDL_OPTIONS) as ydl:
       info = ydl.extract_info(url, download=False)
     URL = info['url']
     source = (FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
     if voice.is_playing():
      guild_id = ctx.message.guild.id
      if guild_id in queues:
        queues[guild_id].append(source)
      else:
          queues[guild_id]=[source]
      await ctx.send('Song added to queue')
     else:
        ctx.voice_client.stop()
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda x=0: check_queue(ctx, ctx.message.guild.id))
        voice.is_playing()
        embed = discord.Embed(title= "Playing:"+   info.get('title'), color = discord.Color.lighter_grey())
        embed.add_field(name="Requested by:", value=f"{ctx.author}")
        await ctx.send(embed=embed)
       
    
class MusicUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")  
    @commands.command()
    async def join(self, ctx):

     if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel!")
        return
     else:
        channel = ctx.message.author.voice.channel
        self.queue = {}
        await ctx.send(f'Connected to ``{channel}``')

     await channel.connect()
    @commands.command()
    async def pause(self,ctx):
     voice = get(bot.voice_clients, guild=ctx.guild)
     connected = ctx.author.voice
     if connected and voice.is_playing() :
      voice.is_playing()
      voice.pause()
     await ctx.send('Music paused')
    @commands.command()
    async def resume(self,ctx):
        voice = get(bot.voice_clients, guild=ctx.guild)
        connected = ctx.author.voice
        if connected and voice.is_playing() :
         voice.resume()
        await ctx.send('Resuming ') 
         




class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)




client = MyClient(intents=intents)

    

async def on_member_update(self, before, after):
        activity_type = None
        streaming_role = after.guild.get_role(521744891748024330)
        try:
            activity_type = after.activity.type
        except:
            pass

        if not (activity_type is discord.ActivityType.streaming):
            # User is doing something other than streaming
            if streaming_role in after.roles:
                print(f"{after.display_name} has stopped streaming")
                await after.remove_roles(streaming_role)
        else:
            if streaming_role not in after.roles:
                # If they don't have the role, give it to them
                # If they have it, we already know they're streaming so we don't need to do anything
                print(f"{after.display_name} has started streaming")
                await after.add_roles(streaming_role)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')









bot.add_cog(MusicUtils(bot))
bot.add_cog(Music(bot))
bot.add_cog(Fun(bot))
bot.add_cog(Moderation(bot))
bot.add_cog(Server(bot))
bot.run("ODA1MzkzNTIzNjk1NDE5NDEz.YBaPKw.U5fLi3wvVH8OT1o2uxweIFetmg8")