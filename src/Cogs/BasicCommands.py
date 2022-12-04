import discord
import random
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import feedparser


class BasicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.rss_entries = []
        self.rss_links = []
        

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('With Cocaine'))
        await self.tech_rss.start()
        print('Billy is ready for you daddy.')

    @tasks.loop(minutes=60)
    async def tech_rss(self):
        print("Getting Tech Feeds")
        
        channel = self.client.get_channel(CHANNEL_ID)
        
        try:
            NewsFeed = feedparser.parse("NONE")
            
            entry = NewsFeed.entries[0]
            entry_title = entry.title
            entry_link = entry.link
            if entry_title not in self.rss_entries:
                self.rss_entries.append(entry_title)
                self.rss_links.append(entry_link)
                embed = discord.Embed(title=entry_title, description=entry_link)
                if entry.__contains__('media_thumbnail'):
                    #print(entry.media_thumbnail[0]['url'])
                    embed.set_thumbnail(url=entry.media_thumbnail[0]['url'])
                await channel.send(embed=embed)
        except:
            print("Unable to get RSS Feed")
        

    @commands.command()
    async def help(self, ctx):
        try:
            embed = discord.Embed(title="Help Dad?", description="Heres what I can do for you :wink:")
            embed.set_thumbnail(url='NONE')
            embed.add_field(name='.help', value='Sends this message', inline=False)
            embed.add_field(name='.clear', value='\nClears your dirty messages :wink: Default is 5', inline=False)
            embed.add_field(name='.youretrash', value='\nDisplay server statistics', inline=False)
            embed.add_field(name='.beatbilly', value='\nPlease dont hurt me again', inline=False)
            embed.add_field(name='.join', value='\nI join voice chat :flushed:', inline=False)
            embed.add_field(name='.leave', value='\nI leave you just like everyone else in your life. :weary:', inline=False)
            embed.add_field(name='.whatdoyouthink', value='Tells you my opinion on your bullshit', inline=False)
            embed.add_field(name='.urbanquery', value='Gives you a random word from Urban Dictionary', inline=False)
            await ctx.send(embed=embed)
        except:
            print("Help Command Failed")


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
    async def join(self, ctx):
        print('joining')
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def urbanquery(self, ctx):
        page_url = "https://www.urbandictionary.com/random.php"

        url_client = req(page_url)

        page_soup = soup(url_client.read(), "html.parser")
        url_client.close()

        titles = page_soup.findAll("a", {"data-x-bind": "definition"})
        definitions = page_soup.findAll("div", {"class": "break-words meaning mb-4"})
        example = page_soup.findAll("div", {"class": "break-words example italic mb-4"})
    
        responses = []

        for i in range(len(titles)):
            responses.append(titles[i].text + ":\n" + definitions[i].text + "\n" + "Example: " + example[i].text + "\n")
        
        embed = discord.Embed(title=titles[0].text, description=definitions[0].text)
        embed.set_thumbnail(url='GIF')
        
        await ctx.send(embed=embed)
    

async def setup(client): 
    await client.add_cog(BasicCommands(client))
