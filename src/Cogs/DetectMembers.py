import discord
import asyncio
import random
import time
import os
from discord.ext import commands, tasks

class DetectMembers(commands.Cog):

    channel_ID = CHANNEL-ID

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
    
        global currentMembers
        global soundClips
        soundClips = []
        
        try:
            for filename in os.listdir('./SoundClips'):
                if filename.endswith('.mp3'):
                    soundClips.append(filename)
        except:
            print("Getting sound clips failed")
            
        currentMembers = len(self.client.get_channel(self.channel_ID).members)
        
        print('Detect Members Started.')
        
        await self.detect_members.start()

    @tasks.loop()
    async def detect_members(self):
        global currentMembers
        global soundClips

        newChannelMembers = self.client.get_channel(self.channel_ID).members
        
        if len(newChannelMembers) != currentMembers and len(newChannelMembers) >= currentMembers:
            currentChannel = await self.client.get_channel(self.channel_ID).connect()
            currentChannel.play(discord.FFmpegPCMAudio(source=f'./SoundClips/{random.choice(soundClips)}'))#{random.choice(soundClips)}
            while currentChannel.is_playing():
                await asyncio.sleep(.1)
            else:
                await currentChannel.disconnect()
            
        newChannelMembers = self.client.get_channel(self.channel_ID).members
    
        currentMembers = len(newChannelMembers)


async def setup(client): 
    await client.add_cog(DetectMembers(client))
