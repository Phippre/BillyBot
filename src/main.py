import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='.', intents = intents)
client.remove_command('help')

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension): 
    await client.load_extension(f'Cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension): 
    await client.unload_extension(f'Cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension): 
    await client.unload_extension(f'Cogs.{extension}')
    await client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'{extension} reloaded')

async def load_extensions():
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'Cogs.{filename[:-3]}') 

async def main():
    async with client:
        await load_extensions()
        await client.start('TOKEN')

asyncio.run(main())
