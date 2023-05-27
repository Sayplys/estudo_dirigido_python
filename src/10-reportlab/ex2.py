from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Cria um documento PDF usando o tamanho da página "letter"
pdf = SimpleDocTemplate("documento.pdf", pagesize=letter)

# Obtém um estilo de amostra para parágrafos e cabeçalhos
styles = getSampleStyleSheet()

# Cria uma lista de elementos para o conteúdo do PDF
conteudo = []

# Adiciona um título
titulo = Paragraph("<font size=16>Título do Documento</font>", styles["Title"])
conteudo.append(titulo)

# Adiciona espaço entre o título e o primeiro parágrafo
espaco1 = Spacer(1, 20)  # 20 pontos de altura
conteudo.append(espaco1)

# Adiciona o primeiro parágrafo
paragrafo1 = Paragraph("Este é o primeiro parágrafo.", styles["Normal"])
conteudo.append(paragrafo1)

# Adiciona espaço entre os parágrafos
espaco2 = Spacer(1, 15)  # 15 pontos de altura
conteudo.append(espaco2)

# Adiciona o segundo parágrafo
paragrafo2 = Paragraph("Este é o segundo parágrafo.", styles["Normal"])
conteudo.append(paragrafo2)
conteudo.append(espaco2)
paragrafo_style = ParagraphStyle(
    'paragrafo',
    fontName='Helvetica',
    fontSize=12,
    leading=10,
    alignment=1
)
texto1 = 'adsfdaf'

conteudo.extend([ Paragraph(texto1, paragrafo_style), espaco2])


paragrafo_style2 = ParagraphStyle(
    'paragrafo',
    fontName='Helvetica',
    fontSize=10,
    leading=7,
    alingment=0
)
texto2 = '1asf'
conteudo.extend([Paragraph(texto2, paragrafo_style2), espaco2])

# Gera o PDF com o conteúdo definido
pdf.build(conteudo)
