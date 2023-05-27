from discord.ext import commands
import discord
from discord import app_commands


class Image(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="foto", description="Manda uma foto aleatória")
    async def get_random_image(self, interaction: discord.Interaction, largura: int, altura: int):
        url_image = f"https://loremflickr.com/{largura}/{altura}"

        embed = discord.Embed(
            title="Resultado da busca da imagem",
            description = "PS: A busca é totalmente aleatória",
            color = 0x0000FF
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)

        embed.add_field(name="API", value=f"Usamos a API do {url_image}")
        embed.add_field(name="Parâmetros", value=f"{largura}/{altura}")

        embed.add_field(name="Exemplo", value=url_image, inline=False)

        embed.set_image(url=url_image)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Image(bot),  guilds=[discord.Object(id=1110550192534589543)])