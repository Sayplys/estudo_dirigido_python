""" cadastra os alunos """

from discord.ext import commands 
import discord
from discord import app_commands

class Cadastro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description= "Cadastra aluno.")
    async def cadastrar(self, interaction: discord.Interaction, prontuario: str, nome: str,email: str ):
        await interaction.response.send_message('cadastando...')
        dados = f'{prontuario},{nome},{email}'

        with open("src/10-Discord_bot/alunos/alunos.txt", 'r', encoding='UTF-8') as arquivo_r:
            lines = arquivo_r.readlines()
            if len(lines) != 0:
                await self.check_occurrence(interaction, lines, prontuario, email, dados)
            else:
                await self.add_to_data_base(interaction, dados)
 
    async def check_occurrence(self, interaction, lines, prontuario, email, dados):
        await interaction.followup.send("Checando ocorrência...")

        for index, line in enumerate(lines):
            line_data = line.strip().split(',')

            if line_data[0] == prontuario and line_data[2] == email:
                if line_data[0] == prontuario:
                    await interaction.followup.send(
                        "Já existe um aluno cadastrado com esse prontuário." + 
                        " Por favor indique outro."
                    )

                if line_data[2] == email:
                    await interaction.followup.send(
                        "Já existe um aluno cadastrado com esse email." +
                        " Por favor indique outro."
                    )
                    break

            elif index == len(lines)-1:
                await self.add_to_data_base(interaction, dados)

    async def add_to_data_base(self, interaction, dados):
        with open("src/10-Discord_bot/alunos/alunos.txt", 'a', encoding='UTF-8') as arquivo_a:
            arquivo_a.write( dados +"\n")
            await interaction.followup.send("Cadastrado com sucesso.")

async def setup(bot):
    await bot.add_cog(Cadastro(bot),  guilds=[discord.Object(id=1110550192534589543)])