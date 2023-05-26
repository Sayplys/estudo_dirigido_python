""" cadastra os alunos """

from discord.ext import commands 

class Cadastro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help= "Cadastra aluno. (!cadastrar prontuario nome email)")
    async def cadastrar(self, ctx, *message):
        await ctx.send('cadastando...')
        dados = ','.join(message)
        with open("src/10-Discord_bot/alunos/alunos.txt", 'r', encoding='UTF-8') as arquivo_r:
            lines = arquivo_r.readlines()
            if len(lines) != 0:
                await self.check_occurrence(ctx, lines, dados)
            else:
                await self.add_to_data_base(ctx, dados)
 
    async def check_occurrence(self, ctx, lines, dados):
        await ctx.send("Checando ocorrência...")
        for index, line in enumerate(lines):
            line_data = line.strip().split(',')
            dados_data = dados.strip().split(',')
            if len(dados_data) == 3:     
                if line_data[0] == dados_data[0] and line_data[2] == dados_data[2]:
                    if line_data[0] == dados_data[0]:
                        await ctx.send("Já existe um aluno cadastrado com esse prontuário. Por favor indique outro.")
                    if line_data[2] == dados_data[2]:
                        await ctx.send("Já existe um aluno cadastrado com esse email. Por favor indique outro.")
                    break
                elif index == len(lines)-1:
                    await self.add_to_data_base(ctx, dados)
            else:
                await ctx.send("Por favor mande as informações: prontuário nome email." + 
                               " Caso nome composto adicionar entre aspas."
                               )
                break

    async def add_to_data_base(self, ctx, dados):
        with open("src/10-Discord_bot/alunos/alunos.txt", 'a', encoding='UTF-8') as arquivo_a:
            arquivo_a.write( dados +"\n")
            await ctx.send("Cadastrado com sucesso.")

async def setup(bot):
    await bot.add_cog(Cadastro(bot))