import discord
import random
import time
import os
from discord.ext import commands, tasks


class DetectMembers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        global currentMembers
        global soundClips

        soundClips = []

        for filename in os.listdir('C:/SoundClips'):
            if filename.endswith('.mp3'):
                soundClips.append(filename)

        currentMembers = len(self.client.get_channel(533319670552330244).members)

        print('Detect Members Ready.')

        self.detect_members.start()

    @tasks.loop()
    async def detect_members(self):

        global currentMembers
        global soundClips

        newChannelMembers = self.client.get_channel(533319670552330244).members
        
        if len(newChannelMembers) != currentMembers and len(newChannelMembers) >= currentMembers:
            currentChannel = await self.client.get_channel(533319670552330244).connect()
            currentChannel.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/bin/ffmpeg.exe', source=f'C:/SoundClips/{random.choice(soundClips)}'))#{random.choice(soundClips)}
            while currentChannel.is_playing():
                time.sleep(.1)
            else:
                await currentChannel.disconnect()
            
        newChannelMembers = self.client.get_channel(533319670552330244).members
    
        currentMembers = len(newChannelMembers)


def setup(client): 
    client.add_cog(DetectMembers(client))