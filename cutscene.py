from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene():
    def __init__(self, janela):
        self.janela = janela

        #region Backgrounds e mapas
        self.background1 = GameImage("images/backgrounds/background1.jpg")
        self.mapa1 = Sprite("images/mapas/mapa1.png")
        #endregion

        #region Detetive
        self.detetive0 = Sprite("images/personagens/detetive/0.png")
        self.detetive1 = Sprite("images/personagens/detetive/1.png")
        self.detetive2 = Sprite("images/personagens/detetive/2.png")
        self.detetive3 = Sprite("images/personagens/detetive/3.png")
        self.detetive4 = Sprite("images/personagens/detetive/4.png")
        self.detetive5 = Sprite("images/personagens/detetive/5.png")
        self.detetive6 = Sprite("images/personagens/detetive/6.png")
        self.detetive7 = Sprite("images/personagens/detetive/7.png")
        self.detetive8 = Sprite("images/personagens/detetive/8.png")

        self.detetive_list = [self.detetive0, self.detetive1, self.detetive2, self.detetive3,
                              self.detetive4, self.detetive5, self.detetive6, self.detetive7,
                              self.detetive8]
        self.detetive = Sprite("images/personagens/detetive/0.png")
        self.detetive.x = 300 - self.detetive.width
        self.detetive.y = 640 - self.detetive.height
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

        self.japones_list = [self.japones0, self.japones1, self.japones2, self.japones3,
                              self.japones4, self.japones5, self.japones6, self.japones7,
                              self.japones8]
        self.japones = Sprite("images/personagens/japones/0.png")
        self.japones.x = 200 - self.japones.width
        self.japones.y = 645 - self.japones.height
        #endregion

        #region Criança
        self.crianca0 = Sprite("images/personagens/crianca/0.png")
        self.crianca1 = Sprite("images/personagens/crianca/1.png")
        self.crianca2 = Sprite("images/personagens/crianca/2.png")
        self.crianca3 = Sprite("images/personagens/crianca/3.png")
        self.crianca4 = Sprite("images/personagens/crianca/4.png")
        self.crianca5 = Sprite("images/personagens/crianca/5.png")
        self.crianca6 = Sprite("images/personagens/crianca/6.png")
        self.crianca7 = Sprite("images/personagens/crianca/7.png")
        self.crianca8 = Sprite("images/personagens/crianca/8.png")

        self.crianca_list = [self.crianca0, self.crianca1, self.crianca2, self.crianca3,
                              self.crianca4, self.crianca5, self.crianca6, self.crianca7,
                              self.crianca8]
        self.crianca = Sprite("images/personagens/crianca/0.png")
        self.crianca.x = 200 - self.crianca.width
        self.crianca.y = 647 - self.crianca.height
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

        self.crianca_face = Sprite("images/dialogo/crianca_face.png")
        self.crianca_face.y = 520
        self.crianca_face.x = 100
        #endregion

        #region Indices
        self.cronometoIndice = 0
        self.corridaIndice = 0

        self.velocidade_camera = -1

        self.contador_dialogo1 = 0
        self.mostrar_dialogo = True

        self.vai_crianca = False

        self.velocidade_movimento = 0.3
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

        self.historia_introduction = Sprite("images/introduction/historia.png")

    def animate(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 8:
            self.corridaIndice = 0
        #region detetive
        self.detetive_list[self.corridaIndice].x = self.detetive.x
        self.detetive_list[self.corridaIndice].y = self.detetive.y
        self.detetive_list[self.corridaIndice].draw()
        #endregion

        #region japones
        self.japones_list[self.corridaIndice].x = self.japones.x
        self.japones_list[self.corridaIndice].y = self.japones.y
        self.japones_list[self.corridaIndice].draw()
        #endregion

    def animate_crianca(self):
        self.crianca.move_x(0.60)
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.corridaIndice += 1
            self.cronometoIndice = 0
        if self.corridaIndice == 8:
            self.corridaIndice = 0
        self.crianca_list[self.corridaIndice].x = self.crianca.x
        self.crianca_list[self.corridaIndice].y = self.crianca.y
        self.crianca_list[self.corridaIndice].draw()

    def cena(self):
        self.mapa1.move_x(self.velocidade_camera)

        if self.mapa1.x > -2200:
            self.animate()
            self.detetive.move_x(self.velocidade_movimento)
            self.japones.move_x(self.velocidade_movimento)

        if self.mapa1.x < -2200:
            self.detetive.x = 907.7
            self.japones.x = 779.7
            self.detetive.draw()
            self.japones.draw()
            self.velocidade_camera = 0
            if self.mostrar_dialogo == True:
                self.dialogo()

        if self.vai_crianca == True:
            self.detetive.hide()
            self.japones.hide()
            self.animate_crianca()
            self.dialogo_crianca()
            if self.crianca.x > 1280:
                gamestates.GameState = 2

    def dialogo(self):
        self.contador_dialogo1 += gamestates.vel_cena

        if (1 < self.contador_dialogo1 < 5):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Kuroshido, tem certeza disso? É sua última chance, depois disso não tem mais volta.",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (5 < self.contador_dialogo1 < 10):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Tenho meu caro amigo Patrick, eu tenho uma dívida eterna com você.",
                                  x=self.japones_face.x - 800, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)

        if (10 < self.contador_dialogo1 < 15):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Então vamos, antes que seja tarde!",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo1 > 15):
            self.mostrar_dialogo = False
            self.vai_crianca = True

    def dialogo_crianca(self):
        self.fundo_dialogo.draw()
        self.crianca_face.draw()
        self.janela.draw_text("Eu nunca vou deixar meu pai sozinho!",
                              x=self.crianca_face.x + 200, y=620, size=20, color=(0, 255, 0), font_name="Verdana", bold=True, italic=False)

    def toca_musica(self):
        if gamestates.GameState == 1:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def introduction(self):
        self.janela.set_background_color([0,0,0])
        self.historia_introduction.draw()
        self.historia_introduction.move_y(-0.1)
        if self.historia_introduction.y < -2500:
            self.historia_introduction.hide()


    def run(self):
        self.introduction()

        if self.historia_introduction.y < -2500:
            #region Draws
            self.background1.draw()
            self.mapa1.draw()
            #endregion

            self.cena()



        self.toca_musica()