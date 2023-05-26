from discord.ext import commands
import discord


class Talks(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='oi', help="Manda um oi")
    async def send_hi(self, ctx):
        name = ctx.author.name
        response = 'Salve, ' + name
        print(response)
        await ctx.channel.send(response)

    @commands.command(name="segredo", help="Manda um segro no pv")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Comi o cu de curioso")
        except discord.errors.forbidden:
            await ctx.send("Não posso te contar o segredo, habilite a opção para receber mensagem no privado.")


async def setup(bot):
    await bot.add_cog(Talks(bot))