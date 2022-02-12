import discord
import asyncio
import random 
import os
from discord import Member
from discord import player
from discord import channel
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from discord.ext import tasks
import datetime as dt
import json
import os 
import datetime
from PIL import Image
from io import BytesIO
from youtube_dl import YoutubeDL
from discord.ext import commands
import aiohttp
from discord import Spotify 
from discord import Intents
import  requests 
from discord.ext import menus     
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents =Intents.all(), help_command=None)
@bot.command()
async def meme(ctx):
    embed = discord.Embed(title="Random Memes", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def mood(ctx):
    responses =["https://youtu.be/UiPirmkLr9g","https://youtu.be/E9baa1IQoC4","https://youtu.be/1MalyCzt258","https://youtu.be/WGUr6xZnkbU","https://youtu.be/N2KlTK2cMFM","https://youtu.be/I815FLT_Hr4",]
    response = random.choice(responses)
    author = ctx.author
    embed=discord.Embed(title="Song of the day ↓", color=0xfe0606)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910265356348710943/934768866683416586/5..jpg")
    embed.add_field(name=response,value=f"Song of the day for {author}")
    await ctx.send(embed=embed)

@bot.command()
async def hm(ctx):
    embed = discord.Embed(title="Hmm", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/hmm/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
     
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Bot commands")
    embed.set_author(name="Spellbound Bot",icon_url="https://cdn.discordapp.com/attachments/910265356348710943/934768866683416586/5..jpg")
    embed.add_field(name="play", value="playes a song via a  youtube url and queues a next song if a song is palying ")
    embed.add_field(name="skip", value="Skips the song")
    embed.add_field(name="pause", value="Pauses the song")
    embed.add_field(name="resume", value="Resumes the song ")
    embed.add_field(name="Ban",value="Bans a user and sends them a messsage")
    embed.add_field(name="Warn", value="Warns a user")
    embed.add_field(name="Metamsk", value="Shows you your inventory/portfolio")
    embed.add_field(name="Shop", value="Displayes the shop ")
    embed.add_field(name="sell", value="Sell an item from inventory")
    embed.add_field(name="buy", value="Buy an item from shop ")
    embed.add_field(name="doom", value="Be a doomer ")
    embed.add_field(name="nft", value="Custom nft ")
    embed.add_field(name="gm", value="Easy way to enter the chat")
    embed.add_field(name="zzz", value="Just iconic ")
    embed.add_field(name="vibe", value="Vibe of the day")
    embed.add_field(name="fractions",value="A way for everyone to join the Metaverse")
    embed.add_field(name="av",value="Displayes the avatar of a user")
    embed.add_field(name="info",value="Displayes information about a user")
    embed.set_footer(text="Thanks your using the bot")
    await ctx.send(embed=embed)




@bot.command()
async def doom(ctx, user:discord.Member = None ):
    if user == None: 
       user = ctx.author
    doomer = Image.open("doomer.jpg")
    
    asset = user.avatar_url_as(size=512) 
    
    data = BytesIO(await asset.read())
    pfp = Image.open(data) 
    pfp = pfp.resize((100,90))
    doomer.paste(pfp, (140,150))
    doomer.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))


@bot.command()
async def nft(ctx, user:discord.Member = None ):
    if user == None: 
       user = ctx.author
    NFT = Image.open("NFT.png")
    
    asset = user.avatar_url_as(size=512) 
    
    data = BytesIO(await asset.read())
    pfp = Image.open(data) 
    pfp = pfp.resize((336,342))
    NFT.paste(pfp, (18,19))
    NFT.save("profile2.png")
    await ctx.send(file = discord.File("profile2.png"))




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Support: https://smarturl.it/Spellbound_YouTube'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    
@bot.command()
@commands.has_any_role('ADMIN', 'Moderator','Discord Management')
async def warn(ctx, member: discord.Member, *, arg):
    logsChannel = bot.get_channel(768939846797361202)
    user = member.mention
    embed = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

    embed2 = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed2.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed2.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

    await logsChannel.send(embed=embed2)
    await member.send(f'You have been warned in {ctx.guild.name} for **{arg}**!')
    message = await ctx.send(embed=embed)

