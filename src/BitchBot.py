import discord
import random
import time
import youtube_dl
from discord import channel
from discord import FFmpegPCMAudio
from discord import guild
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import context
from discord.ext.commands.context import Context
from discord.guild import Guild
from discord.member import VoiceState
from discord.utils import escape_markdown
from asyncio.tasks import sleep
from typing import ContextManager

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='.', intents = intents, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('With Cocaine'))
    global currentMembers
    currentMembers = len(client.get_channel(533319670552330244).members)
    print('Billy is ready for you daddy.')
    detect_members.start()

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help Dad?", description="Heres what I can do for you :wink:", inline=True)
    embed.add_field(name='.help', value='Sends this message', inline=True)
    embed.add_field(name='.clear', value='\nClears your dirty messages :wink: Default is 5', inline=True)
    embed.add_field(name='.youretrash', value='\nDisplay server statistics', inline=True)
    embed.add_field(name='.beatbilly', value='\nPlease dont hurt me again', inline=True)
    embed.add_field(name='.join', value='\nI join voice chat :flushed:', inline=True)
    embed.add_field(name='.leave', value='\nI leave you just like everyone else in your life. :weary:', inline=True)
    embed.add_field(name='.whatdoyouthink', value='Tells you my opinion on your bullshit', inline=True)

    await ctx.send(embed=embed)

@client.command()
async def clear(ctx, amount=2):
    if amount <= 5:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged {amount} messages ma Lord')
    else:
        await ctx.send('That too many daddy :(\nIm not that powerful yet.')

@client.command()
async def youretrash(ctx):
    await ctx.send(f'Please end my fucking life.\nClient Latency: {round(client.latency * 1000)}ms\nCurrent Member Count: {ctx.guild.member_count}')

@client.command(aliases=['beathim'])
async def beatbilly(ctx):
    responses = ['Please not again :(', 'Dont send me back to the hospital :(', 'FUCK!', 'It wasnt me!', 'I swear ill be a better bot.', 'DISCORD HELP ME.', 'End my suffering.', 'I just want to die.', 'I didnt do anything wrong though!', 'Please let me see my family :(']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def whatdoyouthink(ctx):
    await ctx.send('Fucking dope dude.')

@client.command()
async def play(ctx):
    vc = await ctx.author.voice.channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='C:/hahh.mp3'))
    while vc.is_playing():
        time.sleep(.1)
    else:
        await vc.disconnect()

@tasks.loop()
async def detect_members():
    global currentMembers
    newChannelMembers = client.get_channel(533319670552330244).members
    
    if len(newChannelMembers) != currentMembers and len(newChannelMembers) >= currentMembers:
        currentChannel = await client.get_channel(533319670552330244).connect()
        currentChannel.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/bin/ffmpeg.exe', source='C:/hahh.mp3'))
        while currentChannel.is_playing():
            time.sleep(.1)
        else:
            await currentChannel.disconnect()
        
    newChannelMembers = client.get_channel(533319670552330244).members
 
    currentMembers = len(newChannelMembers)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    

client.run('TOKEN')
