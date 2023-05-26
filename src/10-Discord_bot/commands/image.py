from discord.ext import commands
import discord


class Image(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="foto", help="Manda uma foto aleatória (!foto largura altura)")
    async def get_random_image(self, ctx, largura, altura):
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

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Image(bot))