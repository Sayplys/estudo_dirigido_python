from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image

# Criação do arquivo PDF
pdf_filename = "exemplo.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Estilos
styles = getSampleStyleSheet()
titulo_style = styles["Title"]
paragrafo_style = styles["Normal"]

# Conteúdo do documento
conteudo = []

#Image
imagem = Image("src/10-reportlab/reportlab_img.png")
imagem.drawWidth = 175
imagem.drawHeight = 150
conteudo.append(imagem)

# Título
titulo = "Título do Documento"
titulo_espacamento = Spacer(1, 20 )  # Espaçamento de 20pt
titulo_paragrafo = Paragraph(titulo, titulo_style)
conteudo.extend([ titulo_paragrafo, titulo_espacamento])

# Parágrafo
paragrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
paragrafo_espacamento = Spacer(1, 15 )  # Espaçamento de 15pt
paragrafo_paragrafo = Paragraph(paragrafo, paragrafo_style)
conteudo.extend([ paragrafo_paragrafo, paragrafo_espacamento])

# Tabela
dados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    ["Dado 1", "Dado 2", "Dado 3", "Dado 4"]
]
tabela = Table(dados)
conteudo.append(tabela)

# Construção do documento PDF
doc.build(conteudo)
