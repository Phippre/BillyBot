import discord
import random
import time
import youtube_dl
import os
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

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension): 
    client.load_extension(f'Cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension): 
    client.unload_extension(f'Cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension): 
    client.unload_extension(f'Cogs.{extension}')
    client.load_extension(f'Cogs.{extension}')

for filename in os.listdir('C:/Users/parke/Documents/GitHub/BillyBot/src/Cogs'):
    if filename.endswith('.py'): 
        client.load_extension(f'Cogs.{filename[:-3]}') 


client.run('TOKEN')