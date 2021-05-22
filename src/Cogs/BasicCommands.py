import discord
import random
import time
import os
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


class BasicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('With Cocaine'))
        print('Billy is ready for you daddy.')

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help Dad?", description="Heres what I can do for you :wink:", inline=True)
        embed.add_field(name='.help', value='Sends this message', inline=True)
        embed.add_field(name='.clear', value='\nClears your dirty messages :wink: Default is 5', inline=True)
        embed.add_field(name='.youretrash', value='\nDisplay server statistics', inline=True)
        embed.add_field(name='.beatbilly', value='\nPlease dont hurt me again', inline=True)
        embed.add_field(name='.join', value='\nI join voice chat :flushed:', inline=True)
        embed.add_field(name='.leave', value='\nI leave you just like everyone else in your life. :weary:', inline=True)
        embed.add_field(name='.whatdoyouthink', value='Tells you my opinion on your bullshit', inline=True)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=5):
        if amount <= 20:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'Purged {amount} messages ma Lord')
        else:
            await ctx.send('That too many daddy :(\nIm not that powerful yet.')

    @commands.command()
    async def youretrash(self, ctx):
        await ctx.send(f'Please end my fucking life.\nClient Latency: {round(self.client.latency * 1000)}ms\nCurrent Member Count: {ctx.guild.member_count}')

    @commands.command(aliases=['beathim'])
    async def beatbilly(self, ctx):
        responses = ['Please not again :(', 'Dont send me back to the hospital :(', 'FUCK!', 'It wasnt me!', 'I swear ill be a better bot.', 'DISCORD HELP ME.', 'End my suffering.', 'I just want to die.', 'I didnt do anything wrong though!', 'Please let me see my family :(']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def whatdoyouthink(self, ctx):
        await ctx.send('Fucking dope dude.')

    @commands.command()
    async def play(self, ctx):
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='C:/hahh.mp3'))
        while vc.is_playing():
            time.sleep(.1)
        else:
            await vc.disconnect()

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    

def setup(client): 
    client.add_cog(BasicCommands(client))
