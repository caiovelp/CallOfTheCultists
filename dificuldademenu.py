from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *

import gamestates


class MenuD():
    def __init__(self, janela, mouse, teclado):
        self.janela = janela
        self.mouse = mouse
        self.teclado = teclado

        self.background = GameImage("images/menu/background.jpg")

        self.play_button = Sprite("images/menu/easy.png")
        self.level_button = Sprite("images/menu/medium.png")
        self.quit_button = Sprite("images/menu/HARD.png")

        self.titulo = Sprite("images/menu/titulo.png")

        self.menu_sound = Sound("sounds/Nothingness.ogg")
        self.menu_sound.set_repeat(repeat=True)
        self.menu_sound.set_volume(20)

    def posiciona_botoes(self):
        self.play_button.x = 650
        self.play_button.y = 100

        self.level_button.x = 650
        self.level_button.y = 300

        self.quit_button.x = 650
        self.quit_button.y = 500

    def effect(self):
        #effect over
        if self.mouse.is_over_object(self.play_button):
            self.play_button.x += 50
        elif self.mouse.is_over_object(self.level_button):
            self.level_button.x += 50
        elif self.mouse.is_over_object(self.quit_button):
            self.quit_button.x += 50

        #effect click
        if self.mouse.is_over_object(self.play_button) and self.mouse.is_button_pressed(1):
            gamestates.Dificuldade = 1
            gamestates.GameState = 0
        if self.mouse.is_over_object(self.level_button) and self.mouse.is_button_pressed(1):
            gamestates.Dificuldade = 1.5
            gamestates.GameState = 0
        if self.mouse.is_over_object(self.quit_button) and self.mouse.is_button_pressed(1):
            gamestates.Dificuldade = 2
            gamestates.GameState = 0

        if self.teclado.key_pressed("esc"):
            gamestates.GameState = 0

    def toca_musica(self):
        if gamestates.GameState == 0:
            self.menu_sound.play()
        else:
            self.menu_sound.stop()

    def run(self):
        #function
        self.posiciona_botoes()
        self.effect()
        self.toca_musica()

        #draws
        self.background.draw()
        self.play_button.draw()
        self.level_button.draw()
        self.quit_button.draw()
        self.titulo.draw()
