from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene5():
    def __init__(self, janela):
        self.janela = janela

        #region Backgrounds e mapas
        self.background2 = GameImage("images/backgrounds/background2.jpg")
        #endregion

        #region Personagens
        self.detetive = Sprite("images/personagens/detetive/0.png")
        self.detetive.x = 300 - self.detetive.width
        self.detetive.y = 540 - self.detetive.height

        self.japones = Sprite("images/personagens/japones/0.png")
        self.japones.x = 200 - self.japones.width
        self.japones.y = 545 - self.japones.height
        #endregion

        #region Cultista
        self.cultista = Sprite("images/personagens/cultista/cultista.png")
        self.cultista.x = 1082.39 - self.cultista.width
        self.cultista.y = 540 - self.cultista.height

        #region Dialogo
        self.fundo_dialogo = Sprite("images/dialogo/fundo.png")
        self.fundo_dialogo.y = 500

        self.detetive_face = Sprite("images/dialogo/detetive_face.png")
        self.detetive_face.y = 520
        self.detetive_face.x = 100

        self.japones_face = Sprite("images/dialogo/japones_face.png")
        self.japones_face.y = 520
        self.japones_face.x = 100

        self.cultista_face = Sprite("images/dialogo/cultista.png")
        self.cultista_face.y = 520
        self.cultista_face.x = 1100
        #endregion

        #region Indices
        self.cronometoIndice = 0
        self.corridaIndice = 0

        self.velocidade_camera = -1

        self.contador_dialogo5 = 0

        self.state_bonecos = "nada"

        self.velocidade_movimento = 0.3
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

    def cena(self):
        self.detetive.draw()
        self.japones.draw()
        self.cultista.draw()
        self.dialogo()

    def dialogo(self):
        self.contador_dialogo5 += gamestates.vel_cena

        if (1 < self.contador_dialogo5 < 5):
            self.fundo_dialogo.draw()
            self.cultista_face.draw()
            self.janela.draw_text("Então vocês são os intrusos de minha mansão...",
                                  x=self.cultista_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (5 < self.contador_dialogo5 < 10):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("O que está acontecendo aqui? Quem é você?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)
        if (10 < self.contador_dialogo5 < 15):
            self.fundo_dialogo.draw()
            self.cultista_face.draw()
            self.janela.draw_text("Detetive, você chegou tarde... A invocação já foi feita.",
                                  x=self.cultista_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (15 < self.contador_dialogo5 < 20):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Invocação? Do que você está falando?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (20 < self.contador_dialogo5 < 25):
            self.fundo_dialogo.draw()
            self.cultista_face.draw()
            self.janela.draw_text("Cyaegha está chegando, e não há nada que vocês possam fazer...",
                                  x=self.cultista_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (25 < self.contador_dialogo5 < 30):
            self.fundo_dialogo.draw()
            self.cultista_face.draw()
            self.janela.draw_text("Agora, sintam a fúria do avatar de Cyaegha na terra!",
                                  x=self.cultista_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo5 > 30):
            gamestates.GameState = 8

    def toca_musica(self):
        if gamestates.GameState == 7:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def run(self):
        #draw
        self.background2.draw()

        self.cena()

        self.toca_musica()