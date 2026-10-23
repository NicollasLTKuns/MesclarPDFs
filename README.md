# Mesclador de PDFs

Aplicação desktop desenvolvida em Python que permite selecionar, organizar e mesclar múltiplos arquivos PDF em um único documento, por meio de uma interface gráfica.

## Funcionalidades

- Selecionar múltiplos arquivos PDF.
- Impedir a adição duplicada do mesmo arquivo.
- Visualizar os arquivos selecionados.
- Remover arquivos da lista.
- Alterar a ordem dos arquivos antes da mesclagem.
- Escolher o nome e o local de salvamento do PDF resultante.
- Utilizar uma interface gráfica com tema escuro.

## Tecnologias utilizadas

- **Python** — linguagem de programação utilizada no desenvolvimento.
- **PySide6** — biblioteca utilizada para criar a interface gráfica.
- **pypdf** — biblioteca utilizada para manipular e mesclar arquivos PDF.
- **Qt Style Sheets (QSS)** — utilizado para personalizar a aparência da interface.

## Requisitos

- Python instalado no computador.
- Bibliotecas PySide6 e pypdf.

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/NicollasLTKuns/MesclarPDFs.git
```

### 2. Entre na pasta do projeto

```bash
cd mesclador-pdf
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows, usando PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python main.py
```

## Estrutura do projeto

```text
mesclador-pdf/
├── .gitignore
├── funcoes.py
├── interface.py
├── main.py
├── README.md
├── requirements.txt
└── style.qss
```

## Objetivo

O projeto tem como objetivo facilitar a organização de documentos digitais, permitindo reunir vários arquivos PDF em um único documento e definir a ordem em que suas páginas serão adicionadas.

## Autor

Desenvolvido por [NicollasLTKuns](https://github.com/NicollasLTKuns) como projeto de aprendizado em programação e desenvolvimento de software.