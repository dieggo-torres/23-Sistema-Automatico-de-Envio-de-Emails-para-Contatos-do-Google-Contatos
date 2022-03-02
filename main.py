# Importa métodos do módulo rotinas
import rotinas

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

# Carrega as variáveis de ambiente
load_dotenv()

# Intervalo entre os comandos do pyautogui
pyautogui.PAUSE = 2

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
    pyautogui.write('https://contacts.google.com/')
    pyautogui.press('enter')

    # Espera o Google Contatos carregar
    esperar_pagina_carregar('icone_google_contatos_tela_principal.png')

    # Clicar no botão de exportação
    pyautogui.click(x=104, y=509, button='left')

    # Esperar menu modal carregar e confirmar a exportação
    esperar_pagina_carregar('botao_exportar_menu_modal.png')
    pyautogui.click(x=810, y=540, button='left')

    # Caminho do arquivo baixado
    caminho = os.getenv('CAMINHO')

    # Criação do dataframe
    df_contatos = pd.read_csv(caminho)

    # Elimina as colunas vazias do dataframe
    df_contatos.dropna(axis=1, how='all', inplace=True)

    # Cria uma nova aba
    pyautogui.hotkey('ctrl', 't')

    # Digita a URL especificada e pressiona a tecla enter
    pyautogui.write('https://mail.google.com/')
    pyautogui.press('enter')

    # Espera o botão de escrever e-mail aparecer
    esperar_pagina_carregar('botao_escrever_gmail.png')

    # Percorre cada linha do dataframe para obter as informações de contato
    for i, email in enumerate(df_contatos['E-mail 1 - Value']):
        # Clica no botão de escrever e-mail
        pyautogui.click(x=80, y=171, button='left')

        # Nome do destinatário
        nome = df_contatos.loc[i, 'Name']

        # Escreve o e-mail do destinatário
        pyautogui.write(email)

        # Confirma o contato
        pyautogui.press('enter')

        # Pula para o campo de assunto e escreve o conteúdo
        pyautogui.press('tab')
        copiar_colar('Teste de Automação com Python')

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
        copiar_colar(mensagem)

        # Envia o e-mail usando um atalho
        pyautogui.hotkey('ctrl', 'enter')
else:
    pass

pyautogui.alert(
    text='Fim da automação. Agora você já pode usar seu computador.'
)
