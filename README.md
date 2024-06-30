# Separador de Páginas de PDF com Interface Gráfica

## Descrição

Projeto em Python para separar páginas de arquivos PDF, permitindo extrair intervalos específicos de páginas e salvá-las em novos arquivos PDF. Utiliza uma interface gráfica construída com **PySimpleGUI** e manipula os arquivos PDF usando a biblioteca **PyPDF2**.

## Funcionalidades

- Separação de páginas de PDF: Extrai páginas específicas de um arquivo PDF.
- Interface Gráfica: Interface fácil de usar.
- Suporte a intervalos: Suporte para intervalos de páginas, como 1,3-5,7.
- Diretório de Saída: Escolha o diretório onde os arquivos PDF extraídos serão salvos.
- Nome Base Personalizado: Defina um nome base para os novos arquivos PDF.

## Requisitos

- Python 3.x
- Bibliotecas Python: PySimpleGUI, PyPDF2

## Instalação

Clone o repositório:

```
git clone https://github.com/luizelias8/gui-separar-pdf.git
cd gui-separar-pdf
```

Instale os requisitos necessários:
```
pip install -r requirements.txt
```

## Uso

1. Execute o script:

```
python gui_separar_pdf.py
```

2. Selecione um arquivo PDF de entrada.

3. Insira os intervalos de páginas que deseja extrair (ex: 1,3-5,7).

4. Opcionalmente, Escolha o diretório de saída onde os novos PDFs serão salvos.

5. Opcionalmente, defina um nome base para os novos arquivos.

6. Clique em "Separar" para extrair as páginas.

## Contribuição

Contribuições são bem-vindas!

## Autor

[Luiz Elias](https://github.com/luizelias8)