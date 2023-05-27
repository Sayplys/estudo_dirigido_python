""" cadastra os alunos """

from discord.ext import commands
import discord
from discord import ui, app_commands

class Cadastro(ui.Modal, title="Cadastro de aluno"):
    prontuario = ui.TextInput(label='Prontuário', placeholder="xxxxxx", style=discord.TextStyle.short)
    nome = ui.TextInput(label='name', placeholder='xxxxxx', style=discord.TextStyle.short)
    email = ui.TextInput(label='email', placeholder='xxx@xxxx.com', style=discord.TextStyle.short)
    
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message('cadastando...')
        dados = f'{self.prontuario},{self.nome},{self.email}'

        with open("src/10-Discord_bot/alunos/alunos.txt", 'r', encoding='UTF-8') as arquivo_r:
            lines = arquivo_r.readlines()
            if len(lines) != 0:
                await self.check_occurrence(interaction, lines, dados)
            else:
                await self.add_to_data_base(interaction, dados)
 
    async def check_occurrence(self, interaction, lines, dados):
        await interaction.followup.send("Checando ocorrência...")

        for index, line in enumerate(lines):
            line_data = line.strip().split(',')
            if line_data[0] == str(self.prontuario) or line_data[2] == str(self.email):
                if line_data[0] == str(self.prontuario):
                    await interaction.followup.send(
                        "Já existe um aluno cadastrado com esse prontuário." + 
                        " Por favor indique outro."
                    )
                    break

                if line_data[2] == str(self.email):
                    await interaction.followup.send(
                        "Já existe um aluno cadastrado com esse email." +
                        " Por favor indique outro."
                    )
                    break

            elif index == len(lines)-1:
                await self.add_to_data_base(interaction, dados)
                break

    async def add_to_data_base(self, interaction, dados):
        with open("src/10-Discord_bot/alunos/alunos.txt", 'a', encoding='UTF-8') as arquivo_a:
            arquivo_a.write( dados +"\n")
            await interaction.followup.send("Cadastrado com sucesso.")

    
class SendModal(commands.Cog):
    @app_commands.command(name="cadastro", description="Cadastra alunos.")
    async def send_modal(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Cadastro())

async def setup(bot):
    await bot.add_cog(SendModal(bot),  guilds=[discord.Object(id=1110550192534589543)])