import pypdf


def mesclar_pdfs(arquivos, caminho_saida):
    pdf_mesclados = pypdf.PdfWriter()

    for arquivo in arquivos:
        pdf_mesclados.append(arquivo)

    pdf_mesclados.write(caminho_saida)