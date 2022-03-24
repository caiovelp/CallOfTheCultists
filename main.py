from PPlay.window import *
from PPlay.sound import *

import gamestates
from cutscene import *
from cutscene2 import *
from cutscene3 import *
from cutscene4 import *
from cutscene5 import *
from cutscene6 import *
from menu import *
from dificuldademenu import *
from gamestates import *

import Battle1

#Inicialização
janela = Window(1280, 720)
janela.set_title("Call of Cultists")

mouse = Window.get_mouse()
teclado = Window.get_keyboard()

cutscene = Cutscene(janela)
cutscene2 = Cutscene2(janela)
cutscene3 = Cutscene3(janela)
cutscene4 = Cutscene4(janela)
cutscene5 = Cutscene5(janela)
cutscene6 = Cutscene6(janela)
menu = Menu(janela, mouse)
dificuldademenu = MenuD(janela, mouse, teclado)

tela_vitoria = Sprite("images/backgrounds/VICTORY.png")
mensagem_final = Sprite("images/backgrounds/finalscreen.png")
contador = 0

tela_derrota = Sprite("images/backgrounds/GAMEOVER.png")

sound_battle1 = Sound("sounds/battle1.ogg")



while True:
    if gamestates.GameState == 0:
        gamestates.SoundStates = 0
        menu.run()
    elif gamestates.GameState == 0.1:
        dificuldademenu.run()
    elif gamestates.GameState == 1:
        gamestates.SoundStates = 0
        cutscene.run()
    elif gamestates.GameState == 2:
        gamestates.SoundStates = 0
        cutscene2.run()
    elif gamestates.GameState == 3:
        gamestates.SoundStates = 1
        batalha1 = Battle1.battle(Battle1.nomeDoPersonagem1, Battle1.nomeDoPersonagem2, Battle1.vilao1, Battle1.gameData)
        if batalha1 == "Vitoria":
            gamestates.GameState = 4
            gamestates.SoundStates = 0
        else:
            gamestates.GameState = 11
    elif gamestates.GameState == 4:
        gamestates.SoundStates = 0
        cutscene3.run()
    elif gamestates.GameState == 5:
        gamestates.SoundStates = 0
        cutscene4.run()
    elif gamestates.GameState == 6:
        gamestates.SoundStates = 2
        batalha2 = Battle1.battle(Battle1.nomeDoPersonagem1, Battle1.nomeDoPersonagem2, Battle1.vilao2, Battle1.gameData)
        if batalha2 == "Vitoria":
            gamestates.GameState = 7
        else:
            gamestates.GameState = 11
    elif gamestates.GameState == 7:
        gamestates.SoundStates = 0
        cutscene5.run()
    elif gamestates.GameState == 8:
        gamestates.SoundStates = 3
        batalha3 = Battle1.battle(Battle1.nomeDoPersonagem1, Battle1.nomeDoPersonagem2, Battle1.vilao3, Battle1.gameData)
        if batalha3 == "Vitoria":
            gamestates.GameState = 9
        else:
            gamestates.GameState = 11
    elif gamestates.GameState == 9:
        gamestates.SoundStates = 0
        cutscene6.run()
    elif gamestates.GameState == 10:
        contador += 0.05
        if contador < 570:
            janela.set_background_color([0,0,0])
            mensagem_final.draw()
        else:
            janela.set_background_color([255,255,255])
            tela_vitoria.draw()
    elif gamestates.GameState == 11:
        janela.set_background_color([0,0,0])
        tela_derrota.draw()

    if gamestates.SoundStates == 0:
        Battle1.sound_battle1.stop()
        Battle1.sound_battle2.stop()
        Battle1.sound_battle3.stop()
    janela.update()