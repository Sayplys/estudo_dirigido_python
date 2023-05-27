from discord.ext import commands
import requests
from discord import app_commands
import discord

class Binance(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="moeda", description="Mostra cotações de acordo com os dados da binance")
    async def binance(self, interaction: discord.Interaction, coin: str, base: str):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")

            if price:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é {price}")
            else:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é invalido")
        except Exception as error:
            await interaction.response.send_message("Deu errado sua requisição")
            print(error)       

async def setup(bot):
    await bot.add_cog(Binance(bot),  guilds=[discord.Object(id=1110550192534589543)])