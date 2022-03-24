from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene3():
    def __init__(self, janela):
        self.janela = janela

        #region Backgrounds e mapas
        self.background2 = GameImage("images/backgrounds/background2.jpg")
        #endregion

        #region Personagens
        self.detetive = Sprite("images/personagens/detetive/0.png")
        self.detetive.x = 300 - self.detetive.width
        self.detetive.y = 540 - self.detetive.height
        #endregion

        #region Butcher
        self.butcher2 = Sprite("images/personagens/butcher/morrendo/2.png")
        self.butcher3 = Sprite("images/personagens/butcher/morrendo/3.png")
        self.butcher4 = Sprite("images/personagens/butcher/morrendo/4.png")
        self.butcher5 = Sprite("images/personagens/butcher/morrendo/5.png")

        self.butcher_list = [self.butcher2, self.butcher3,
                             self.butcher4, self.butcher5]
        self.butcher = Sprite("images/personagens/butcher/morrendo/2.png")
        self.butcher.x = 1082.39 - self.butcher.width
        self.butcher.y = 540 - self.butcher.height
        #endregion

        #region Japonês
        self.japones0 = Sprite("images/personagens/japones/0.png")
        self.japones1 = Sprite("images/personagens/japones/1.png")
        self.japones2 = Sprite("images/personagens/japones/2.png")
        self.japones3 = Sprite("images/personagens/japones/3.png")
        self.japones4 = Sprite("images/personagens/japones/4.png")
        self.japones5 = Sprite("images/personagens/japones/5.png")
        self.japones6 = Sprite("images/personagens/japones/6.png")
        self.japones7 = Sprite("images/personagens/japones/7.png")
        self.japones8 = Sprite("images/personagens/japones/8.png")

        self.japonesKill0 = Sprite("images/personagens/japones/matando/0.png")
        self.japonesKill1 = Sprite("images/personagens/japones/matando/1.png")
        self.japonesKill2 = Sprite("images/personagens/japones/matando/2.png")
        self.japonesKill3 = Sprite("images/personagens/japones/matando/3.png")
        self.japonesKill4 = Sprite("images/personagens/japones/matando/4.png")
        self.japonesKill5 = Sprite("images/personagens/japones/matando/5.png")

        self.japones_list = [self.japones0, self.japones1, self.japones2, self.japones3,
                              self.japones4, self.japones5, self.japones6, self.japones7,
                              self.japones8]
        self.japones_listKill = [self.japonesKill0, self.japonesKill1, self.japonesKill2, self.japonesKill3,
                              self.japonesKill4, self.japonesKill5]
        self.japones = Sprite("images/personagens/japones/0.png")
        self.japones.x = 200 - self.japones.width
        self.japones.y = 545 - self.japones.height
        #endregion

        #region Dialogo
        self.fundo_dialogo = Sprite("images/dialogo/fundo.png")
        self.fundo_dialogo.y = 500

        self.detetive_face = Sprite("images/dialogo/detetive_face.png")
        self.detetive_face.y = 520
        self.detetive_face.x = 100

        self.japones_face = Sprite("images/dialogo/japones_face.png")
        self.japones_face.y = 520
        self.japones_face.x = 100

        self.butcher_face = Sprite("images/dialogo/butcher.png")
        self.butcher_face.y = 520
        self.butcher_face.x = 1100
        #endregion

        #region Indices
        self.cronometoIndice = 0
        self.corridaIndice = 0

        self.velocidade_camera = -1

        self.contador_dialogo3 = 0

        self.state_bonecos = "nada"

        self.velocidade_movimento = 0.3
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

    def animate_butcher(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 33:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 4:
            self.corridaIndice = 0
        #region butcher
        self.butcher_list[self.corridaIndice].x = self.butcher.x
        self.butcher_list[self.corridaIndice].y = self.butcher.y
        self.butcher_list[self.corridaIndice].draw()
        #endregion

    def animate_Kuroshido(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 8:
            self.corridaIndice = 0
        #region japones
        self.japones_list[self.corridaIndice].x = self.japones.x
        self.japones_list[self.corridaIndice].y = self.japones.y
        self.japones_list[self.corridaIndice].draw()
        #endregion

    def animate_KuroshidoMatando(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 20:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 5:
            self.corridaIndice = 0
        #region japones
        self.japones_listKill[self.corridaIndice].x = self.japones.x
        self.japones_listKill[self.corridaIndice].y = self.japones.y
        self.japones_listKill[self.corridaIndice].draw()
        #endregion

    def cena(self):
        self.detetive.draw()
        if self.state_bonecos == "andando" and (self.japones.x + self.japones.width) < self.butcher.x:
            self.animate_Kuroshido()
            self.japones.move_x(0.7)
            self.butcher.draw()
        elif self.state_bonecos == "matando":
            self.animate_KuroshidoMatando()
            self.butcher.draw()
        elif (self.state_bonecos == "morrendo"):
            self.animate_butcher()
            self.japones.draw()
        elif (self.state_bonecos == "morto"):
            self.japones.draw()
            self.butcher5.x = self.butcher.x
            self.butcher5.y = self.butcher.y
            self.butcher5.draw()
        else:
            self.japones.draw()
            self.butcher.draw()
        self.dialogo()

    def dialogo(self):
        self.contador_dialogo3 += gamestates.vel_cena

        if (1 < self.contador_dialogo3 < 5):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.janela.draw_text("Vocês não tem noção do que fizeram...",
                                  x=self.butcher_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (5 < self.contador_dialogo3 < 10):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Açougueiro, fale agora o que está acontecendo, ou você",
                                  x=self.japones_face.x + 200, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)
            self.janela.draw_text("pagará pela minha lâmina!",
                                  x=self.japones_face.x + 200, y=650, size=20, color=(255, 0, 0), font_name="Verdana",
                                  bold=True, italic=False)

        if (10 < self.contador_dialogo3 < 15):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.janela.draw_text("No momento que vocês entraram aqui, a fúria",
                                  x=self.butcher_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)
            self.janela.draw_text("de Cyaegha foi despertada!",
                                  x=self.butcher_face.x - 800, y=650, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (15 < self.contador_dialogo3 < 20):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Cyaegha? O que é isso?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (20 < self.contador_dialogo3 < 25):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Fale agora, imundo!",
                                  x=self.japones_face.x + 200, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)

        if (25 < self.contador_dialogo3 < 30):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.janela.draw_text("Cyaegha ephaiehye yah'or'nanah ah na'ah'ehye, hup Freihausgarten l' Boston...",
                                  x=self.butcher_face.x - 1050, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)


        if (30 < self.contador_dialogo3 < 35):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("O que você está falando? Kuroshido, acabe com isso.",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo3 > 32):
            self.state_bonecos = "andando"

        if (35 < self.contador_dialogo3 < 40):
            self.fundo_dialogo.draw()
            self.butcher_face.draw()
            self.janela.draw_text("...riuh'eor sings Cyaegha's vulgtmog, ng hup llll mountain dunkelhügel Cyaegha ephaiemerge",
                                  x=self.butcher_face.x - 1050, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo3 > 40):
            self.state_bonecos = "matando"
        if (self.contador_dialogo3 > 43):
            self.state_bonecos = "morrendo"
        if (self.contador_dialogo3 > 45):
            self.state_bonecos = "morto"
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Vamos continuar...",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)
        if (self.contador_dialogo3 > 47):
            gamestates.GameState = 5

    def toca_musica(self):
        if gamestates.GameState == 4:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def run(self):
        #draw
        self.background2.draw()

        self.cena()

        self.toca_musica()