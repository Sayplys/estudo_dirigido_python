""" bot discord teste """

from discord.ext import commands
from decouple import config
import discord, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
    
def load_cogs(bot): 
    bot.load_extension('manager')
    bot.load_extension('tasks.dates')
    for file in os.listdir("src/10-Discord_bot/commands"):
        if file.endswith(".py"):
            bot.load_extension(f"commands.{file[:-3]}")
   
    
load_cogs(bot)   
    

TOKEN = config("TOKEN")
bot.run(TOKEN)

