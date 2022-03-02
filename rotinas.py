# Importa a biblioteca pyautogui
import pyautogui

# Importa a biblioteca time
import time

# Importa a biblioteca pyperclip
import pyperclip


def esperar_pagina_carregar(img):
    '''Espera até que a imagem apareça na tela para poder executar uma ação.'''

    while not pyautogui.locateOnScreen(img):
        time.sleep(0.5)
        

def copiar_colar(conteudo):
    '''Copia o conteúdo para a área de transferência e depois cola'''
    # Copia conteúdo para a área de transferência
    pyperclip.copy(conteudo)
    
    # Cola o conteúdo
    pyautogui.hotkey('ctrl', 'v')