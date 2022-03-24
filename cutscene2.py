from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene2():
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

        #region Criança
        self.butcher0 = Sprite("images/personagens/butcher/0.png")
        self.butcher1 = Sprite("images/personagens/butcher/1.png")
        self.butcher2 = Sprite("images/personagens/butcher/2.png")
        self.butcher3 = Sprite("images/personagens/butcher/3.png")
        self.butcher4 = Sprite("images/personagens/butcher/4.png")
        self.butcher5 = Sprite("images/personagens/butcher/5.png")
        self.butcher6 = Sprite("images/personagens/butcher/6.png")
        self.butcher7 = Sprite("images/personagens/butcher/7.png")
        self.butcher8 = Sprite("images/personagens/butcher/8.png")

        self.butcher_list = [self.butcher0, self.butcher1, self.butcher2, self.butcher3,
                             self.butcher4, self.butcher5, self.butcher6, self.butcher7,
                             self.butcher8]
        self.butcher = Sprite("images/personagens/butcher/0.png")
        self.butcher.x = 1300 - self.butcher.width
        self.butcher.y = 540 - self.butcher.height
        #endregion

        #region Dialogo
        self.fundo_dialogo = Sprite("images/dialogo/fundo.png")
        self.fundo_dialogo.y = 500

        self.detetive_face = Sprite("images/dialogo/detetive_face.png")
        self.detetive_face.y = 520
        self.detetive_face.x = 100

        self.japones_face = Sprite("images/dialogo/japones_face.png")
        self.japones_face.y = 520
        self.japones_face.x = 1100

        self.butcher_face = Sprite("images/dialogo/butcher.png")
        self.butcher_face.y = 520
        self.butcher_face.x = 1100
        #endregion

        #region Indices
        self.cronometoIndice = 0
        self.corridaIndice = 0

        self.velocidade_camera = -1

        self.contador_dialogo2 = 0

        self.state_bonecos = "nada"

        self.velocidade_movimento = 0.3
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

    def animate_butcher(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 8:
            self.corridaIndice = 0
        #region butcher
        self.butcher_list[self.corridaIndice].x = self.butcher.x
        self.butcher_list[self.corridaIndice].y = self.butcher.y
        self.butcher_list[self.corridaIndice].draw()
        #endregion

    def cena(self):
        self.detetive.draw()
        self.japones.draw()
        if (self.state_bonecos == "andando"):
            self.animate_butcher()
            self.butcher.move_x(-0.2)
        if (self.state_bonecos == "parado"):
            self.butcher.draw()
        self.dialogo()

    def dialogo(self):
        self.contador_dialogo2 += gamestates.vel_cena

        if (1 < self.contador_dialogo2 < 5):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Estamos dentro, agora não há mais volta.",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (5 < self.contador_dialogo2 < 8):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Silêncio! Tem alguém vindo.",
                                  x=self.japones_face.x - 800, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)
        if (self.contador_dialogo2 > 5):
            self.state_bonecos = "andando"

        if (8 < self.contador_dialogo2 < 13):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.state_bonecos = "parado"
            self.janela.draw_text("Argh! O que estão fazendo aqui?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (13 < self.contador_dialogo2 < 18):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.state_bonecos = "parado"
            self.janela.draw_text("Espera, eu conheço você.",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (18 < self.contador_dialogo2 < 23):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.state_bonecos = "parado"
            self.janela.draw_text("Você é o açougueiro da Newbury Street!",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (23 < self.contador_dialogo2 < 28):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.state_bonecos = "parado"
            self.janela.draw_text("Você não deveria estar aqui detetive.",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo2 > 28):
            gamestates.GameState = 3

    def toca_musica(self):
        if gamestates.GameState == 2:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def run(self):
        #draw
        self.background2.draw()

        self.cena()

        self.toca_musica()