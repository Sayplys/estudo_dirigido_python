from discord.ext import commands
import discord
from discord import app_commands


class Talks(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name='oi', description="Manda um oi")
    async def send_hi(self, interaction: discord.Interaction):
        name = interaction.user.name
        response = 'Salve, ' + name
        await interaction.channel.send(response)

    @app_commands.command(name="segredo", description="Manda um segredo no pv")
    async def secret(self, interaction: discord.Interaction):
        try:
            await interaction.user.send("Comi o cu de curioso")
        except discord.errors.forbidden:
            await interaction.send("Não posso te contar o segredo, habilite a opção para receber mensagem no privado.")


async def setup(bot):
    await bot.add_cog(Talks(bot),  guilds=[discord.Object(id=1110550192534589543)])