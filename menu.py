from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *

import gamestates


class Menu():
    def __init__(self, janela, mouse):
        self.janela = janela
        self.mouse = mouse

        self.background = GameImage("images/menu/background.jpg")

        self.play_button = Sprite("images/menu/play_button.png")
        self.level_button = Sprite("images/menu/level_button.png")
        self.quit_button = Sprite("images/menu/quit_button.png")

        self.titulo = Sprite("images/menu/titulo.png")

        self.menu_sound = Sound("sounds/Nothingness.ogg")
        self.menu_sound.set_repeat(repeat=True)
        self.menu_sound.set_volume(20)

    def posiciona_botoes(self):
        self.play_button.x = self.janela.width - 1.1*self.play_button.width
        self.play_button.y = 100

        self.level_button.x = self.play_button.x
        self.level_button.y = 300

        self.quit_button.x = self.level_button.x
        self.quit_button.y = 500

    def effect(self):
        #effect over
        if self.mouse.is_over_object(self.play_button):
            self.play_button.x -= 50
        elif self.mouse.is_over_object(self.level_button):
            self.level_button.x -= 50
        elif self.mouse.is_over_object(self.quit_button):
            self.quit_button.x -= 50

        #effect click
        if self.mouse.is_over_object(self.play_button) and self.mouse.is_button_pressed(1):
            gamestates.GameState = 1
        if self.mouse.is_over_object(self.level_button) and self.mouse.is_button_pressed(1):
            gamestates.GameState = 0.1
        if self.mouse.is_over_object(self.quit_button) and self.mouse.is_button_pressed(1):
            sys.exit()

    def toca_musica(self):
        if gamestates.GameState == 0 or gamestates.GameState == 0.1:
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
