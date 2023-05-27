""" Manda um pdf com a lista de alunos """

import discord
from discord.ext import commands
from discord import app_commands
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors    

class ListarEmPdf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ls-aluno_pdf", description="Manda lista de alunos em pdf")
    async def listar(self,interaction: discord.Interaction):
        pdf = SimpleDocTemplate('lista_de_alunos.pdf', pagesize=letter)
        styles = getSampleStyleSheet()
        conteudo = []
        
        titulo_style = styles['Title']
        titulo_style.alignment = 0
        titulo = Paragraph('Alunos Cadastrados', titulo_style)

        espaco1 = Spacer(1, 30)
        dados = [['Prontuário', 'Nome', 'E-mail']]
        with open("src/09-Discord_bot/alunos/alunos.txt", "r", encoding="UTF-8") as arquivo:
            for linha in arquivo.readlines():
                dados_da_linha = linha.strip().split(',')
                dados.append([
                    dados_da_linha[0], 
                    dados_da_linha[1],
                    dados_da_linha[2]
                ])

            tabela = Table(dados)
            tabela.setStyle(([
                ('BACKGROUND', (0,0), (3,0), colors.black),
                ('TEXTCOLOR',(0,0),(3,0),colors.white),
                ('FONTNAME', (0,0), (3,0), 'Helvetica-Bold'),
                ('INNERGRID',(0,0),(-1,-1), 0.5, colors.black),
                ('BOX', (0,0), (-1,-1), 0.5, colors.black),
                ('WIDTH', (0, 0), (-1, -1), 50),
            ]))

            espaco2 = Spacer(1, 15)

            contador = Paragraph(f'Total de alunos {len(dados) - 1}', styles['Heading4'])

        conteudo.extend([titulo, espaco1, tabela, espaco2, contador])
        
        pdf.build(conteudo)

        await interaction.response.send_message(file=discord.File('lista_de_alunos.pdf', 'nome_do_arquivo.pdf'))           


async def setup(bot):
    await bot.add_cog(ListarEmPdf(bot),  guilds=[discord.Object(id=1110550192534589543)])