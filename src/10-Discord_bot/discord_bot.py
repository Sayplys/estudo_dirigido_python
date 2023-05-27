""" bot discord teste """

from discord.ext import commands
from decouple import config
import discord, os
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
    
@bot.event
async def on_ready():
    print(f"Estou conectado como {bot.user}")
    await load_cogs(bot)
    await bot.get_cog('Dates').current_time.start()

async def load_cogs(bot): 
    await bot.load_extension('manager')
    await bot.load_extension('tasks.dates')

    for file in os.listdir("src/10-Discord_bot/alunos"):
        if file.endswith(".py"):
            await bot.load_extension(f'alunos.{file[:-3]}')

    for file in os.listdir("src/10-Discord_bot/commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")


TOKEN = config("TOKEN")
bot.run(TOKEN)

