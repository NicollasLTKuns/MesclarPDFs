import sys
import os
import pypdf
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QListWidget,
    QMessageBox,
    QToolBox,
    QHBoxLayout,
    QLabel
)
from PySide6.QtCore import Qt

pdfs_selecionados = []

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Mesclar PDFs")
janela.resize(800, 500)

layout = QVBoxLayout()

botao_add = QPushButton("Selecionar Arquivos")
botao_remover = QPushButton("Remover Arquivo")
botao_mesclar = QPushButton("Mesclar PDFs")
lista_pdfs = QListWidget()

layout.addWidget(botao_add)
layout.addWidget(botao_remover)
layout.addWidget(lista_pdfs)
layout.addWidget(botao_mesclar)
janela.setLayout(layout)

def adicionar_pdfs():
    arquivos, _ = QFileDialog.getOpenFileNames(
        janela,
        "selecionar arquivos",
        os.path.expanduser("~"),
        "Arquivo PDF (*.pdf)"
    )

    for arquivo in arquivos:
        if arquivo not in pdfs_selecionados:
            pdfs_selecionados.append(arquivo)
            lista_pdfs.addItem(os.path.basename(arquivo))

def remover_pdf():
    arquivo_selecionado = lista_pdfs.currentRow()
    if arquivo_selecionado != -1:
        lista_pdfs.takeItem(arquivo_selecionado)
        del pdfs_selecionados[arquivo_selecionado]

def mesclar_pdf():
    if not pdfs_selecionados:
        QMessageBox.warning(
            janela,
            "Atenção",
            "Selecione pelo menos um PDF"
        )
        return

    caminho_sainda, _ = QFileDialog.getSaveFileName(
        janela,
        "Salvar PDF mesclado",
        "PDFMesclado.pdf",
        "arquivo PDF (*.pdf)"
    )

    try:
        if not caminho_sainda:
            return

        pdf_mesclados = pypdf.PdfWriter()
        for pdf in pdfs_selecionados:
            pdf_mesclados.append(pdf)

        pdf_mesclados.write(caminho_sainda)

        lista_pdfs.clear()
        pdfs_selecionados.clear()

        QMessageBox.information(
            janela,
            "Sucesso",
            "Os PDFs foram mesclados com Sucesso!"
        )
    except Exception as erro:
        QMessageBox.critical(
            janela,
            "Erro"
            f"Não foi possivel mesclar os PDFs.\n\nDetalhes: {erro}"
        )

botao_add.clicked.connect(adicionar_pdfs)
botao_remover.clicked.connect(remover_pdf)
botao_mesclar.clicked.connect(mesclar_pdf)

janela.show()
sys.exit(app.exec())