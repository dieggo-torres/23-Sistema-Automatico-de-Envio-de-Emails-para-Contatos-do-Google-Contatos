# Importa a biblioteca pyautogui
import pyautogui

# Importa a biblioteca time
import time

# Funções a serem usadas em main.py
def clicar_imagem(img):
    '''Espera até que a imagem apareça na tela para depois clicar nela'''

    while not pyautogui.locateOnScreen(img):
        time.sleep(1)

    # Obtém as informações da imagem já carregada
    x, y, largura, altura = pyautogui.locateAllOnScreen(img)

    # Clica no meio da imagem
    pyautogui.click(x + largura /2, y + altura / 2)


def esperar_pagina_carregar(img):
    '''Espera até que a imagem apareça na tela para poder executar uma ação.'''

    while not pyautogui.locateOnScreen(img):
        time.sleep(1)