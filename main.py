import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from interface import JanelaPrincipal

app = QApplication(sys.argv)

caminho_estilo = Path(__file__).with_name("style.qss")

with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
    app.setStyleSheet(arquivo.read())

janela = JanelaPrincipal()
janela.show()

sys.exit(app.exec())