import discord
from discord.ext import commands
import os
import discord
from discord.ext import commands
import sqlite3
import json
from discord.gateway import DiscordWebSocket



intents = discord.Intents.all()


bot = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True)
bot.remove_command("help")

#@bot.event
#async def on_ready():
    #print("Bot is ready")



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    print("Bot is ready")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    emoji = bot.get_emoji(id=840089389718962176)
    embed=discord.Embed(description=f"{emoji} Successfully loaded the {extension} cog", color=discord.Color.green())
    await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    emoji = bot.get_emoji(id=840089389718962176)
    embed=discord.Embed(description=f"{emoji} Successfully unloaded the {extension} cog", color=discord.Color.green())
    await ctx.send(embed=embed)




@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    emoji = bot.get_emoji(id=840089389718962176)
    embed=discord.Embed(description=f"{emoji} Successfully reloaded the {extension} cog", color=discord.Color.green())
    await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")





















bot.run('INSERT YOUR TOKEN')