@bot.command()
async def report(ctx, member: discord.Member, *, arg):
    logsChannel = bot.get_channel(769179307649925201)
    user = member.mention
    embed = discord.Embed(title="User report issued: ", color=0xf40000)
    embed.add_field(name="Reporting: ", value=f'Reason: {arg}', inline=False)
    embed.add_field(name="User reported: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="Reported by: ", value=f'{ctx.author}', inline=False)

    embed2 = discord.Embed(title="User report: ", color=0xf40000)
    embed2.add_field(name="Reporting: ", value=f'Reason: {arg}', inline=False)
    embed2.add_field(name="User reported: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="Reported by: ", value=f'{ctx.author}', inline=False)

    await logsChannel.send(embed=embed2)
    message = await ctx.send(embed=embed)


@bot.command()
async def  av(ctx, member: discord.Member=None):
    if member:
        info_user = member
    elif member == None:
        info_user = ctx.author
    embed=discord.Embed(title=f"{info_user}")
    embed.set_image(url= f"{info_user.avatar_url_as(format=None, static_format='webp')}")    
    await ctx.send(embed=embed)
 
 
@bot.command()
@commands.has_any_role('ADMIN', 'Moderator','Discord Management')
async def ban(ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a dump!"
    message = f"If you think your ban was unjustified dm a mod you have been banned from {ctx.guild.name} for  {reason}"
    await member.send(message)
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")
    await member.ban(reason = reason)


@bot.command()
async def vibe( ctx ):
    
    embed=discord.Embed(title="Dope Shit Only")
    embed.set_image(url='https://media.discordapp.net/attachments/910041377075769345/915317482879873024/bepop.gif')
    embed.add_field(name='IKZ ', value='TTP', inline=False)
    await ctx.send(embed=embed)

mainshop = [{"name":"NemeShin ","price":10000000000},{"name":"Defractionalized-NemeShin","price":10,"description":"A fraction of defractionalized NemeShin"},{"name":"Spellbound-fouter","price":250000,"description":"Voodoo doll fouter"},{"name":"Spellbound-mask","price":100,"description":"Ape logo mask"},{"name":"Warhoundz-fouter","price":250000,"description":"Warhoundz logo "}]                      
@bot.command()
async def fractions(ctx):
   await  open_acount(ctx.author)
   user = ctx.author 
   users = await get_bank_data()
   wallet_apm =  users[str(user.id)]["wallet"] 
   
   embed=discord.Embed(title="NemeShin")
   embed.set_image(url="https://yt3.ggpht.com/aT1RcqmOcgVgNd58CmpXFOIKUuPXUvIWIQjW14nGnbnrhHeMC2GkObMkxdJcBiNOKMSnR9AHRA=s900-c-k-c0x00ffffff-no-rj")
   embed.add_field(name="Dope shit only", value= "Defractionized NemeShin is a  way to allow everybody to access the Metaverse "  , inline=False)
   await ctx.send(embed=embed)

@bot.command()
async def Shop(ctx):
    em = discord.Embed(title="Shop")
    for item in mainshop:
        name = item["name"]
        price = item["price"]
        em.set_thumbnail(url="https://yt3.ggpht.com/aT1RcqmOcgVgNd58CmpXFOIKUuPXUvIWIQjW14nGnbnrhHeMC2GkObMkxdJcBiNOKMSnR9AHRA=s900-c-k-c0x00ffffff-no-rj")
        em.add_field(name = name, value =f"eth{price} | ",inline=False) 
    await ctx.send(embed = em)    


@bot.command()
async def buy(ctx,item,amount = 1):
    await open_acount(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")
    return [True,"Worked"]
    
async def update_bank(user,change=0,mode = "wallet"):
    users = await get_bank_data()
    
    users[str(user.id)][mode] += change
    
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    
    bal = [users[str(user.id)][mode]]
    return  bal 
    

@bot.command()
async def Metamask(ctx):
    await open_acount(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "MetaMask Wallet")
    em.set_image(url="https://media.discordapp.net/attachments/910041377075769345/910383027069255751/SLEEPYazki.gif")
    em.add_field(name = "connect your metamask:", value="https://metamask.io")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        wallet_apm =  users[str(user.id)]["wallet"] 
        em.add_field(name = name, value = amount)
        em.add_field(name = wallet_apm , value = "eth")   

    await ctx.send(embed = em)    
   
@bot.command()
@commands.cooldown(1, 120000, commands.BucketType.user)
async def beg(ctx):
    await open_acount(ctx.author)
    user = ctx.author
    users = await get_bank_data()
   
   
    earings = random.randrange(101)
   
    await ctx.send(f"You Were given {earings} eth ")
   
    wallet_apm =  users[str(user.id)]["wallet"] =+ earings
     
    with open("mainbank.json", "w") as f:
        json.dump(users,f)


@beg.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down !",description=f"Try again in {error.retry_after:.2f}s." )
            await ctx.send(embed=em)       

@mood.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="",description="You can use this command  once a day " )
            await ctx.send(embed=em)       



async def open_acount(user):
   
   users = await get_bank_data()
        
   if str(user.id) in users:
        return False
   else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        
   with open("mainbank.json", "w") as f:
        json.dump(users,f)

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
       
    
    return users    

@bot.command()
async def sell(ctx,item,amount = 1):
    await open_acount(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]




@bot.command()
async def eth(ctx):
 embed=discord.Embed()
 embed.set_image(url="http://www.simpleimageresizer.com/_uploads/photos/0a8a0008/unknown_34.png")
 embed.add_field(name="ethereum graph [24h] ", value="±0,30%", inline=False)
 await ctx.send(embed=embed)


@bot.command()
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    connected = ctx.author.voice
    if voice.is_playing()  and connected  :
     
     voice.stop()
     await ctx.send('Skipping...')
    else:
     await ctx.send('Please join a voice channel before using this command')
    
# command to resume voice if it is paused
@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    connected = ctx.author.voice
    if connected and voice.is_playing() :
        voice.resume()
        await ctx.send('Bot is resuming')
    else:
     await ctx.send('Please join a voice channel before using this command')

# command to pause voice if it is playing
@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    connected = ctx.author.voice
    if connected and voice.is_playing() :
     voice.is_playing()
     voice.pause()
     await ctx.send('Bot has been paused')
    else:
     await ctx.send('Please join a voice channel before using this command')

    
 
@bot.command()
async def leave(ctx):
    connected = ctx.author.voice
    if connected:
     await ctx.voice_client.disconnect()
    else:
     await ctx.send('Please join a voice channel before using this command') 

# command to clear channel messages
@bot.command()
@commands.has_role("Moderator")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")


queues = {}
def check_queue(ctx, id):
  if queues[id] !=[]:
    voice = ctx.guild.voice_client
    source = queues[id].pop(0)
    voice.play(source, after=lambda x=0: check_queue(ctx, ctx.message.guild.id))

@bot.command(aliases = ["p"])
async def play(ctx, url):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
      await voice.move_to(channel)
    else:
      voice = await channel.connect()
  else:
    await ctx.send('You are not in a voice channel')      
  YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
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
      await ctx.send('Playing: '+ info.get('title'))


      

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]    
