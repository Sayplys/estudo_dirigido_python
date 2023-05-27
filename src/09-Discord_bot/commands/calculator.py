from discord.ext import commands
import re
from discord import app_commands
import discord

class Calculator(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="calcular", description="Calculadora")
    async def calculate_expression(self,interaction: discord.Interaction, message: str):
        expression = ''.join(message)
        numeros = re.split(r"[+ x / ( ) -]+", expression)           

        try:
            for numero in numeros:
                int(numero)
            response = eval(expression)
        except ValueError:
            await interaction.response.send_message('Por favor, mande uma conta válida.')
            return

        await interaction.response.send_message('A resposta é: ' +  str(response))


async def setup(bot):
    await bot.add_cog(Calculator(bot),  guilds=[discord.Object(id=1110550192534589543)])