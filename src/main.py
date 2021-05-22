import discord
import os
from discord.ext import commands

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