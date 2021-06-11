import discord
from discord.ext import commands
import asyncio
import sqlite3
import datetime
import discord
from discord.ext import commands
import sqlite3
import json
import math

import aiosqlite

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000, 0)
        msg = await ctx.send(f":ping_pong: Pong!")
        await asyncio.sleep(0.1)
        await msg.edit(content=f":ping_pong: Pong! `{latency}ms`")


    @commands.command()
    async def help(self, ctx, command=None):
        if command is None:
            embed=discord.Embed(title="Help | Commands", description=f"Use `.help [command name]` to get more information on a specific command. \n **Command Prefix:**: `.`", color=discord.Color.random(), inline=False) 
            #embed.add_field(name="**Command Prefix**", value="`.`", inline=True)
            embed.add_field(name="**__Moderation__**", value=f"`announce` | `addrole` | `ban` | `dm` | `kick` | `lock` | `lockdown` | `lockdownend` | `mute` | `nick` | `purge` | `roles` | `removerole` | `slowmode` | `tempmute` | `unban` | `unlock` | `unmute` | `warn` | `warnings` | `whois`", inline=False)
            embed.add_field(name="**__Self Roles__**", value=f"`.android` | `.asia` | `.emulator` | `.europe` | `.ios` | `.NA` | `.SA`", inline=False)
            embed.add_field(name="**__Fun__**", value=f"`av` |  `beg` | `buy` | `cat` | `coins` | `dadjoke` | `daily` | `dice` | `dog` | `eightball` `give` | `poll` | `rank` | `reminder` | `richest` | `rob` | `shop` | `slots` | `top` | `work`", inline=False) 
            embed.add_field(name="**__Other__**", value=f"`activity` | `CRcolor` | `CRmove` | `CRname` | `join` | `pause` `play` | `resume` | `serverinfo`\n \n \n **__Support Website__** | [Click here](https://juicy-celestial-backpack.glitch.me/)", inline=False)
                
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)

        if command == "announce":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Announce** \nDescription - Announce a specified message in a specified channel. \nUsage - `!announce [channel] [message]` \nExample - `!announce #general Hello!`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "give":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Give** \nDescription - Give a specified amount of coins to a mentioned user. \nUsage - `!give [member] [amount]` \nExample - `!give @F904 1000000`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "addrole":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Addrole** \nDescription - Give a specified member a specified role. \nUsage - `!addrole [member] [role]` \nExample - `!addrole @F904#0605 @Master of the Universe`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "ban":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Ban** \nDescription - Ban a member from the guild. \nUsage - `!ban [member] [optional reason]` \nExample - `!ban @F904#0605 Being too cool`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "kick":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Kick** \nDescription - Kick a member from the guild. They will be able to rejoin with a new invite link \nUsage - `!kick [member] [optional reason]` \nExample - `!kick @F904#0605 Being too cool`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "dm":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: DM** \nDescription - Send a given message to a user via Direct Messages. \nUsage - `!dm [member] [message]` \nExample - `!dm @F904#0605 Hey!`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "lock":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lock** \nDescription - Lock the channel you are currently in. \nUsage - `!lock [optional message]` \nExample - `!lock Raid!!!`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "lockdown":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lockdown** \nDescription - Lock the entire server \nUsage - `!lockdown [optional message]` \nExample - `!lockdown We have a raid!!!`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "lockdown":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lockdown End** \nDescription - Unock the entire server \nUsage - `!lockdownend [optional message]` \nExample - `!lockdownend The raid is over, sorry for the inconviences.`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "mute":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Mute** \nDescription - Mute a user from the guild \nUsage - `!mute [member] [optional reason]` \nExample - `!mute @F904#0605 Enough Talking!`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "mute":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Nick** \nDescription - Change a member's nickname \nUsage - `!nick [member] [new nickname]` \nExample - `!nick @F904#0605 Casper`", color=discord.Color.random())
            await ctx.send(embed=embed)
            
        elif command == "purge":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Purge** \nDescription - Clear a specified amount of messages in a channel \nUsage - `!purge [amount]` \nExample - `!purge 50`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "roles":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Roles** \nDescription - View all the roles in the guild. \nUsage - `!roles` \nExample - `!roles`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "removerole":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Remove Role** \nDescription - Take away a specified role from a member. \nUsage - `!removerole [member] [role]` \nExample - `!removerole @F904#0605 @Master of the Universe`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "slowmode":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Slowmode** \nDescription - Change the slowmode of the channel you are in. \nUsage - `!slowmode [seconds]` \nExample - `!slowmode 5`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "tempmute":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Tempmute** \nDescription - Temporarily mute a member for a given time. \nUsage - `!tempmute [member] [time] [optional reason]` \nExample - `!tempmute @F904#0605 1h Please read our #rules`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "unban":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unban** \nDescription - Unban a member from the guild. \nUsage - `!unban [member] [optional reason]` \nExample - `!unban @F904#0605 Sorry for the inconvenience, please join back`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "unlock":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unlock** \nDescription - Unlock the channel you are in. \nUsage - `!unlock [optional reason]` \nExample - `!unlock The raid is over`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "unmute":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unmute** \nDescription - Unmute a member. \nUsage - `!unmute [member] [reason]` \nExample - `!unmute @F904#0605 Mute duration is over`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "warn":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Warn** \nDescription - Warn a member. \nUsage - `!warn [member] [reason]` \nExample - `!warn @F904#0605 Advertising content`", color=discord.Color.random())
            await ctx.send(embed=embed)
            
        elif command == "warnings": 
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Warnings** \nDescription - View a member's warnings. \nUsage - `!warnings [member]` \nExample - `!warnings @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "whois":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Whois** \nDescription - View information about a member. \nUsage - `!whois [member]` \nExample - `!whois @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "av":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Avatar** \nDescription - View a members avatar. \nUsage - `!av [member]` \nExample - `!av @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "beg":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Beg** \nDescription - Beg to earn between 1 to 100 coins. \nUsage - `!beg` \nExample - `!beg`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "buy":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Buy** \nDescription - Buy an item in the shop. \nUsage - `!buy [item name]` \nExample - `!buy Discord Legend`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "coins":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Coins** \nDescription - View your coins. Coins can be earned through several various games. \nUsage - `!coins` \nExample - `!coins`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "dadjoke":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Dadjoke** \nDescription - Recieve a random bad joke. \nUsage - `!dadjoke` \nExample - `!dadjoke`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "daily":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Daily** \nDescription - Claim an amount of coins between 250 to 485 daily. \nUsage - `!daily` \nExample - `!daily`", color=discord.Color.random())
            await ctx.send(embed=embed)
        
        elif command == "dice":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Dice** \nDescription - Roll the dice for coins. Rolling a double will give you twice your bet, rolling a double 6 will give you thrice your bet. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "poll":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Poll** \nDescription - Create a poll. Automatic thumbs up and thumbs down reactions will be placed. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "rank":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Rank** \nDescription - View you rank statistics. XP is earned by simply chatting. \nUsage - `!rank` \nExample - `!rank`", color=discord.Color.random())
            await ctx.send(embed=embed)
        elif command == "reminder":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Reminder** \nDescription - Set a reminder. \nUsage - `!reminder [time] [message]` \nExample - `!reminder 1h Walk my dog`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "richest":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Richest** \nDescription - View the richest users in the server. This is completely based on raw amount of coins a user has. \nUsage - `!richest [index]` \nExample - `!richest 5`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "rob":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Rob** \nDescription - Rob a user. Successfully robbing can get you coins, but getting caught will charge you coins. You need at least 250 coins to be able to rob. \nUsage - `!rob [member]` \nExample - `!rob @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "shop":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Shop** \nDescription - View the shop items. Purchase items with coins. \nUsage - `!shop` \nExample - `!shop`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "slots":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Slots** \nDescription - Play slots with a chance to win up to triple your bet. \nUsage - `!slots [bet]` \nExample - `!slots 1000`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "top":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Top** \nDescription - View the rank leaderboard. \nUsage - `!top` \nExample - `!top`", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif command == "work":
            #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Work** \nDescription - Claim a work paycheck each hour. You can earn between 100 to 280 coins. \nUsage - `!work` \nExample - `!work`", color=discord.Color.random())
            await ctx.send(embed=embed)

        

        elif command == "configuring":
            
            embed = discord.Embed(description=f"Hey there, {ctx.author}! \nPlease enter the following configuring commands: \n- `f!configtickets [message ID] [ticket category ID]` \nThe Message ID provided is the message I will react to, if and when a user presses on that reaction, a new ticket channel will be created under the channel category provided. \n\n- `configlvlups [channel category ID]` \n Under the channel category ID provided, I will create the channel where I will congratulate users once they level up \n\n- `configmsglogs [channel category ID]` \nUnder channel category provided, I will create a new channel, where all message log data will be stored, this means all messages edited or deleted by a user in the guild. \n\n - `configmemberlogs [channel category ID]` \nUnder channel category provided, I will create a new channel, where all member update data will be stored, this includes username changes, nickname changes, discriminator changes, role updates, avatar changes, etc.", color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            emoji = self.bot.get_emoji(id=840585961497952256)
            embed=discord.Embed(description=f"{emoji} Command not found", color=discord.Color.red())



    

        
    



def setup(bot):
    bot.add_cog(Moderation(bot))
        
