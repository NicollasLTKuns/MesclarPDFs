import os
import pypdf

pdfs_selecionado = []

pdfs_mesclados = pypdf.PdfWriter()

for pdf in pdfs_selecionado:
    pdfs_mesclados.append(pdf)

pasta = "./NovosPDFs"

if not os.path.exists(pasta):
    os.makedirs(pasta)


saida = os.path.join(pasta, "resultado.pdf")

pdfs_mesclados.write(saida)