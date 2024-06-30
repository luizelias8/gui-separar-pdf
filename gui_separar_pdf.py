import PySimpleGUI as sg
from PyPDF2 import PdfReader, PdfWriter
import os

# Definir o tema escuro
sg.theme('DarkGrey10')

def parsear_intervalos_paginas(intervalos_paginas):
    paginas = set()
    intervalos = intervalos_paginas.split(',')

    for intervalo in intervalos:
        if '-' in intervalo:
            inicio, fim = map(int, intervalo.split('-'))
            if inicio > 0 and fim > 0 and fim >= inicio:
                paginas.update(range(inicio, fim + 1))
            else:
                sg.popup_error(f'Erro: Intervalo de páginas inválido: {intervalo}')
                return None
        else:
            pagina = int(intervalo)
            if pagina > 0:
                paginas.add(pagina)
            else:
                sg.popup_error(f'Erro: Número de página inválido: {pagina}')
                return None

    return sorted(paginas)

def extrair_paginas(pdf_entrada, intervalos_paginas, dir_saida, nome_arquivo_base):
    leitor = PdfReader(pdf_entrada)
    intervalos_conjuntos = intervalos_paginas.split(';')
    for contador, intervalos in enumerate(intervalos_conjuntos, start=1):
        escritor = PdfWriter()
        paginas = parsear_intervalos_paginas(intervalos)

        if paginas is None:
            return

        for pagina in paginas:
            if pagina <= len(leitor.pages):
                escritor.add_page(leitor.pages[pagina - 1])
            else:
                sg.popup_error(f'Erro: Página {pagina} não existe no documento.')
                return

        novo_nome = f'{nome_arquivo_base}_{contador}.pdf'
        caminho_saida = os.path.join(dir_saida, novo_nome)

        with open(caminho_saida, 'wb') as arquivo_saida:
            escritor.write(arquivo_saida)

    sg.popup(f'Páginas extraídas para {dir_saida}')

def main():
    layout = [
        [
            sg.Text('Arquivo PDF de ntrada'),
            sg.Input(key='pdf_entrada'),
            sg.FileBrowse(button_text='Selecionar', file_types=(('PDF Files', '*.pdf'),))
        ],
        [
            sg.Text('Intervalos de Páginas (ex: 1,3-5,7)'),
            sg.Input(key='intervalos_paginas')
        ],
        [
            sg.Text('Diretório de Saída'),
            sg.Input(key='dir_saida'),
            sg.FolderBrowse(button_text='selecionar')
        ],
        [
            sg.Text('Nome Base para os Arquivos de Saída'),
            sg.Input(key='nome_base')
        ],
        [
            sg.Button('Separar'),
            sg.Button('Cancelar')
        ]
    ]

    janela = sg.Window('Separar Páginas de PDF', layout)

    while True:
        evento, valores = janela.read()

        if evento == sg.WIN_CLOSED or evento == 'Cancelar':
            break

        if evento == 'Separar':
            pdf_entrada = valores['pdf_entrada']
            intervalos_paginas = valores['intervalos_paginas']
            dir_saida = valores['dir_saida'] or os.path.dirname(os.path.abspath(pdf_entrada))
            nome_base = valores['nome_base'] or os.path.splitext(os.path.basename(pdf_entrada))[0]

            if not os.path.exists(pdf_entrada):
                sg.popup_error(f'Erro: O arquivo "{pdf_entrada}" não existe.')
                continue

            if not os.path.exists(dir_saida):
                sg.popup_error(f'Erro: O diretório "{dir_saida}" não existe.')
                continue

            extrair_paginas(pdf_entrada, intervalos_paginas, dir_saida, nome_base)

    janela.close()

if __name__ == '__main__':
    main()