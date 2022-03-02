# Importa o módulo rotinas
from rotinas import clicar_imagem, esperar_pagina_carregar

# Importa a biblioteca pandas
import pandas as pd

# Importa a biblioteca pyautogui
import pyautogui

# Importa a biblioteca pyperclip
import pyperclip

# Importa a biblioteca os
import os

# Importa o método load_doten
from dotenv import load_dotenv

# Importa a biblioteca time
import time

# Carrega as variáveis de ambiente
load_dotenv()

# Intervalo entre os comandos do pyautogui
pyautogui.PAUSE = 1

# Pergunta se o usuário quer dar início à automação
confirmacao = pyautogui.confirm(
    text='Deseja iniciar a automação?',
    buttons=['OK', 'Cancelar']
)

# Solicita que o usuário digite sua senha
senha = pyautogui.password(
    text='Digite sua senha',
    mask='*'
)

if confirmacao == 'OK' and senha == os.getenv('SENHA_AUTOMACAO'):
    # Exibe uma mensagem de alerta ao usuário
    pyautogui.alert(
        text='Por favor, não seu mouse nem seu teclado enquanto a automação estiver em execução.',
        button='OK'
    )

    # Abrindo o navegador (Google Chrome)

    # Pressiona a tecla de logo do Windows
    pyautogui.press('win')

    # Digita o texto no campo de busca
    pyautogui.write('chrome')

    # Pressiona a tecla enter
    pyautogui.press('enter')

    # Digita a URL especificada
    pyautogui.write('https://mail.google.com/')
    pyautogui.press('enter')

    # Espera o Gmail carregar
    esperar_pagina_carregar('tela_inicial_gmail.png')

    # Clicar no menu do Google Apps
    clicar_imagem('google_apps_menu.png')

    # Clicar no ícone do Google Contatos
    clicar_imagem('icone_google_contatos.png')

    # Esperar página do Google Contatos carregar
    esperar_pagina_carregar('icone_google_contatos_tela_principal.png')

    # Clicar no botão de exportação
    clicar_imagem('botao_exportar_menu_google_contatos.png')

    # Esperar menu modal carregar e confirmar a exportação
    esperar_pagina_carregar('botao_exportar_menu_modal.png')
    clicar_imagem('botao_exportar_menu_modal.png')

    # Aguarda 10s até que o arquivo seja baixado
    time.sleep(10)

    # Caminho do arquivo baixado
    caminho = os.getenv('CAMINHO')

    # Criação do dataframe
    df_contatos = pd.read_csv(caminho)

    # Elimina as colunas vazias do dataframe
    df_contatos.dropna(axis=1, how='all', inplace=True)

    # Usa o atalho Ctrl + PgUp para voltar para a tela do Gmail
    pyautogui.hotkey('ctrl', 'pgup')

    # Clica no botão para escrever o e-mail
    clicar_imagem('botao_escrever_gmail.png')

    # Percorre cada linha do dataframe para obter as informações de contato
    for i, email in enumerate(df_contatos['E-mail 1 - Value']):
        # Nome do destinatário
        nome = df_contatos.loc[i, 'Name']

        # Escreve o e-mail do destinatário
        pyautogui.write(email)

        # Confirma o contato
        pyautogui.press('enter')

        # Pula para o campo de assunto
        pyautogui.press('tab')
        pyautogui.write('Teste de Automação com Python')

        # Pula para o campo de corpo do e-mail
        pyautogui.press('tab')

        # Mensagem a ser enviada
        mensagem = f'''
        Olá, {nome}!
        Estou lhe mandando este e-mail para testar uma automação com Python.
        Peço que não se assuste.
        Att.
        Diego Moura Torres
        '''

        # Copia conteúdo da mensagem para a área de transferência
        pyperclip.copy(mensagem)

        # Cola a mensagem
        pyautogui.hotkey('ctrl', 'v')

        # Envia o e-mail usando um atalho
        pyautogui.hotkey('ctrl', 'enter')

else:
    pass

pyautogui.prompt(
    text='Fim da automação. Agora você já pode usar seu computador.'
)
