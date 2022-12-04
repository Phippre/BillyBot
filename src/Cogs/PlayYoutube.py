import discord
from discord.ext import commands
from youtube_dl.YoutubeDL import YoutubeDL

class PlayYoutube(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Youtube Cog ready.')

    @commands.command()
    async def play(self, ctx, *, url):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}
        voice = await self.client.get_channel(CHANNEL ID).connect()
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            I_URL = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
            voice.play(source)
            voice.is_playing()

async def setup(client): 
    await client.add_cog(PlayYoutube(client))






######################################
                # Previous Play Code #
#song_there = os.path.isfile('./src/Cogs/song.mp3')
#        
#        if song_there:
#            os.remove('./src/Cogs/song.mp3')
#
#        vc = await self.client.get_channel(533319670552330244).connect()
#
#        ydl_opts = {
#            'format': 'bestaudio/best',
#            'postprocessors': [{
#                'key': 'FFmpegExtractAudio',
#                'preferredcodec': 'mp3',
#                'preferredquality': '192',
#            }],
#        }
#
#        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#            ydl.download([url])
#
#        for file in os.listdir('./'):
#            if file.endswith('.mp3'):
#                os.rename(file, './src/Cogs/song.mp3')
#                print('File succesfully downloaded, renamed and moved folders. Attempting to play.')
#        vc.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/bin/ffmpeg.exe', source='./src/Cogs/song.mp3'))
