import discord
from discord.ext import commands
import asyncio
import sqlite3
import datetime
import discord
from discord.ext import commands
import sqlite3
import json

from discord.ext.commands.core import command



embedfilter=discord.Embed(description=f"**Command: Filter** \nDescription - Filter a word, anyone who is not a Server Moderator will be warned for language \nUsage - `!filter [word]` \nExample - `!filter fuck`", color=discord.Color.random())
embedunfilter=discord.Embed(description=f"**Command: Unfilter** \nDescription - Unilter a filtered word \nUsage - `!unfilter [word]` \nExample - `!unfilter fuck`", color=discord.Color.random())


class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        message_content = message.content.strip().lower()
        dbconnect = sqlite3.connect('users (3).db')
        cursor = dbconnect.cursor()
        records = cursor.execute("SELECT word FROM bannedwords").fetchall()
        for row in records:
            if row[0] in message_content:
                if message.author.permissions_in(message.channel).manage_messages:
                    break
                else:
                    await message.delete()
                msg = await message.channel.send(f"{message.author.mention}, watch your language.")
                await asyncio.sleep(3.5)
                await msg.delete()
                #channel = bot.get_channel(848062068887781437)
                channel = discord.utils.get(message.guild.channels, name='automod-logs')
                embedVar = discord.Embed(description=f"Language Warning Issued to {message.author}", color=discord.Color.red(), timestamp=datetime.utcnow())
                embedVar.set_author(name=f"{message.author}#{message.author.discriminator}", icon_url=message.author.avatar_url)
                embedVar.set_footer(text=f"ID: {message.author.id}")
                embedVar.add_field(name="User:", value=f"{message.author.mention}", inline=True)
                embedVar.add_field(name="Channel:", value=f"{message.channel.mention}", inline=True)
                #dt_string = datetime.strftime("%d/%m/%Y %H:%M:%S")
                #embedVar.add_field(name="Time:", value=f"{dt_string}", inline=True)
                embedVar.add_field(name="Message:", value=f"{message.content}", inline=False)
                await channel.send(embed=embedVar)


    @commands.command()
    async def filter(self, ctx, word=None):
        if word is None:
            return await ctx.reply(embed=embedfilter)
        word = word.lower()
        dbconnect = sqlite3.connect('users (3).db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
        result = cursor.fetchone()
        if result:

            emoji = self.bot.get_emoji(id=840585961497952256)
            embed=discord.Embed(description=f"{emoji} That word is already filtered", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            cursor.execute('''INSERT INTO bannedwords(word) VALUES(?)''', (word,))
            emoji = self.bot.get_emoji(id=840089389718962176)
            embed = discord.Embed(description=f"{emoji} `{word}` has been filtered", colour=discord.Color.green())
            await ctx.send(embed=embed)
        
            channel = self.bot.get_channel(848064366145568798)
            embedVar = discord.Embed(title="Word Filtered", description=f"Issued by **{ctx.message.author}**", color=0xe74c3c)
            embedVar.add_field(name="Word:", value=f"**{word}**", inline=True)
            embedVar.add_field(name="Channel:", value=f"**{ctx.channel.mention}**", inline=True)
            #embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=True)
            await channel.send(embed=embedVar)
            dbconnect.commit()
            dbconnect.close()


    @commands.command()
    async def unfilter(self, ctx, word=None):
        if word is None:
            return await ctx.reply(embed=embedfilter)
        word = word.lower()
        dbconnect = sqlite3.connect('users (3).db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM bannedwords WHERE word = ?", (word,))
            emoji = self.bot.get_emoji(id=840089389718962176)
            embed = discord.Embed(description=f"{emoji} `{word}` has been unfiltered", color=discord.Color.green())
            await ctx.send(embed=embed)
            channel = self.bot.get_channel(848064366145568798)
            embedVar = discord.Embed(title="Word Unfiltered", description=f"Issued by **{ctx.message.author}**", color=0xe74c3c)
            embedVar.add_field(name="Word:", value=f"**{word}**", inline=True)
            embedVar.add_field(name="Channel:", value=f"**{ctx.channel.mention}**", inline=True)
            #embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=True)
            await channel.send(embed=embedVar)
        else:
            emoji = self.bot.get_emoji(id=840585961497952256)
            embed=discord.Embed(description=f"{emoji} That word is not filtered", colour=discord.Color.red())
            await ctx.send(embed=embed)
        dbconnect.commit()
        dbconnect.close()


    @commands.command()
    async def filters(self, ctx):
        bannedTerms = "**The filtered words are: **\n"
        dbconnect = sqlite3.connect('users (3).db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords")
        result = cursor.fetchall()
        for row in result:
            bannedTerm = row[0]
            
            bannedTerms = bannedTerms + bannedTerm + "\n"
        embed = discord.Embed(description=f"{bannedTerms}", color=discord.Color.blue())
        embed.set_footer(text=f"Note: If there are no filtered words, the embed will be blank.")
        await ctx.send(embed=embed)
        #await ctx.send(bannedTerms)
        dbconnect.commit()
        dbconnect.close()


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(840105867948195860)
        await member.add_roles(role)
        #channel = member.guild.get_channel(842082286966931458) 
        channel = discord.utils.get(member.guild.channels, name="welcome-logs")
        #await channel.send(f"Hey there, {member.mention}! Welcome to Helpers Lounge <:pepesadlove:840824623431155722> \nPlease go through our <#798547735615635526>, and have a fantastic time here!")
        #memberleavejoincnl = discord.utils.get(member.guild.get_channel, name="member-logs")
        embed = discord.Embed(description=f"{member.mention} has joined the server", timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
        embed.set_author(name="Member joined", icon_url=member.avatar_url)
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)


    
    

    







def setup(bot):
    bot.add_cog(Automod(bot))
