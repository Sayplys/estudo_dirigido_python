from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, blue
from reportlab.lib.units import inch

# Cria o documento PDF
pdf = canvas.Canvas("hello_world.pdf", pagesize=letter)

# Desenha um retângulo azul
pdf.setFillColor(blue)
pdf.rect(1 * inch, 1 * inch, 2 * inch, 1 * inch, fill=True)

# Desenha um círculo vermelho
pdf.setFillColor(red)
pdf.circle(5 * inch, 5 * inch, 0.5 * inch, fill=True)

# Escreve a string "Hello World" na posição (3 polegadas, 3 polegadas)
pdf.setFont("Helvetica", 12)
pdf.drawString(3 * inch, 3 * inch, "Hello World")

# Salva o documento PDF
pdf.save()
