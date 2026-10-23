import os
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QListWidget,
    QMessageBox,
    QToolButton,
    QHBoxLayout,
    QLabel,
    QListWidgetItem
)
from PySide6.QtCore import Signal, QTimer
import traceback
from funcoes import mesclar_pdfs

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.pdfs_selecionados = []

        self.setWindowTitle("Mesclar PDFs")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.botao_add = QPushButton("Selecionar Arquivos")
        self.botao_mesclar = QPushButton("Mesclar PDFs")
        self.lista_pdfs = QListWidget()

        layout.addWidget(self.botao_add)
        layout.addWidget(self.lista_pdfs)
        layout.addWidget(self.botao_mesclar)

        self.setLayout(layout)

        # Conecta o botão ao método
        self.botao_add.clicked.connect(self.adicionar_pdfs)
        self.botao_mesclar.clicked.connect(self.mesclar_pdf)

    def adicionar_pdfs(self):
        arquivos, _ = QFileDialog.getOpenFileNames(
            self,
            "Selecionar arquivos",
            os.path.expanduser("~"),
            "Arquivo PDF (*.pdf)"
        )

        for arquivo in arquivos:
            if arquivo not in self.pdfs_selecionados:
                self.pdfs_selecionados.append(arquivo)

                nome_arquivo = os.path.basename(arquivo)

                item = QListWidgetItem()
                widget = ItemPDF(nome_arquivo)

                item.setSizeHint(widget.sizeHint())

                self.lista_pdfs.addItem(item)
                self.lista_pdfs.setItemWidget(item, widget)

                widget.remover_solicitacao.connect(
                    lambda widget=widget: self.remover_pdf(widget)
                )

                widget.subir_solicitacao.connect(
                    lambda widget=widget: self.testar_subir_pdf(widget)
                )

                widget.descer_solicitacao.connect(
                    lambda widget=widget: self.testar_descer_pdf(widget)
                )

    def remover_pdf(self, widget):
        for i in range(self.lista_pdfs.count()):
            item = self.lista_pdfs.item(i)

            if self.lista_pdfs.itemWidget(item) == widget:
                self.lista_pdfs.takeItem(i)
                del self.pdfs_selecionados[i]
                break
    def subir_pdf(self, widget):
        for i in range(self.lista_pdfs.count()):
            item = self.lista_pdfs.item(i)

            if self.lista_pdfs.itemWidget(item) == widget:
                if i == 0:
                    return

                self.pdfs_selecionados[i - 1], self.pdfs_selecionados[i] = (
                    self.pdfs_selecionados[i],
                    self.pdfs_selecionados[i - 1]
                )

                QTimer.singleShot(0, self.atualizar_lista)
                return
            
    def testar_subir_pdf(self, widget):
        try:
            self.subir_pdf(widget)
        except Exception:
            traceback.print_exc()

    def descer_pdf(self, widget):
        for i in range(self.lista_pdfs.count()):
            item = self.lista_pdfs.item(i)

            if self.lista_pdfs.itemWidget(item) == widget:
                if i == self.lista_pdfs.count() - 1:
                    return

                self.pdfs_selecionados[i], self.pdfs_selecionados[i + 1] = (
                    self.pdfs_selecionados[i + 1],
                    self.pdfs_selecionados[i]
                )

                QTimer.singleShot(0, self.atualizar_lista)
                return
            
    def testar_descer_pdf(self, widget):
        try:
            self.descer_pdf(widget)
        except Exception:
            traceback.print_exc()

    def atualizar_lista(self):
        self.lista_pdfs.clear()

        for arquivo in self.pdfs_selecionados:
            nome_arquivo = os.path.basename(arquivo)

            item = QListWidgetItem()
            widget = ItemPDF(nome_arquivo)

            item.setSizeHint(widget.sizeHint())

            self.lista_pdfs.addItem(item)
            self.lista_pdfs.setItemWidget(item, widget)

            widget.remover_solicitacao.connect(
                lambda widget=widget: self.remover_pdf(widget)
            )

            widget.subir_solicitacao.connect(
                lambda widget=widget: self.testar_subir_pdf(widget)
            )

            widget.descer_solicitacao.connect(
                lambda widget=widget: self.testar_descer_pdf(widget)
            )

    
    def mesclar_pdf(self):
        if not self.pdfs_selecionados:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione pelo menos um PDF"
            )
            return

        caminho_saida, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar PDF mesclado",
            "PDFMesclado.pdf",
            "Arquivo PDF (*.pdf)"
        )

        if not caminho_saida:
            return

        try:
            mesclar_pdfs(self.pdfs_selecionados, caminho_saida)

            self.lista_pdfs.clear()
            self.pdfs_selecionados.clear()

            QMessageBox.information(
                self,
                "Sucesso",
                "Os PDFs foram mesclados com sucesso!"
            )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível mesclar os PDFs.\n\nDetalhes: {erro}"
            )

class ItemPDF(QWidget):
    remover_solicitacao = Signal()
    subir_solicitacao = Signal()
    descer_solicitacao = Signal()

    def __init__(self, nome_arquivo):
        super().__init__()

        self.layout = QHBoxLayout(self)

        self.nome = QLabel(nome_arquivo)

        self.botao_subir = QToolButton()
        self.botao_subir.setText("↑")
        self.botao_subir.clicked.connect(
            self.subir_solicitacao.emit
        )

        self.botao_descer = QToolButton()
        self.botao_descer.setText("↓")
        self.botao_descer.clicked.connect(
            self.descer_solicitacao.emit
        )

        self.botao_remover = QToolButton()
        self.botao_remover.setText("×")
        self.botao_remover.clicked.connect(
            self.remover_solicitacao.emit
        )

        self.botao_subir.hide()
        self.botao_descer.hide()
        self.botao_remover.hide()

        self.layout.addWidget(self.nome)
        self.layout.addStretch()
        self.layout.addWidget(self.botao_subir)
        self.layout.addWidget(self.botao_descer)
        self.layout.addWidget(self.botao_remover)

    def enterEvent(self, event):
        self.botao_subir.show()
        self.botao_descer.show()
        self.botao_remover.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.botao_subir.hide()
        self.botao_descer.hide()
        self.botao_remover.hide()        
        super().leaveEvent(event)