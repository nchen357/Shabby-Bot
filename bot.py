# bot.py
import os
import sys
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

#intializing some stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

######################### START OF CILENT FUNCTIONS ###############################
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #maybe create a bank of words 
    badSubtext = 'git gud'

    messageSplit = message.content.split()
    #add try catch maybe to prevent git gud from printing in multiple iterations
    if 'bad' in messageSplit:
        response = badSubtext
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
client.run(TOKEN)
###################### START OF BOT COMMANDS ###################################
#this function displays various cat pictures
@bot.command(name='cat')
async def kitty_cat(ctx):
    #increase bank in future
    catBank = [
        'https://cdn.shopify.com/s/files/1/0092/7724/3507/files/IMG_0669_large.GIF?v=1574180591',
        'https://cdn.shopify.com/s/files/1/0092/7724/3507/articles/190828_0026_1200x.jpg?v=1573022194',
    ]
    response = random.choice(catBank)
    await ctx.send(response)


#create birb, penguin, seal and doggo
bot.run(TOKEN)
sys.exit()
