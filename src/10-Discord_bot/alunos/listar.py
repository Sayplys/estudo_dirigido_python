""" Listar os alunos cadastrados """

from discord.ext import commands
import discord

class Listar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ls-aluno", help="Lista de alunos (!ls-alunos)")
    async def listar(self, ctx):

        embed = discord.Embed(
            title="Lista de alunos",
            description="Lista de alunos cadastrados, com o comando !cadastrar",
            color=0xff4422
        )

        with open("src/10-Discord_bot/alunos/alunos.txt", "r", encoding="UTF-8") as arquivo:
            for linha in arquivo.readlines():
                dados_da_linha = linha.strip().split(',')
                embed.add_field(
                    name=dados_da_linha[1], 
                    value=f'prontuário: {dados_da_linha[0]}\n email: {dados_da_linha[2]}'
                )

                
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)

        await ctx.send(embed=embed)            


async def setup(bot):
    await bot.add_cog(Listar(bot))